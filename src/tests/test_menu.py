import pytest
from translate_game.menu import mainMenu


def menu_test(monkeypatch, choice, expected):
    #Arrange
    monkeypatch.setattr('builtins.input', lambda _:choice)
    #Act
    result = mainMenu()
    assert result == expected

def test_menu_quit(monkeypatch):
    menu_test(monkeypatch, 'q', 'q')

def test_menu_ko(monkeypatch):
    menu_test(monkeypatch, '1', "ko")

def test_menu_es(monkeypatch):
    menu_test(monkeypatch, '2', "es")

def test_menu_zh(monkeypatch):
    menu_test(monkeypatch, '3', "zh")