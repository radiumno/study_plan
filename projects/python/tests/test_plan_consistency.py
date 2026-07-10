from scripts import check_plan_consistency as cpc


def test_forbidden_patterns_detect_deprecated_rules() -> None:
    text = "量化:AI = 60:40; Day30+; LeetCode 500题"
    errors = cpc.scan_forbidden_patterns("demo.md", text)
    assert len(errors) == 3


def test_required_sections_report_missing_headings() -> None:
    errors = cpc.validate_required_sections("resources/主脉络.md", "# 主脉络")
    assert any("## 一、路线结论" in error for error in errors)
    assert any("至少85%" in error for error in errors)


def test_active_plan_files_are_consistent() -> None:
    assert cpc.collect_errors() == []
