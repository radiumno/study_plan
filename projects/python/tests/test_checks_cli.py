from scripts import checks


def test_parser_defaults_to_list() -> None:
    parser = checks.build_parser()
    args = parser.parse_args([])
    assert args.command == "list"


def test_parser_accepts_health_command() -> None:
    parser = checks.build_parser()
    args = parser.parse_args(["health"])
    assert args.command == "health"


def test_command_map_contains_core_workflows() -> None:
    assert checks.COMMANDS["bootstrap"][-1] == "scripts/bootstrap.py"
    assert checks.COMMANDS["status"][-1] == "scripts/status.py"
    assert checks.COMMANDS["sync"][-1] == "scripts/sync_docs.py"
    assert checks.COMMANDS["docs"][-2:] == ["scripts/healthcheck.py", "docs"]
    assert checks.COMMANDS["course"][-2:] == ["scripts/healthcheck.py", "course"]
    assert checks.COMMANDS["tests"][-2:] == ["scripts/healthcheck.py", "tests"]
    assert checks.COMMANDS["health"][-1] == "scripts/healthcheck.py"
    assert checks.COMMANDS["reset-stage1"][-1] == "stage1"
    assert checks.COMMANDS["reset-stage2"][-1] == "stage2"
    assert checks.COMMANDS["install-hooks"][-1] == "scripts/install_git_hooks.py"
