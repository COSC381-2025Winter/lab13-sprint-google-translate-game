import pytest 
from translate_game.translation import translate_text

#Test tranlsation from English to Korean
def test_translation_ko():
    #Arrange
    translatedText = translate_text("Hello, how are you?", "en", "ko")

    #Assert
    assert "안녕하세요. 어떻게 지내세요?" in translatedText

#Test tranlsation from English to Spanish
def test_translation_es():
    #Arrange
    translatedText = translate_text("Hello, how are you?", "en", "es")

    #Assert
    assert "¿Hola, cómo estás?" in translatedText

#Test tranlsation from English to Manderin
def test_translation_zh():
    #Arrange
    translatedText = translate_text("Hello, how are you?", "en", "zh")

    #Assert
    assert "你好吗？" in translatedText
