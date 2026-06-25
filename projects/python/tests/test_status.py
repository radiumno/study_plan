from pathlib import Path

from scripts import status as st
from scripts.shared_paths import MirrorTarget


def make_target(tmp_path, label: str, source_label: str) -> MirrorTarget:
    return MirrorTarget(
        label=label,
        path=tmp_path / Path(label),
        source_root=tmp_path / source_label.rstrip("/"),
        source_label=source_label,
    )


def patch_root_relative(monkeypatch, tmp_path) -> None:
    monkeypatch.setattr(st, "to_root_relative", lambda path: path.relative_to(tmp_path).as_posix())


def test_normalize_hooks_path_accepts_relative_value(monkeypatch, tmp_path) -> None:
    monkeypatch.setattr(st, "ROOT", tmp_path)
    normalized = st.normalize_hooks_path(".githooks")
    assert normalized == (tmp_path / ".githooks").resolve().as_posix()


def test_hooks_installed_matches_repo_hooks_dir(monkeypatch, tmp_path) -> None:
    hooks_dir = tmp_path / ".githooks"
    hooks_dir.mkdir()
    monkeypatch.setattr(st, "ROOT", tmp_path)
    monkeypatch.setattr(st, "HOOKS_DIR", hooks_dir)
    assert st.hooks_installed(".githooks")
    assert not st.hooks_installed(".other-hooks")


def test_count_status_entries_counts_nonempty_lines() -> None:
    text = " M README.md\n?? docs/resources/\n\n"
    assert st.count_status_entries(text) == 2


def test_summarize_mirror_target_detects_missing(monkeypatch, tmp_path) -> None:
    patch_root_relative(monkeypatch, tmp_path)
    target = make_target(tmp_path, "docs/resources", "resources/")
    mirror_status = st.summarize_mirror_target("", "", target.path, target.source_label)
    assert mirror_status.state == "missing"
    assert mirror_status.reason == "mirror directory missing: docs/resources"


def test_summarize_mirror_target_detects_untracked_with_source_reason(monkeypatch, tmp_path) -> None:
    patch_root_relative(monkeypatch, tmp_path)
    target = make_target(tmp_path, "docs/resources", "resources/")
    target.path.mkdir(parents=True)
    mirror_status = st.summarize_mirror_target(
        " M resources/主脉络.md",
        "?? docs/resources/index.md\n",
        target.path,
        target.source_label,
    )
    assert mirror_status.state == "untracked"
    assert mirror_status.count == 1
    assert mirror_status.reason == "source changes in resources/"


def test_summarize_mirror_target_detects_stale(monkeypatch, tmp_path) -> None:
    patch_root_relative(monkeypatch, tmp_path)
    target = make_target(tmp_path, "docs/tutorials", "projects/python/")
    target.path.mkdir(parents=True)
    mirror_status = st.summarize_mirror_target(
        " M projects/python/stage2_数据处理/day09_Pandas入门.py",
        "",
        target.path,
        target.source_label,
    )
    assert mirror_status.state == "stale"
    assert mirror_status.reason == "source changes in projects/python/"


def test_summarize_mirror_target_detects_dirty_without_source_changes(monkeypatch, tmp_path) -> None:
    patch_root_relative(monkeypatch, tmp_path)
    target = make_target(tmp_path, "docs/tutorials", "projects/python/")
    target.path.mkdir(parents=True)
    mirror_status = st.summarize_mirror_target(
        "",
        " M docs/tutorials/index.md\n",
        target.path,
        target.source_label,
    )
    assert mirror_status.state == "dirty"
    assert mirror_status.reason == "mirror files changed without source updates"


def test_summarize_docs_mirrors_uses_highest_priority_state() -> None:
    summary = st.summarize_docs_mirrors(
        {
            "docs/resources": st.MirrorStatus("stale", 0, "source changes in resources/"),
            "docs/tutorials": st.MirrorStatus("dirty", 1, "mirror files changed without source updates"),
        }
    )
    assert summary.state == "dirty"
    assert summary.count == 1


def test_render_status_formats_summary_with_reasons() -> None:
    rendered = st.render_status(
        {
            "venv_exists": True,
            "python_exists": True,
            "requirements_exists": True,
            "hooks_configured": False,
            "hooks_path": "",
            "hooks_dir_exists": True,
            "docs_mirrors_exist": True,
            "docs_mirror_state": "untracked",
            "docs_mirror_changes": 2,
            "docs_mirror_reason": "source changes in resources/",
            "docs_mirror_details": {
                "docs/resources": st.MirrorStatus("untracked", 1, "source changes in resources/"),
                "docs/tutorials": st.MirrorStatus("untracked", 1, "source changes in projects/python/"),
            },
            "repo_changes": 5,
            "test_files": 9,
        }
    )
    assert "study_plan status" in rendered
    assert "- git hooks: missing" in rendered
    assert "- docs mirrors: untracked (2 paths)" in rendered
    assert "- docs/resources: untracked (1 paths, source changes in resources/)" in rendered
    assert "- docs/tutorials: untracked (1 paths, source changes in projects/python/)" in rendered
    assert "- worktree: dirty (5 paths)" in rendered
    assert "run: python3 scripts/checks.py install-hooks" in rendered
    assert "run: python3 scripts/checks.py docs" in rendered
    assert "inspect: git status --short" in rendered


def test_build_suggestions_distinguishes_stale_and_dirty() -> None:
    stale_suggestions = st.build_suggestions(
        {
            "venv_exists": True,
            "python_exists": True,
            "requirements_exists": True,
            "hooks_configured": True,
            "hooks_path": "",
            "hooks_dir_exists": True,
            "docs_mirrors_exist": True,
            "docs_mirror_state": "stale",
            "docs_mirror_changes": 0,
            "docs_mirror_reason": "source changes in resources/",
            "docs_mirror_details": {
                "docs/resources": st.MirrorStatus("stale", 0, "source changes in resources/"),
                "docs/tutorials": st.MirrorStatus("clean", 0, "in sync"),
            },
            "repo_changes": 0,
            "test_files": 8,
        }
    )
    dirty_suggestions = st.build_suggestions(
        {
            "venv_exists": True,
            "python_exists": True,
            "requirements_exists": True,
            "hooks_configured": True,
            "hooks_path": "",
            "hooks_dir_exists": True,
            "docs_mirrors_exist": True,
            "docs_mirror_state": "dirty",
            "docs_mirror_changes": 1,
            "docs_mirror_reason": "mirror files changed without source updates",
            "docs_mirror_details": {
                "docs/resources": st.MirrorStatus("dirty", 1, "mirror files changed without source updates"),
                "docs/tutorials": st.MirrorStatus("clean", 0, "in sync"),
            },
            "repo_changes": 0,
            "test_files": 8,
        }
    )
    assert "run: python3 scripts/checks.py docs" in stale_suggestions
    assert "inspect: docs mirrors may be hand-edited" not in stale_suggestions
    assert "inspect: docs mirrors may be hand-edited" in dirty_suggestions
    assert "run: python3 scripts/checks.py docs" not in dirty_suggestions
