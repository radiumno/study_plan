from __future__ import annotations

import os
import re
from pathlib import Path

try:
    from scripts.shared_paths import (
        DOCS_DIR,
        RESOURCES_DST,
        RESOURCES_INDEX,
        RESOURCES_SRC,
        ROOT,
        TUTORIALS_DST,
        TUTORIALS_INDEX,
        TUTORIALS_SRC,
        iter_day_source_files,
        resource_mirror_path,
        to_root_relative,
        tutorial_mirror_path,
    )
except ModuleNotFoundError:
    from shared_paths import (
        DOCS_DIR,
        RESOURCES_DST,
        RESOURCES_INDEX,
        RESOURCES_SRC,
        ROOT,
        TUTORIALS_DST,
        TUTORIALS_INDEX,
        TUTORIALS_SRC,
        iter_day_source_files,
        resource_mirror_path,
        to_root_relative,
        tutorial_mirror_path,
    )


WIKILINK_RE = re.compile(r"\[\[([^\]|]+)(?:\|([^\]]+))?\]\]")


def to_posix_relative(target: Path, start: Path) -> str:
    return os.path.relpath(target, start).replace(os.sep, "/")


def inject_source_note(text: str, note: str) -> str:
    if text.startswith("---\n"):
        end = text.find("\n---\n", 4)
        if end != -1:
            frontmatter = text[: end + 5]
            body = text[end + 5 :].lstrip("\n")
            return f"{frontmatter}\n> 来源文件: `{note}`\n\n{body}"
    return f"> 来源文件: `{note}`\n\n{text}"


def build_resource_index() -> dict[str, Path]:
    index: dict[str, Path] = {}
    for path in RESOURCES_SRC.rglob("*.md"):
        key = path.stem
        index.setdefault(key, path.relative_to(RESOURCES_SRC))
    return index


def rewrite_wikilinks(text: str, output_path: Path, resource_index: dict[str, Path]) -> str:
    def replace(match: re.Match[str]) -> str:
        name = match.group(1).strip()
        label = (match.group(2) or name).strip()
        target_rel = resource_index.get(name)
        if not target_rel:
            return label
        target = RESOURCES_DST / target_rel
        href = to_posix_relative(target, output_path.parent)
        return f"[{label}]({href})"

    return WIKILINK_RE.sub(replace, text)


def rewrite_doc_links(text: str, output_path: Path) -> str:
    replacements = {
        "resources/lib/资源库.md": RESOURCES_DST / "lib" / "资源库.md",
        "resources/主脉络.md": RESOURCES_DST / "主脉络.md",
        "resources/招聘市场调研报告.md": RESOURCES_DST / "招聘市场调研报告.md",
        "resources/个人信息.md": RESOURCES_DST / "个人信息.md",
        "resources/教学资源参考.md": RESOURCES_DST / "教学资源参考.md",
        "docs/plans/考研备考对照表.md": DOCS_DIR / "plans" / "考研备考对照表.md",
        "docs/references/ai-side/README.md": DOCS_DIR / "references" / "ai-side" / "README.md",
    }
    text = text.replace("`docs/plans/阶段X_名称.md`", "`../plans/` 下对应阶段文件")
    for raw, target in replacements.items():
        href = to_posix_relative(target, output_path.parent)
        text = text.replace(f"`{raw}`", f"`{href}`")
    return text


def mirror_resource_file(src: Path, dst: Path, resource_index: dict[str, Path]) -> None:
    text = src.read_text(encoding="utf-8")
    text = rewrite_wikilinks(text, dst, resource_index)
    text = rewrite_doc_links(text, dst)
    text = inject_source_note(text, src.relative_to(ROOT).as_posix())
    dst.parent.mkdir(parents=True, exist_ok=True)
    dst.write_text(text, encoding="utf-8")


def extract_title(code: str, fallback: str) -> str:
    match = re.search(r"Day\s*\d+\s*\|[^\n\"]+", code)
    if match:
        return match.group(0).strip()
    return fallback


