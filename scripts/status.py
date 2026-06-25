from __future__ import annotations

from dataclasses import dataclass
import subprocess
import sys
from pathlib import Path

try:
    from scripts.shared_paths import (
        DOCS_MIRROR_TARGETS,
        HOOKS_DIR,
        REQUIREMENTS_FILE,
        ROOT,
        TESTS_DIR,
        VENV_DIR,
        to_root_relative,
    )
except ModuleNotFoundError:
    from shared_paths import (
        DOCS_MIRROR_TARGETS,
        HOOKS_DIR,
        REQUIREMENTS_FILE,
        ROOT,
        TESTS_DIR,
        VENV_DIR,
        to_root_relative,
    )


if sys.platform == "win32":
    PROJECT_PYTHON = VENV_DIR / "Scripts" / "python.exe"
else:
    PROJECT_PYTHON = VENV_DIR / "bin" / "python"


@dataclass(frozen=True)
class MirrorStatus:
    state: str
    count: int
    reason: str


def run_capture(cmd: list[str]) -> tuple[int, str]:
    result = subprocess.run(
        cmd,
        cwd=ROOT,
        text=True,
        capture_output=True,
    )
    return result.returncode, result.stdout.strip()


def normalize_hooks_path(value: str | None) -> str | None:
    if not value:
        return None
    path = Path(value)
    if not path.is_absolute():
        path = (ROOT / path).resolve()
    return path.as_posix()


def hooks_installed(config_value: str | None) -> bool:
    normalized = normalize_hooks_path(config_value)
    return normalized == HOOKS_DIR.resolve().as_posix()


def count_status_entries(text: str) -> int:
    return sum(1 for line in text.splitlines() if line.strip())


def parse_status_lines(text: str) -> list[str]:
    return [line for line in text.splitlines() if line.strip()]


def has_untracked(lines: list[str]) -> bool:
    return any(line.startswith("??") for line in lines)


def summarize_mirror_target(
    source_status_text: str, mirror_status_text: str, mirror_dir: Path, source_label: str
) -> MirrorStatus:
    mirror_changes = count_status_entries(mirror_status_text)
    mirror_lines = parse_status_lines(mirror_status_text)
    source_changes = count_status_entries(source_status_text)

    if not mirror_dir.exists():
        return MirrorStatus("missing", 0, f"mirror directory missing: {to_root_relative(mirror_dir)}")
    if has_untracked(mirror_lines):
        reason = (
            f"source changes in {source_label}"
            if source_changes
            else "mirror files are untracked"
        )
        return MirrorStatus("untracked", mirror_changes, reason)
    if source_changes > 0:
        return MirrorStatus("stale", mirror_changes, f"source changes in {source_label}")
    if mirror_changes > 0:
        return MirrorStatus("dirty", mirror_changes, "mirror files changed without source updates")
    return MirrorStatus("clean", 0, "in sync")


def collect_mirror_statuses() -> dict[str, MirrorStatus]:
    details: dict[str, MirrorStatus] = {}
    for label, target in DOCS_MIRROR_TARGETS.items():
        source_code, source_output = run_capture(
            ["git", "status", "--short", "--", to_root_relative(target.source_root)]
        )
        mirror_code, mirror_output = run_capture(
            ["git", "status", "--short", "--", to_root_relative(target.path)]
        )
        details[label] = summarize_mirror_target(
            source_output if source_code == 0 else "",
            mirror_output if mirror_code == 0 else "",
            target.path,
            target.source_label,
        )
    return details


def summarize_docs_mirrors(details: dict[str, MirrorStatus]) -> MirrorStatus:
    priority = {
        "missing": 4,
        "dirty": 3,
        "untracked": 2,
        "stale": 1,
        "clean": 0,
    }
    overall = max(details.values(), key=lambda item: priority[item.state])
    total_changes = sum(item.count for item in details.values())
    return MirrorStatus(overall.state, total_changes, overall.reason)


def collect_status() -> dict[str, object]:
    hooks_code, hooks_output = run_capture(["git", "config", "--get", "core.hooksPath"])
    repo_code, repo_output = run_capture(["git", "status", "--short"])
    docs_mirror_details = collect_mirror_statuses()
    docs_mirror_summary = summarize_docs_mirrors(docs_mirror_details)

    return {
        "venv_exists": VENV_DIR.exists(),
        "python_exists": PROJECT_PYTHON.exists(),
        "requirements_exists": REQUIREMENTS_FILE.exists(),
        "hooks_configured": hooks_installed(hooks_output if hooks_code == 0 else None),
        "hooks_path": hooks_output if hooks_code == 0 else "",
        "hooks_dir_exists": HOOKS_DIR.exists(),
        "docs_mirrors_exist": all(target.path.exists() for target in DOCS_MIRROR_TARGETS.values()),
        "docs_mirror_changes": docs_mirror_summary.count,
        "docs_mirror_state": docs_mirror_summary.state,
        "docs_mirror_reason": docs_mirror_summary.reason,
        "docs_mirror_details": docs_mirror_details,
        "repo_changes": count_status_entries(repo_output) if repo_code == 0 else 0,
        "test_files": len(list(TESTS_DIR.glob("test_*.py"))),
    }


def build_suggestions(data: dict[str, object]) -> list[str]:
    suggestions: list[str] = []
    if not data["venv_exists"] or not data["python_exists"]:
        suggestions.append("run: python3 scripts/checks.py bootstrap")
    if not data["hooks_configured"]:
        suggestions.append("run: python3 scripts/checks.py install-hooks")
    mirror_states = [item.state for item in data["docs_mirror_details"].values()]
    if any(state in {"missing", "untracked", "stale"} for state in mirror_states):
        suggestions.append("run: python3 scripts/checks.py docs")
    if any(state == "dirty" for state in mirror_states):
        suggestions.append("inspect: docs mirrors may be hand-edited")
    if data["repo_changes"]:
        suggestions.append("inspect: git status --short")
    return suggestions


def render_status(data: dict[str, object]) -> str:
    hooks_label = "ok" if data["hooks_configured"] else "missing"
    mirror_label = data["docs_mirror_state"]
    repo_label = "clean" if data["repo_changes"] == 0 else "dirty"
    venv_label = "ok" if data["venv_exists"] and data["python_exists"] else "missing"
    requirements_label = "ok" if data["requirements_exists"] else "missing"

    lines = [
        "study_plan status",
        f"- venv: {venv_label}",
        f"- requirements: {requirements_label}",
        f"- git hooks: {hooks_label}",
        f"- docs mirrors: {mirror_label} ({data['docs_mirror_changes']} paths)",
        f"- worktree: {repo_label} ({data['repo_changes']} paths)",
        f"- script tests: {data['test_files']} files",
    ]
    for label, mirror_status in data["docs_mirror_details"].items():
        lines.append(
            f"- {label}: {mirror_status.state} "
            f"({mirror_status.count} paths, {mirror_status.reason})"
        )
    if data["hooks_path"]:
        lines.append(f"- hooks path: {data['hooks_path']}")
    suggestions = build_suggestions(data)
    if suggestions:
        lines.append("- next steps:")
        for item in suggestions:
            lines.append(f"  - {item}")
    return "\n".join(lines)


def main() -> int:
    print(render_status(collect_status()))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
