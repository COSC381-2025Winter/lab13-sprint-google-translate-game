import pytest
import translate_game.score_board


def test_perfect_score(capsys, monkeypatch):
    def mock_translate(text, src, tgt):
        return f"translated({text})"
    monkeypatch.setattr("translate_game.score_board.translate_text", mock_translate)

    user_answers = ['a'] * 10
    correct_answers = ['a'] * 10
    translate_game.score_board.evaluate_quiz(user_answers, correct_answers, 'ko')
    captured = capsys.readouterr()
    assert "You scored 10 out of 10!" in captured.out
    assert "Grade: A" in captured.out

def test_partial_score_with_translation(capsys, monkeypatch):
    def mock_translate(text, src, tgt):
        return f"translated({text})"

    # Patch the correct reference
    monkeypatch.setattr(translate_game.score_board, "translate_text", mock_translate)

    user_answers = ['a'] * 7 + ['x', 'x', 'x']
    correct_answers = ['a'] * 10
    translate_game.score_board.evaluate_quiz(user_answers, correct_answers, 'ko')
    captured = capsys.readouterr()

    assert captured.out.count("Google Translate: translated(a)") == 3
    assert "Wrong number: 8" in captured.out
    assert "Wrong number: 9" in captured.out
    assert "Wrong number: 10" in captured.out

def test_low_score(capsys, monkeypatch):
    def mock_translate(text, src, tgt):
        return f"translated({text})"
    monkeypatch.setattr("translate_game.score_board.translate_text", mock_translate)

    user_answers = ['x'] * 10
    correct_answers = ['a'] * 10
    translate_game.score_board.evaluate_quiz(user_answers, correct_answers, 'ko')
    captured = capsys.readouterr()
    assert "You scored 0 out of 10!" in captured.out
    assert "Grade: C" in captured.out