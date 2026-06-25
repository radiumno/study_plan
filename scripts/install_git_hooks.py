from __future__ import annotations

import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
HOOKS_DIR = ROOT / ".githooks"


def ensure_hook(name: str) -> None:
    path = HOOKS_DIR / name
    if not path.exists():
        try:
            display = path.relative_to(ROOT).as_posix()
        except ValueError:
            display = path.as_posix()
        raise FileNotFoundError(f"missing hook file: {display}")
    path.chmod(0o755)


def main() -> int:
    for hook_name in ["pre-commit", "pre-push"]:
        ensure_hook(hook_name)

    subprocess.run(
        ["git", "config", "core.hooksPath", HOOKS_DIR.as_posix()],
        cwd=ROOT,
        check=True,
    )
    print(f"configured git hooks path: {HOOKS_DIR.relative_to(ROOT).as_posix()}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
