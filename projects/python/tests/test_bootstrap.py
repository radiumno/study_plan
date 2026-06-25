from scripts import bootstrap as bs


def test_project_python_points_into_venv(monkeypatch, tmp_path) -> None:
    monkeypatch.setattr(bs, "VENV_DIR", tmp_path / ".venv")
    python_path = bs.project_python()
    assert python_path.endswith("/.venv/bin/python")


def test_build_parser_accepts_skip_healthcheck() -> None:
    parser = bs.build_parser()
    args = parser.parse_args(["--skip-healthcheck"])
    assert args.skip_healthcheck is True


def test_run_healthcheck_skips_when_flag_set(monkeypatch) -> None:
    calls: list[list[str]] = []

    def fake_run(cmd: list[str]) -> None:
        calls.append(cmd)

    monkeypatch.setattr(bs, "run", fake_run)
    bs.run_healthcheck(True)
    assert calls == []


def test_run_healthcheck_invokes_health_script(monkeypatch) -> None:
    calls: list[list[str]] = []

    def fake_run(cmd: list[str]) -> None:
        calls.append(cmd)

    monkeypatch.setattr(bs, "run", fake_run)
    monkeypatch.setattr(bs, "project_python", lambda: "/tmp/project-python")
    bs.run_healthcheck(False)
    assert calls == [["/tmp/project-python", "scripts/healthcheck.py"]]
