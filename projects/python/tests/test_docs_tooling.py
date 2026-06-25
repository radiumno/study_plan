from pathlib import Path

from scripts import check_docs_structure as cds
from scripts import sync_docs as sd
from scripts import shared_paths as sp


def patch_repo_paths(monkeypatch, tmp_path) -> None:
    docs_dir = tmp_path / "docs"
    resources_src = tmp_path / "resources"
    resources_dst = docs_dir / "resources"
    resources_index = resources_dst / "index.md"
    tutorials_src = tmp_path / "projects" / "python"
    tutorials_dir = docs_dir / "tutorials"
    tutorials_dst = tutorials_dir / "python"
    tutorials_index = tutorials_dir / "index.md"
    mkdocs_file = tmp_path / "mkdocs.yml"

    monkeypatch.setattr(sp, "ROOT", tmp_path)
    monkeypatch.setattr(sp, "DOCS_DIR", docs_dir)
    monkeypatch.setattr(sp, "RESOURCES_SRC", resources_src)
    monkeypatch.setattr(sp, "RESOURCES_DST", resources_dst)
    monkeypatch.setattr(sp, "RESOURCES_INDEX", resources_index)
    monkeypatch.setattr(sp, "TUTORIALS_SRC", tutorials_src)
    monkeypatch.setattr(sp, "TUTORIALS_DIR", tutorials_dir)
    monkeypatch.setattr(sp, "TUTORIALS_DST", tutorials_dst)
    monkeypatch.setattr(sp, "TUTORIALS_INDEX", tutorials_index)
    monkeypatch.setattr(sp, "MKDOCS_FILE", mkdocs_file)

    monkeypatch.setattr(sd, "ROOT", tmp_path)
    monkeypatch.setattr(sd, "DOCS_DIR", docs_dir)
    monkeypatch.setattr(sd, "RESOURCES_SRC", resources_src)
    monkeypatch.setattr(sd, "RESOURCES_DST", resources_dst)
    monkeypatch.setattr(sd, "RESOURCES_INDEX", resources_index)
    monkeypatch.setattr(sd, "TUTORIALS_SRC", tutorials_src)
    monkeypatch.setattr(sd, "TUTORIALS_DST", tutorials_dst)
    monkeypatch.setattr(sd, "TUTORIALS_INDEX", tutorials_index)

    monkeypatch.setattr(cds, "ROOT", tmp_path)
    monkeypatch.setattr(cds, "DOCS_DIR", docs_dir)
    monkeypatch.setattr(cds, "MKDOCS_FILE", mkdocs_file)
    monkeypatch.setattr(cds, "RESOURCES_SRC", resources_src)
    monkeypatch.setattr(cds, "RESOURCES_DST", resources_dst)
    monkeypatch.setattr(cds, "RESOURCES_INDEX", resources_index)
    monkeypatch.setattr(cds, "TUTORIALS_DIR", tutorials_dir)
    monkeypatch.setattr(cds, "TUTORIALS_DST", tutorials_dst)
    monkeypatch.setattr(cds, "TUTORIALS_INDEX", tutorials_index)


def test_inject_source_note_preserves_frontmatter() -> None:
    text = "---\ntitle: Demo\n---\n\n正文"
    result = sd.inject_source_note(text, "resources/demo.md")
    assert result.startswith("---\ntitle: Demo\n---\n")
    assert "> 来源文件: `resources/demo.md`" in result
    assert result.rstrip().endswith("正文")


def test_rewrite_wikilinks_uses_relative_docs_path(monkeypatch, tmp_path) -> None:
    patch_repo_paths(monkeypatch, tmp_path)
    output_path = sd.RESOURCES_DST / "lib" / "资源库.md"
    resource_index = {"主脉络": Path("主脉络.md")}
    result = sd.rewrite_wikilinks("见 [[主脉络|路线图]]", output_path, resource_index)
    assert result == "见 [路线图](../主脉络.md)"


def test_rewrite_doc_links_maps_known_targets(monkeypatch, tmp_path) -> None:
    patch_repo_paths(monkeypatch, tmp_path)
    output_path = sd.RESOURCES_DST / "个人信息.md"
    text = "`resources/lib/资源库.md` `docs/references/ai-side/README.md`"
    result = sd.rewrite_doc_links(text, output_path)
    assert "`lib/资源库.md`" in result
    assert "`../references/ai-side/README.md`" in result


def test_tutorial_markdown_contains_title_source_and_code(tmp_path, monkeypatch) -> None:
    patch_repo_paths(monkeypatch, tmp_path)
    src = tmp_path / "projects" / "python" / "day99_demo.py"
    src.parent.mkdir(parents=True)
    src.write_text('"""\nDay 99 | Demo Lesson\n"""\nprint("hi")\n', encoding="utf-8")
    result = sd.tutorial_markdown(src)
    assert "title: Day 99 | Demo Lesson" in result
    assert "> 来源文件: `projects/python/day99_demo.py`" in result
    assert '```python\n"""\nDay 99 | Demo Lesson\n"""\nprint("hi")\n```' in result


def test_remove_stale_files_prunes_unexpected_files_and_dirs(tmp_path) -> None:
    root = tmp_path / "docs_out"
    keep = root / "keep.md"
    stale = root / "old" / "stale.md"
    keep.parent.mkdir(parents=True)
    stale.parent.mkdir(parents=True)
    keep.write_text("keep", encoding="utf-8")
    stale.write_text("old", encoding="utf-8")

    sd.remove_stale_files(root, {keep})

    assert keep.exists()
    assert not stale.exists()
    assert not stale.parent.exists()


