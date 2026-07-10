from __future__ import annotations

import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]

ACTIVE_FILES = (
    "AGENTS.md",
    "README.md",
    "docs/index.md",
    "resources/主脉络.md",
    "resources/招聘市场调研报告.md",
    "docs/plans/技能需求-权重矩阵.md",
    "docs/plans/阶段1_Python_分脉络大纲.md",
    "docs/plans/阶段2_C++算法_分脉络大纲.md",
    "docs/plans/阶段3_C++深入_分脉络大纲.md",
    "docs/plans/阶段4_量化核心AI_分脉络大纲.md",
    "docs/plans/阶段5-6_实习与冲刺_分脉络大纲.md",
    "docs/plans/ai-side/AI辅线_分脉络大纲.md",
    "docs/workflows/写课程流程.md",
    "docs/workflows/写脉络流程.md",
    "docs/workflows/周审流程.md",
)

FORBIDDEN_PATTERNS = (
    (re.compile(r"量化\s*[:：]\s*AI\s*=\s*60\s*[:：]\s*40"), "旧AI比例60:40"),
    (re.compile(r"\bDay\s*30\+?", re.IGNORECASE), "旧Day30触发规则"),
    (re.compile(r"LeetCode\s*500\s*题", re.IGNORECASE), "旧500题硬指标"),
    (re.compile(r"2000\s*-\s*3000\s*元\s*/\s*天"), "未限定的高薪实习口径"),
    (re.compile(r"50\s*-\s*200K"), "疑似误读的薪资口径"),
)

REQUIRED_SECTIONS = {
    "resources/主脉络.md": (
        "## 一、路线结论",
        "## 二、项目层级",
        "## 六、里程碑与闸门",
    ),
    "resources/招聘市场调研报告.md": (
        "## 一、调研范围与证据规则",
        "## 二、岗位族拆分",
        "## 五、薪资与岗位数量口径修正",
    ),
    "docs/plans/阶段1_Python_分脉络大纲.md": (
        "## 1. 阶段终点",
        "## 3. 容量预算",
        "## 9. 阶段闸门",
    ),
    "docs/plans/阶段2_C++算法_分脉络大纲.md": (
        "## 1. 阶段终点",
        "## 2. 容量预算",
        "## 11. 进入阶段3的闸门",
    ),
    "docs/plans/阶段3_C++深入_分脉络大纲.md": (
        "## 1. 阶段终点",
        "## 2. 容量预算",
        "## 9. 进入阶段4的闸门",
    ),
    "docs/plans/阶段4_量化核心AI_分脉络大纲.md": (
        "## 1. 阶段终点",
        "## 2. 容量预算",
        "## 12. 阶段闸门",
    ),
    "docs/workflows/写课程流程.md": (
        "## 一、状态原则",
        "## 五、Step 3: 学习量卡",
        "## 九、Step 7: 四道质量门",
    ),
    "docs/workflows/写脉络流程.md": (
        "## 三、Step 2: 证据复核",
        "## 五、Step 4: 阶段容量预算",
        "## 八、Step 7: 对齐检查",
    ),
}

REQUIRED_TEXT = {
    "resources/主脉络.md": ("至少85%", "最多15%"),
    "docs/plans/阶段4_量化核心AI_分脉络大纲.md": ("至少85%", "最多15%"),
    "README.md": ("精确进度", "vault/会话交接.md"),
}

NO_HARDCODED_DAY_PROGRESS = ("README.md", "docs/index.md")


def scan_forbidden_patterns(relative_path: str, text: str) -> list[str]:
    errors: list[str] = []
    for pattern, label in FORBIDDEN_PATTERNS:
        if pattern.search(text):
            errors.append(f"{relative_path}: 发现{label}")
    return errors


def validate_required_sections(relative_path: str, text: str) -> list[str]:
    errors: list[str] = []
    for heading in REQUIRED_SECTIONS.get(relative_path, ()):
        if heading not in text:
            errors.append(f"{relative_path}: 缺少章节 {heading}")
    for required in REQUIRED_TEXT.get(relative_path, ()):
        if required not in text:
            errors.append(f"{relative_path}: 缺少必需口径 {required}")
    if relative_path in NO_HARDCODED_DAY_PROGRESS and re.search(
        r"Day\s*\d+\s*/\s*\d+", text, re.IGNORECASE
    ):
        errors.append(f"{relative_path}: 不应写死Day进度，改为引用实时状态")
    return errors


def collect_errors(root: Path = ROOT) -> list[str]:
    errors: list[str] = []
    for relative_path in ACTIVE_FILES:
        path = root / relative_path
        if not path.exists():
            errors.append(f"缺少活动规划文件: {relative_path}")
            continue
        text = path.read_text(encoding="utf-8")
        errors.extend(scan_forbidden_patterns(relative_path, text))
        errors.extend(validate_required_sections(relative_path, text))
    return errors


def main() -> int:
    errors = collect_errors()
    if errors:
        print("plan consistency check failed:")
        for error in errors:
            print(f"- {error}")
        return 1

    print("plan consistency check passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
