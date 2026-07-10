from __future__ import annotations

import argparse
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PROJECT_PYTHON = ROOT / ".venv" / "bin" / "python"
PYTHON = str(PROJECT_PYTHON if PROJECT_PYTHON.exists() else Path(sys.executable))


COMMANDS = {
    "bootstrap": [PYTHON, "scripts/bootstrap.py"],
    "status": [PYTHON, "scripts/status.py"],
    "sync": [PYTHON, "scripts/sync_docs.py"],
    "plans": [PYTHON, "scripts/healthcheck.py", "plans"],
    "docs": [PYTHON, "scripts/healthcheck.py", "docs"],
    "course": [PYTHON, "scripts/healthcheck.py", "course"],
    "tests": [PYTHON, "scripts/healthcheck.py", "tests"],
    "health": [PYTHON, "scripts/healthcheck.py"],
    "install-hooks": [PYTHON, "scripts/install_git_hooks.py"],
    "reset-stage1": [PYTHON, "scripts/archive_and_clear_filled_exercises.py", "stage1"],
    "reset-stage2": [PYTHON, "scripts/archive_and_clear_filled_exercises.py", "stage2"],
}


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Unified maintenance entrypoint for study_plan."
    )
    parser.add_argument(
        "command",
        nargs="?",
        default="list",
        choices=(*COMMANDS.keys(), "list"),
        help="Maintenance command to run.",
    )
    return parser


def print_available_commands() -> None:
    print("available checks commands:")
    print("- list         -> show available commands")
    print("- bootstrap    -> create venv, install deps/hooks, run healthcheck")
    print("- status       -> show current workspace and environment status")
    print("- sync         -> sync docs mirrors only")
    print("- plans        -> run planning consistency checks")
    print("- docs         -> run docs-only checks")
    print("- course       -> run course-quality hard checks")
    print("- tests        -> run script-level regression tests")
    print("- health       -> run full healthcheck")
    print("- install-hooks -> configure repo-managed git hooks")
    print("- reset-stage1 -> archive and clear filled stage1 exercises")
    print("- reset-stage2 -> archive and clear filled stage2 exercises")


def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)

    if args.command == "list":
        print_available_commands()
        return 0

    cmd = COMMANDS[args.command]
    result = subprocess.run(cmd, cwd=ROOT)
    return result.returncode


if __name__ == "__main__":
    raise SystemExit(main())
