import pytest 
from translate_game.selectingQuizQuestions import quiz


def test_list_has_10_answers(monkeypatch, capsys):
    responses = iter(['a','a','a','a','a','a','a','a','a','a'])
    monkeypatch.setattr('builtins.input', lambda _: next(responses))
    userAnswer , correctAnswers, language = quiz("ko")

    assert len(userAnswer) == 10
    assert len(correctAnswers) == 10

def test_language(monkeypatch):
    responses = iter(['a','a','a','a','a','a','a','a','a','a'])
    monkeypatch.setattr('builtins.input', lambda _: next(responses))
    userAnswer , correctAnswers, language = quiz("ko")

    assert language == "ko"

def test_userAnswers_has_input(monkeypatch):
    responses = iter(['a','a','a','a','a','a','a','a','a','a'])
    monkeypatch.setattr('builtins.input', lambda _: next(responses))
    userAnswer , correctAnswers, language = quiz("ko")

    assert userAnswer[0] == 'a'
    assert userAnswer[1] == 'a'
    assert userAnswer[2] == 'a'
    assert userAnswer[3] == 'a'
    assert userAnswer[4] == 'a'
    assert userAnswer[5] == 'a'
    assert userAnswer[6] == 'a'
    assert userAnswer[7] == 'a'
    assert userAnswer[8] == 'a'
    assert userAnswer[9] == 'a'



