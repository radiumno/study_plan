from __future__ import annotations

import re
from pathlib import Path

try:
    from scripts.shared_paths import ROOT, iter_day_source_files, to_root_relative
except ModuleNotFoundError:
    from shared_paths import ROOT, iter_day_source_files, to_root_relative

DAY_HEADER_RE = re.compile(r"Day\s+\d+(?:R)?\s+\|")
PLACEHOLDER_RE = re.compile(r"# ↓ 你的代码 ↓")
REFERENCE_RE = re.compile(r"参考源[:：]")
PROGRESS_RE = re.compile(r"进度[:：]")
HINT_RE = re.compile(r"#\s*提示[:：]")
SECTION_STOP_PREFIXES = (
    "# ---",
    "# ═",
    "# ▸",
    "# ■",
    "# 今天学到的",
    'print("\\n',
)
EXERCISE_SECTION_PREFIX = "# ▸"


def is_separator_or_blank(line: str) -> bool:
    stripped = line.strip()
    if not stripped:
        return True
    if stripped.startswith("#") and set(stripped.replace("#", "").strip()) <= {"═", "=", "-", " "}:
        return True
    if stripped.startswith(("'''", '"""', '"', "'")):
        return True
    return False


def classify_line(stripped: str) -> str:
    if not stripped:
        return "blank"
    if stripped.startswith("#"):
        if "提示" in stripped:
            return "hint"
        return "comment"
    if stripped.startswith(("'''", '"""', '"', "'")):
        return "doc"
    return "code"


def is_section_boundary(stripped: str) -> bool:
    return stripped.startswith(SECTION_STOP_PREFIXES)


def is_total_exercise_heading(stripped: str) -> bool:
    if not stripped.startswith(EXERCISE_SECTION_PREFIX):
        return False
    if "练习" not in stripped:
        return False
    return not stripped.startswith(("# ▸ 附", "# ▸附"))


def check_placeholder_blocks(path: Path, text: str, errors: list[str], warnings: list[str]) -> None:
    lines = text.splitlines()
    for idx, line in enumerate(lines):
        if not PLACEHOLDER_RE.search(line):
            continue
        if line.strip() != "# ↓ 你的代码 ↓":
            errors.append(
                f"{to_root_relative(path)}:{idx+1} 占位符与代码挤在同一行"
            )
        in_doc_block = False
        doc_delimiter = ""
        for offset in range(1, 6):
            if idx + offset >= len(lines):
                break
            next_line = lines[idx + offset]
            stripped = next_line.strip()
            if in_doc_block:
                if doc_delimiter and doc_delimiter in stripped:
                    in_doc_block = False
                continue
            if is_section_boundary(stripped):
                break
            if stripped.startswith(('"""', "'''")):
                if stripped.count(stripped[:3]) < 2:
                    in_doc_block = True
                    doc_delimiter = stripped[:3]
                continue
            if is_separator_or_blank(next_line):
                continue
            kind = classify_line(stripped)
            if kind == "hint":
                warnings.append(
                    f"{to_root_relative(path)}:{idx+offset+1} 占位区后紧跟提示"
                )
                break
            if kind == "code":
                warnings.append(
                    f"{to_root_relative(path)}:{idx+offset+1} 占位区后出现已填写代码"
                )
                break


def check_total_exercise_placeholders(path: Path, text: str, errors: list[str]) -> None:
    lines = text.splitlines()
    rel = to_root_relative(path)
    for idx, line in enumerate(lines):
        stripped = line.strip()
        if not is_total_exercise_heading(stripped):
            continue

        found_placeholder = False
        for probe in lines[idx + 1 :]:
            probe_stripped = probe.strip()
            if probe_stripped.startswith("# ═") and found_placeholder:
                break
            if probe_stripped.startswith(EXERCISE_SECTION_PREFIX):
                break
            if PLACEHOLDER_RE.search(probe):
                found_placeholder = True
                break

        if not found_placeholder:
            errors.append(f"{rel}:{idx+1} 总练习区缺少占位符")


def check_file_basics(path: Path, text: str, errors: list[str]) -> None:
    if not DAY_HEADER_RE.search(text[:400]):
        errors.append(f"{path.relative_to(ROOT).as_posix()} 缺少 Day 标题头")
    if "stage2_数据处理" in path.as_posix():
        if not REFERENCE_RE.search(text[:1200]):
            errors.append(f"{path.relative_to(ROOT).as_posix()} 缺少参考源段")
        if not PROGRESS_RE.search(text[:1500]):
            errors.append(f"{path.relative_to(ROOT).as_posix()} 缺少进度段")


def check_hint_density(path: Path, text: str, warnings: list[str]) -> None:
    hint_count = len(HINT_RE.findall(text))
    if hint_count > 3:
        warnings.append(f"{to_root_relative(path)} 提示过多 ({hint_count})")


def main() -> int:
    errors: list[str] = []
    warnings: list[str] = []

    files = iter_day_source_files()
    if not files:
        print("no day files found")
        return 1

    for path in files:
        text = path.read_text(encoding="utf-8")
        check_file_basics(path, text, errors)
        check_placeholder_blocks(path, text, errors, warnings)
        check_total_exercise_placeholders(path, text, errors)
        check_hint_density(path, text, warnings)

    if errors:
        print("course quality check failed:")
        for item in errors:
            print(f"- {item}")
    else:
        print("course quality hard checks passed")

    if warnings:
        print("course quality warnings:")
        for item in warnings:
            print(f"- {item}")

    return 1 if errors else 0


if __name__ == "__main__":
    raise SystemExit(main())
