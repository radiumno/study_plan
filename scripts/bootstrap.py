from __future__ import annotations

import argparse
import subprocess
import sys
import venv
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
VENV_DIR = ROOT / ".venv"
REQUIREMENTS_FILE = ROOT / "requirements.txt"


def project_python() -> str:
    if sys.platform == "win32":
        return str(VENV_DIR / "Scripts" / "python.exe")
    return str(VENV_DIR / "bin" / "python")


def run(cmd: list[str]) -> None:
    subprocess.run(cmd, cwd=ROOT, check=True)


def ensure_venv() -> None:
    if VENV_DIR.exists():
        return
    builder = venv.EnvBuilder(with_pip=True)
    builder.create(VENV_DIR)


def install_requirements() -> None:
    run([project_python(), "-m", "pip", "install", "-r", str(REQUIREMENTS_FILE)])


def install_hooks() -> None:
    run([project_python(), "scripts/install_git_hooks.py"])


def run_healthcheck(skip_healthcheck: bool) -> None:
    if skip_healthcheck:
        return
    run([project_python(), "scripts/healthcheck.py"])


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Bootstrap the study_plan workspace."
    )
    parser.add_argument(
        "--skip-healthcheck",
        action="store_true",
        help="Skip the final full healthcheck.",
    )
    return parser


def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)

    ensure_venv()
    install_requirements()
    install_hooks()
    run_healthcheck(args.skip_healthcheck)
    print("bootstrap complete")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
