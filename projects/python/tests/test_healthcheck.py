from scripts import healthcheck as hc


def test_select_checks_all_returns_everything() -> None:
    selected = hc.select_checks("all")
    assert len(selected) == len(hc.CHECKS)


def test_select_checks_docs_filters_group() -> None:
    selected = hc.select_checks("docs")
    assert selected
    assert all(check[3] == "docs" for check in selected)
    assert [check[0] for check in selected] == ["docs_sync", "docs_structure"]


def test_select_checks_course_filters_group() -> None:
    selected = hc.select_checks("course")
    assert selected
    assert all(check[3] == "course" for check in selected)
    assert [check[0] for check in selected] == ["course_quality"]


def test_select_checks_tests_filters_group() -> None:
    selected = hc.select_checks("tests")
    assert selected
    assert all(check[3] == "tests" for check in selected)


def test_parser_accepts_list_group() -> None:
    parser = hc.build_parser()
    args = parser.parse_args(["list"])
    assert args.group == "list"
