from __future__ import annotations

import re
from dataclasses import dataclass
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DOCS_DIR = ROOT / "docs"
MKDOCS_FILE = ROOT / "mkdocs.yml"

RESOURCES_SRC = ROOT / "resources"
RESOURCES_DST = DOCS_DIR / "resources"
RESOURCES_INDEX = RESOURCES_DST / "index.md"

TUTORIALS_SRC = ROOT / "projects" / "python"
TUTORIALS_DIR = DOCS_DIR / "tutorials"
TUTORIALS_DST = TUTORIALS_DIR / "python"
TUTORIALS_INDEX = TUTORIALS_DIR / "index.md"

VENV_DIR = ROOT / ".venv"
HOOKS_DIR = ROOT / ".githooks"
REQUIREMENTS_FILE = ROOT / "requirements.txt"
TESTS_DIR = ROOT / "projects" / "python" / "tests"

DAY_FILE_RE = re.compile(r"^day\d+(?:R)?_(?!utils\b).+\.py$")


@dataclass(frozen=True)
class MirrorTarget:
    label: str
    path: Path
    source_root: Path
    source_label: str


DOCS_MIRROR_TARGETS = {
    "docs/resources": MirrorTarget(
        label="docs/resources",
        path=RESOURCES_DST,
        source_root=RESOURCES_SRC,
        source_label="resources/",
    ),
    "docs/tutorials": MirrorTarget(
        label="docs/tutorials",
        path=TUTORIALS_DIR,
        source_root=TUTORIALS_SRC,
        source_label="projects/python/",
    ),
}


def is_day_file_name(name: str) -> bool:
    return bool(DAY_FILE_RE.match(name))


def iter_day_source_files(root: Path | None = None) -> list[Path]:
    search_root = TUTORIALS_SRC if root is None else root
    return sorted(
        path for path in search_root.rglob("*.py") if is_day_file_name(path.name)
    )


def resource_mirror_path(src: Path) -> Path:
    return RESOURCES_DST / src.relative_to(RESOURCES_SRC)


def tutorial_mirror_path(src: Path) -> Path:
    return (TUTORIALS_DST / src.relative_to(TUTORIALS_SRC)).with_suffix(".md")


def to_root_relative(path: Path) -> str:
    return path.relative_to(ROOT).as_posix()