def tutorial_markdown(src: Path) -> str:
    code = src.read_text(encoding="utf-8")
    title = extract_title(code, src.stem)
    rel = to_root_relative(src)
    return (
        f"---\n"
        f"title: {title}\n"
        f"description: 课程源码镜像页，由 scripts/sync_docs.py 生成\n"
        f"---\n\n"
        f"# {title}\n\n"
        f"> 来源文件: `{rel}`\n"
        f"> 说明: 这是文档站镜像页，课程源码仍以项目目录中的 `.py` 文件为准。\n\n"
        f"```python\n{code.rstrip()}\n```\n"
    )


def mirror_tutorial_file(src: Path, dst: Path) -> None:
    dst.parent.mkdir(parents=True, exist_ok=True)
    dst.write_text(tutorial_markdown(src), encoding="utf-8")


def remove_stale_files(root: Path, expected: set[Path]) -> None:
    if not root.exists():
        return
    for path in root.rglob("*"):
        if path.is_file() and path not in expected:
            path.unlink()
    for path in sorted(root.rglob("*"), reverse=True):
        if path.is_dir() and not any(path.iterdir()):
            path.rmdir()


def sync_resources() -> list[Path]:
    resource_index = build_resource_index()
    written: list[Path] = []
    for src in sorted(RESOURCES_SRC.rglob("*.md")):
        dst = resource_mirror_path(src)
        mirror_resource_file(src, dst, resource_index)
        written.append(dst)
    return written


def sync_tutorials() -> list[Path]:
    written: list[Path] = []
    for src in iter_day_source_files():
        dst = tutorial_mirror_path(src)
        mirror_tutorial_file(src, dst)
        written.append(dst)
    return written


def resource_index_markdown() -> str:
    lines = [
        "---",
        "title: 资源库索引",
        "description: resources/ 的文档站入口，由 scripts/sync_docs.py 生成",
        "---",
        "",
        "# 资源库索引",
        "",
        "> 说明: 本页由 `scripts/sync_docs.py` 生成。主资料真源仍在 `resources/`。",
        "",
    ]

    for src in sorted(RESOURCES_SRC.rglob("*.md")):
        rel = src.relative_to(RESOURCES_SRC)
        if rel.name == "index.md":
            continue
        dst = resource_mirror_path(src)
        href = to_posix_relative(dst, RESOURCES_INDEX.parent)
        title = rel.stem
        lines.append(f"- [{title}]({href})")

    lines.append("")
    return "\n".join(lines)


def tutorial_index_markdown() -> str:
    stage_groups: dict[str, list[Path]] = {}
    for src in iter_day_source_files():
        stage_groups.setdefault(src.parent.name, []).append(src)

    lines = [
        "---",
        "title: 教程索引",
        "description: projects/python/ 的文档站入口，由 scripts/sync_docs.py 生成",
        "---",
        "",
        "# 教程索引",
        "",
        "> 说明: 本页由 `scripts/sync_docs.py` 生成。课程真源仍在 `projects/python/`。",
        "",
    ]

    for stage, files in sorted(stage_groups.items()):
        lines.append(f"## {stage}")
        lines.append("")
        for src in files:
            dst = tutorial_mirror_path(src)
            href = to_posix_relative(dst, TUTORIALS_INDEX.parent)
            title = extract_title(src.read_text(encoding="utf-8"), src.stem)
            lines.append(f"- [{title}]({href})")
        lines.append("")

    return "\n".join(lines)


def write_index_pages() -> list[Path]:
    RESOURCES_INDEX.parent.mkdir(parents=True, exist_ok=True)
    RESOURCES_INDEX.write_text(resource_index_markdown(), encoding="utf-8")

    TUTORIALS_INDEX.parent.mkdir(parents=True, exist_ok=True)
    TUTORIALS_INDEX.write_text(tutorial_index_markdown(), encoding="utf-8")

    return [RESOURCES_INDEX, TUTORIALS_INDEX]


def main() -> int:
    resource_files = sync_resources()
    tutorial_files = sync_tutorials()
    index_files = write_index_pages()
    remove_stale_files(RESOURCES_DST, set(resource_files) | {RESOURCES_INDEX})
    remove_stale_files(TUTORIALS_DST, set(tutorial_files))
    for path in index_files:
        print(f"generated index: {path.relative_to(ROOT).as_posix()}")
    print(f"synced resources: {len(resource_files)}")
    print(f"synced tutorials: {len(tutorial_files)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
