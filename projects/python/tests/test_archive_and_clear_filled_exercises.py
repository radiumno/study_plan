from pathlib import Path

from scripts import archive_and_clear_filled_exercises as ace


def test_sanitize_text_keeps_next_exercise_header() -> None:
    text = """
# ↓ 你的代码 ↓
answer = 1
print(answer)

# ■ 练习 1.2: 下一题
# 题目描述
"""
    cleaned = ace.sanitize_text(text)
    assert "# ↓ 你的代码 ↓" in cleaned
    assert "answer = 1" not in cleaned
    assert "# ■ 练习 1.2: 下一题" in cleaned


def test_sanitize_text_keeps_summary_boundary() -> None:
    text = """
# ↓ 你的代码 ↓
value = calc()

# ====================================================
# 今天学到的
# ====================================================
"""
    cleaned = ace.sanitize_text(text)
    assert "value = calc()" not in cleaned
    assert "# 今天学到的" in cleaned


def test_next_archive_root_uses_incrementing_suffix(tmp_path, monkeypatch) -> None:
    monkeypatch.setattr(ace, "ARCHIVE_BASE", tmp_path)

    first = ace.next_archive_root("stage2")
    assert first == tmp_path / f"{ace.date.today().isoformat()}-stage2-reset"

    first.mkdir(parents=True)
    second = ace.next_archive_root("stage2")
    assert second == tmp_path / f"{ace.date.today().isoformat()}-stage2-reset-02"

    second.mkdir(parents=True)
    third = ace.next_archive_root("stage2")
    assert third == tmp_path / f"{ace.date.today().isoformat()}-stage2-reset-03"


def test_should_stop_accepts_total_exercise_boundary() -> None:
    assert ace.should_stop("# ▸ Day 综合练习: 向量化股票分析工具")
    assert ace.should_stop("# ■ 练习 2.1: 向量化计算")
    assert not ace.should_stop("")
    assert not ace.should_stop("result = 1")
