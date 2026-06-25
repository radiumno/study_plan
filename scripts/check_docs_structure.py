from __future__ import annotations

import re
from pathlib import Path

import yaml

try:
    from scripts.shared_paths import (
        DOCS_DIR,
        MKDOCS_FILE,
        RESOURCES_DST,
        RESOURCES_INDEX,
        RESOURCES_SRC,
        ROOT,
        TUTORIALS_DIR,
        TUTORIALS_DST,
        TUTORIALS_INDEX,
        iter_day_source_files,
        resource_mirror_path,
        tutorial_mirror_path,
        to_root_relative,
    )
except ModuleNotFoundError:
    from shared_paths import (
        DOCS_DIR,
        MKDOCS_FILE,
        RESOURCES_DST,
        RESOURCES_INDEX,
        RESOURCES_SRC,
        ROOT,
        TUTORIALS_DIR,
        TUTORIALS_DST,
        TUTORIALS_INDEX,
        iter_day_source_files,
        resource_mirror_path,
        tutorial_mirror_path,
        to_root_relative,
    )

LINK_RE = re.compile(r"\[[^\]]+\]\(([^)]+)\)")
CODE_FENCE_RE = re.compile(r"```.*?```", re.DOTALL)


def iter_nav_paths(node):
    if isinstance(node, list):
        for item in node:
            yield from iter_nav_paths(item)
    elif isinstance(node, dict):
        for value in node.values():
            if isinstance(value, str):
                yield value
            else:
                yield from iter_nav_paths(value)


def ensure(condition: bool, message: str, errors: list[str]) -> None:
    if not condition:
        errors.append(message)


def validate_nav(errors: list[str]) -> None:
    config = yaml.safe_load(MKDOCS_FILE.read_text(encoding="utf-8"))
    for path_str in iter_nav_paths(config.get("nav", [])):
        if path_str.startswith(("http://", "https://")):
            continue
        path = Path(path_str)
        ensure(".." not in path.parts, f"mkdocs nav 越界: {path_str}", errors)
        ensure((DOCS_DIR / path).exists(), f"mkdocs nav 缺失文件: {path_str}", errors)


def validate_links(errors: list[str]) -> None:
    for path in DOCS_DIR.rglob("*.md"):
        text = path.read_text(encoding="utf-8")
        prose = CODE_FENCE_RE.sub("", text)
        if "[[" in prose:
            errors.append(f"仍有 Obsidian wikilink: {path.relative_to(ROOT).as_posix()}")
        for match in LINK_RE.finditer(prose):
            target = match.group(1).strip()
            if not target or target.startswith(("http://", "https://", "mailto:", "#")):
                continue
            target = target.split("#", 1)[0]
            resolved = (path.parent / target).resolve()
            try:
                resolved.relative_to(DOCS_DIR.resolve())
            except ValueError:
                errors.append(
                    f"链接越界: {path.relative_to(ROOT).as_posix()} -> {match.group(1)}"
                )
                continue
            if not resolved.exists():
                errors.append(
                    f"链接目标不存在: {path.relative_to(ROOT).as_posix()} -> {match.group(1)}"
                )


def validate_expected_dirs(errors: list[str]) -> None:
    for rel in [
        "plans",
        "workflows",
        "references",
        "resources",
        "reviews",
        "templates",
        "tutorials/python",
    ]:
        ensure((DOCS_DIR / rel).exists(), f"缺少目录: docs/{rel}", errors)


def expected_resource_files() -> set[str]:
    expected = {to_root_relative(RESOURCES_INDEX)}
    for src in sorted(RESOURCES_SRC.rglob("*.md")):
        expected.add(to_root_relative(resource_mirror_path(src)))
    return expected


def expected_tutorial_files() -> set[str]:
    expected = {to_root_relative(TUTORIALS_INDEX)}
    for src in iter_day_source_files():
        expected.add(to_root_relative(tutorial_mirror_path(src)))
    return expected


def validate_generated_mirrors(errors: list[str]) -> None:
    for required in [RESOURCES_INDEX, TUTORIALS_INDEX]:
        ensure(required.exists(), f"缺少生成入口页: {to_root_relative(required)}", errors)

    resource_expected = expected_resource_files()
    resource_actual = {
        to_root_relative(path) for path in RESOURCES_DST.rglob("*.md")
    }
    tutorial_expected = expected_tutorial_files()
    tutorial_actual = {
        to_root_relative(path) for path in TUTORIALS_DIR.rglob("*.md")
    }

    for path in sorted(resource_actual - resource_expected):
        errors.append(f"资源镜像孤儿文件: {path}")
    for path in sorted(resource_expected - resource_actual):
        errors.append(f"资源镜像缺失文件: {path}")

    for path in sorted(tutorial_actual - tutorial_expected):
        errors.append(f"教程镜像孤儿文件: {path}")
    for path in sorted(tutorial_expected - tutorial_actual):
        errors.append(f"教程镜像缺失文件: {path}")


def main() -> int:
    errors: list[str] = []
    validate_nav(errors)
    validate_links(errors)
    validate_expected_dirs(errors)
    validate_generated_mirrors(errors)

    if errors:
        print("docs structure check failed:")
        for item in errors:
            print(f"- {item}")
        return 1

    print("docs structure check passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
