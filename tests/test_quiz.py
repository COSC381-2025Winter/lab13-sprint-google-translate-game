import pytest 
from translate_game import selectingQuizQuestions

# Automatically mock translate_text in all tests
@pytest.fixture(autouse=True)
def patch_translate(monkeypatch):
    monkeypatch.setattr(selectingQuizQuestions, "translate_text", lambda t, s, d: f"translated({t})")

def test_list_has_10_answers(monkeypatch):
    responses = iter(['a'] * 10)
    monkeypatch.setattr('builtins.input', lambda _: next(responses))

    userAnswer, correctAnswers, language = selectingQuizQuestions.quiz("ko")
    assert len(userAnswer) == 10
    assert len(correctAnswers) == 10

def test_language(monkeypatch):
    responses = iter(['a'] * 10)
    monkeypatch.setattr('builtins.input', lambda _: next(responses))

    userAnswer, correctAnswers, language = selectingQuizQuestions.quiz("ko")
    assert language == "ko"

def test_userAnswers_has_input(monkeypatch):
    responses = iter(['a'] * 10)
    monkeypatch.setattr('builtins.input', lambda _: next(responses))

    userAnswer, correctAnswers, language = selectingQuizQuestions.quiz("ko")
    assert userAnswer == ['a'] * 10