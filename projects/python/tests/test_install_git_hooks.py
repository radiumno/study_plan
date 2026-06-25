from pathlib import Path

from scripts import install_git_hooks as igh


def test_hook_files_exist() -> None:
    assert (igh.HOOKS_DIR / "pre-commit").exists()
    assert (igh.HOOKS_DIR / "pre-push").exists()


def test_ensure_hook_accepts_existing_hook(tmp_path) -> None:
    hook = tmp_path / "pre-commit"
    hook.write_text("#!/bin/sh\nexit 0\n", encoding="utf-8")
    original_dir = igh.HOOKS_DIR
    try:
        igh.HOOKS_DIR = tmp_path
        igh.ensure_hook("pre-commit")
        assert oct(hook.stat().st_mode & 0o777) == "0o755"
    finally:
        igh.HOOKS_DIR = original_dir


def test_ensure_hook_raises_for_missing_file(tmp_path) -> None:
    original_dir = igh.HOOKS_DIR
    try:
        igh.HOOKS_DIR = tmp_path
        try:
            igh.ensure_hook("pre-push")
        except FileNotFoundError as exc:
            assert "missing hook file" in str(exc)
        else:
            raise AssertionError("expected FileNotFoundError")
    finally:
        igh.HOOKS_DIR = original_dir
