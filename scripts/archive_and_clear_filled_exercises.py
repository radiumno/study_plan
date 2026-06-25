from __future__ import annotations

import shutil
import sys
from datetime import date
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
ARCHIVE_BASE = ROOT / "vault" / "10_RAW" / "代码片段" / "filled_course_snapshots"

TARGET_GROUPS = {
    "stage1": [
        ROOT / "projects" / "python" / "stage1_python基础" / "day02_列表与字典.py",
        ROOT / "projects" / "python" / "stage1_python基础" / "day03_函数.py",
        ROOT / "projects" / "python" / "stage1_python基础" / "day04_set文件异常.py",
        ROOT / "projects" / "python" / "stage1_python基础" / "day05_模块与包.py",
        ROOT / "projects" / "python" / "stage1_python基础" / "day06_股票数据管理器.py",
        ROOT / "projects" / "python" / "stage1_python基础" / "day07_复习课.py",
    ],
    "stage2": [
        ROOT / "projects" / "python" / "stage2_数据处理" / "day08_NumPy数组运算.py",
        ROOT / "projects" / "python" / "stage2_数据处理" / "day08R_NumPy强化课.py",
        ROOT / "projects" / "python" / "stage2_数据处理" / "day09_Pandas入门.py",
        ROOT / "projects" / "python" / "stage2_数据处理" / "day10_Pandas进阶.py",
    ],
}

PLACEHOLDER = "# ↓ 你的代码 ↓"
STOP_PREFIXES = (
    "# ---",
    "# ═",
    "# ▸",
    "# ■",
    "# 今天学到的",
    "# Q",
    'print("\\n" + "="',
    'print("\\n---',
)


def should_stop(line: str) -> bool:
    stripped = line.strip()
    if not stripped:
        return False
    return stripped.startswith(STOP_PREFIXES)


def sanitize_text(text: str) -> str:
    lines = text.splitlines()
    out: list[str] = []
    i = 0

    while i < len(lines):
        line = lines[i]
        if PLACEHOLDER not in line:
            out.append(line)
            i += 1
            continue

        prefix = line.split(PLACEHOLDER, 1)[0]
        out.append(f"{prefix}{PLACEHOLDER}")
        i += 1

        while i < len(lines):
            current = lines[i]
            next_line = lines[i + 1] if i + 1 < len(lines) else ""
            stripped = current.strip()

            if should_stop(current):
                break
            if stripped == "" and (next_line.strip() == "" or should_stop(next_line)):
                break

            i += 1

    return "\n".join(out) + "\n"


def next_archive_root(group: str) -> Path:
    base = ARCHIVE_BASE / f"{date.today().isoformat()}-{group}-reset"
    if not base.exists():
        return base

    suffix = 2
    while True:
        candidate = ARCHIVE_BASE / f"{date.today().isoformat()}-{group}-reset-{suffix:02d}"
        if not candidate.exists():
            return candidate
        suffix += 1


def reset_group(group: str) -> None:
    targets = TARGET_GROUPS[group]
    archive_root = next_archive_root(group)
    archive_root.mkdir(parents=True, exist_ok=True)

    for src in targets:
        archive_path = archive_root / src.relative_to(ROOT)
        archive_path.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(src, archive_path)

        cleaned = sanitize_text(src.read_text(encoding="utf-8"))
        src.write_text(cleaned, encoding="utf-8")
        print(f"sanitized {src.relative_to(ROOT).as_posix()}")

    print(f"archived originals to {archive_root.relative_to(ROOT).as_posix()}")


def main(argv: list[str]) -> int:
    if len(argv) != 2 or argv[1] not in (*TARGET_GROUPS.keys(), "all"):
        print("usage: python3 scripts/archive_and_clear_filled_exercises.py [stage1|stage2|all]")
        return 1

    groups = list(TARGET_GROUPS) if argv[1] == "all" else [argv[1]]
    for group in groups:
        reset_group(group)

    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
