from __future__ import annotations

import argparse
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PROJECT_PYTHON = ROOT / ".venv" / "bin" / "python"
PYTHON = str(PROJECT_PYTHON if PROJECT_PYTHON.exists() else Path(sys.executable))


CHECKS = [
    ("docs_sync", "docs sync", [PYTHON, "scripts/sync_docs.py"], "docs"),
    ("docs_structure", "docs structure", [PYTHON, "scripts/check_docs_structure.py"], "docs"),
    (
        "plan_consistency",
        "plan consistency",
        [PYTHON, "scripts/check_plan_consistency.py"],
        "plans",
    ),
    ("course_quality", "course quality", [PYTHON, "scripts/check_course_quality.py"], "course"),
    (
        "plan_consistency_tests",
        "plan consistency tests",
        [PYTHON, "-m", "pytest", "projects/python/tests/test_plan_consistency.py"],
        "tests",
    ),
    (
        "course_quality_tests",
        "course quality tests",
        [PYTHON, "-m", "pytest", "projects/python/tests/test_check_course_quality.py"],
        "tests",
    ),
    (
        "archive_reset_tests",
        "archive reset tests",
        [PYTHON, "-m", "pytest", "projects/python/tests/test_archive_and_clear_filled_exercises.py"],
        "tests",
    ),
    (
        "docs_tooling_tests",
        "docs tooling tests",
        [PYTHON, "-m", "pytest", "projects/python/tests/test_docs_tooling.py"],
        "tests",
    ),
    (
        "healthcheck_tests",
        "healthcheck tests",
        [PYTHON, "-m", "pytest", "projects/python/tests/test_healthcheck.py"],
        "tests",
    ),
    (
        "checks_cli_tests",
        "checks cli tests",
        [PYTHON, "-m", "pytest", "projects/python/tests/test_checks_cli.py"],
        "tests",
    ),
    (
        "install_git_hooks_tests",
        "install git hooks tests",
        [PYTHON, "-m", "pytest", "projects/python/tests/test_install_git_hooks.py"],
        "tests",
    ),
    (
        "bootstrap_tests",
        "bootstrap tests",
        [PYTHON, "-m", "pytest", "projects/python/tests/test_bootstrap.py"],
        "tests",
    ),
    (
        "status_tests",
        "status tests",
        [PYTHON, "-m", "pytest", "projects/python/tests/test_status.py"],
        "tests",
    ),
]
CHECK_GROUPS = ("all", "plans", "docs", "course", "tests")


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Run study_plan repository health checks."
    )
    parser.add_argument(
        "group",
        nargs="?",
        default="all",
        choices=(*CHECK_GROUPS, "list"),
        help="Check subset: all, docs, course, tests, or list available checks.",
    )
    return parser


def select_checks(group: str) -> list[tuple[str, str, list[str], str]]:
    if group == "all":
        return CHECKS
    return [check for check in CHECKS if check[3] == group]


def print_available_checks() -> None:
    print("available healthcheck groups:")
    for group in CHECK_GROUPS:
        print(f"- {group}")
    print("\navailable checks:")
    for check_id, label, _cmd, group in CHECKS:
        print(f"- {check_id} [{group}] -> {label}")


def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)

    if args.group == "list":
        print_available_checks()
        return 0

    selected = select_checks(args.group)
    failed = []
    for _check_id, label, cmd, _group in selected:
        print(f"\n== {label} ==")
        result = subprocess.run(cmd, cwd=ROOT)
        if result.returncode != 0:
            failed.append(label)

    if failed:
        print("\nhealthcheck failed:")
        for label in failed:
            print(f"- {label}")
        return 1

    print("\nhealthcheck passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
