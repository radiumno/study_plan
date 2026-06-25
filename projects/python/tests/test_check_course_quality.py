from scripts import check_course_quality as ccq


def collect_warnings(text: str) -> list[str]:
    warnings: list[str] = []
    errors: list[str] = []
    ccq.check_placeholder_blocks(
        ccq.ROOT / "projects/python/stage2_数据处理/day09_Pandas入门.py",
        text,
        errors,
        warnings,
    )
    assert not errors
    return warnings


def collect_total_exercise_errors(text: str) -> list[str]:
    errors: list[str] = []
    ccq.check_total_exercise_placeholders(
        ccq.ROOT / "projects/python/stage2_数据处理/day10_Pandas进阶.py",
        text,
        errors,
    )
    return errors


def test_next_exercise_header_is_not_reported_as_explanation() -> None:
    text = """
# ↓ 你的代码 ↓


# ■ 练习 1.2: 从 dict 创建 Series
# 这里是下一题，不是提示泄漏
"""
    assert collect_warnings(text) == []


def test_summary_section_is_not_reported_as_explanation() -> None:
    text = """
# ↓ 你的代码 ↓


# ====================================================
# 今天学到的
# ====================================================
# ✅ def/return
"""
    assert collect_warnings(text) == []


def test_docstring_after_placeholder_is_not_reported() -> None:
    text = '''
# ↓ 你的代码 ↓

"""
这里是题目补充说明，不是答案
"""
'''
    assert collect_warnings(text) == []


def test_filled_code_after_placeholder_still_warns() -> None:
    text = """
# ↓ 你的代码 ↓
result = prices.mean()
"""
    warnings = collect_warnings(text)
    assert any("已填写代码" in item for item in warnings)


def test_hint_after_placeholder_still_warns() -> None:
    text = """
# ↓ 你的代码 ↓
# 提示：先想想 rolling 和 mean
"""
    warnings = collect_warnings(text)
    assert any("占位区后紧跟提示" in item for item in warnings)


def test_placeholder_and_code_on_same_line_is_error() -> None:
    errors: list[str] = []
    warnings: list[str] = []
    ccq.check_placeholder_blocks(
        ccq.ROOT / "projects/python/stage2_数据处理/day09_Pandas入门.py",
        "# ↓ 你的代码 ↓ result = prices.mean()",
        errors,
        warnings,
    )
    assert any("占位符与代码挤在同一行" in item for item in errors)


def test_total_exercise_requires_placeholder() -> None:
    text = """
# ▸ 知识块4 总练习: 多股票分组统计
#
data_block4 = pd.DataFrame({"ret": [0.1, 0.2]})
"""
    errors = collect_total_exercise_errors(text)
    assert any("总练习区缺少占位符" in item for item in errors)


def test_total_exercise_with_placeholder_is_valid() -> None:
    text = """
# ▸ Day 综合练习: 股票均线策略分析
#
portfolio = pd.DataFrame({"close": [100, 101]})
#
# ↓ 你的代码 ↓
"""
    assert collect_total_exercise_errors(text) == []


def test_appendix_section_does_not_require_placeholder() -> None:
    text = """
# ▸ 附: Baostock 真实 A 股数据
#
print("reference only")
"""
    assert collect_total_exercise_errors(text) == []