def test_resource_index_markdown_links_mirrored_files(monkeypatch, tmp_path) -> None:
    patch_repo_paths(monkeypatch, tmp_path)
    (sd.RESOURCES_SRC / "lib").mkdir(parents=True)
    (sd.RESOURCES_SRC / "主脉络.md").write_text("# 主脉络\n", encoding="utf-8")
    (sd.RESOURCES_SRC / "lib" / "资源库.md").write_text("# 资源库\n", encoding="utf-8")

    rendered = sd.resource_index_markdown()

    assert "[主脉络](主脉络.md)" in rendered
    assert "[资源库](lib/资源库.md)" in rendered


def test_tutorial_index_markdown_groups_days(monkeypatch, tmp_path) -> None:
    patch_repo_paths(monkeypatch, tmp_path)
    stage1 = sd.TUTORIALS_SRC / "stage1_python基础"
    stage2 = sd.TUTORIALS_SRC / "stage2_数据处理"
    stage1.mkdir(parents=True)
    stage2.mkdir(parents=True)
    (stage1 / "day01_demo.py").write_text('"""\nDay 01 | Demo\n"""\n', encoding="utf-8")
    (stage2 / "day08_demo.py").write_text('"""\nDay 08 | NumPy\n"""\n', encoding="utf-8")

    rendered = sd.tutorial_index_markdown()

    assert "## stage1_python基础" in rendered
    assert "## stage2_数据处理" in rendered
    assert "[Day 01 | Demo](python/stage1_python基础/day01_demo.md)" in rendered
    assert "[Day 08 | NumPy](python/stage2_数据处理/day08_demo.md)" in rendered


def test_iter_nav_paths_flattens_nested_nav() -> None:
    nav = [
        {"首页": "index.md"},
        {"教程": [{"Day 1": "tutorials/day1.md"}, {"Day 2": "tutorials/day2.md"}]},
    ]
    assert list(cds.iter_nav_paths(nav)) == [
        "index.md",
        "tutorials/day1.md",
        "tutorials/day2.md",
    ]


def test_validate_nav_reports_escape_and_missing(tmp_path, monkeypatch) -> None:
    patch_repo_paths(monkeypatch, tmp_path)
    cds.DOCS_DIR.mkdir()
    (cds.DOCS_DIR / "index.md").write_text("# ok\n", encoding="utf-8")
    cds.MKDOCS_FILE.write_text(
        "nav:\n"
        "  - 首页: index.md\n"
        "  - 越界: ../secret.md\n"
        "  - 缺失: missing.md\n",
        encoding="utf-8",
    )

    errors: list[str] = []
    cds.validate_nav(errors)

    assert any("mkdocs nav 越界: ../secret.md" in item for item in errors)
    assert any("mkdocs nav 缺失文件: missing.md" in item for item in errors)


def test_validate_links_ignores_code_fence_but_catches_real_issues(tmp_path, monkeypatch) -> None:
    patch_repo_paths(monkeypatch, tmp_path)
    cds.DOCS_DIR.mkdir()
    (cds.DOCS_DIR / "ok.md").write_text("# ok\n", encoding="utf-8")
    (cds.DOCS_DIR / "fenced.md").write_text(
        "```md\n[[ignored]]\n[bad](missing.md)\n```\n",
        encoding="utf-8",
    )
    (cds.DOCS_DIR / "bad.md").write_text(
        "这里有 [[真实问题]] 和一个 [坏链接](missing.md)\n",
        encoding="utf-8",
    )

    errors: list[str] = []
    cds.validate_links(errors)

    assert any("仍有 Obsidian wikilink: docs/bad.md" in item for item in errors)
    assert any("链接目标不存在: docs/bad.md -> missing.md" in item for item in errors)
    assert not any("fenced.md" in item for item in errors)


def test_validate_expected_dirs_reports_missing_directory(tmp_path, monkeypatch) -> None:
    patch_repo_paths(monkeypatch, tmp_path)
    cds.DOCS_DIR.mkdir()
    for rel in ["plans", "workflows", "references", "resources", "reviews", "templates"]:
        (cds.DOCS_DIR / rel).mkdir()

    errors: list[str] = []
    cds.validate_expected_dirs(errors)

    assert errors == ["缺少目录: docs/tutorials/python"]


def test_validate_generated_mirrors_reports_orphan_and_missing(tmp_path, monkeypatch) -> None:
    patch_repo_paths(monkeypatch, tmp_path)
    cds.RESOURCES_SRC.mkdir(parents=True)
    (cds.RESOURCES_SRC / "主脉络.md").write_text("# 主脉络\n", encoding="utf-8")
    cds.RESOURCES_DST.mkdir(parents=True)
    cds.RESOURCES_INDEX.write_text("# 资源索引\n", encoding="utf-8")
    (cds.RESOURCES_DST / "orphan.md").write_text("# orphan\n", encoding="utf-8")

    cds.TUTORIALS_DIR.mkdir(parents=True)
    cds.TUTORIALS_INDEX.write_text("# 教程索引\n", encoding="utf-8")
    stage = cds.ROOT / "projects" / "python" / "stage1_python基础"
    stage.mkdir(parents=True)
    (stage / "day01_demo.py").write_text('"""\nDay 01 | Demo\n"""\n', encoding="utf-8")

    errors: list[str] = []
    cds.validate_generated_mirrors(errors)

    assert "资源镜像孤儿文件: docs/resources/orphan.md" in errors
    assert "资源镜像缺失文件: docs/resources/主脉络.md" in errors
    assert "教程镜像缺失文件: docs/tutorials/python/stage1_python基础/day01_demo.md" in errors
