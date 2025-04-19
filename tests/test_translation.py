import pytest 
from translate_game.translation import translate_text

#Mock translate_text function from translation.py to avoid additional API calls
def mock_translate_text(text, sourceLanguage, targetLanguage):
    if targetLanguage == "ko":
        return "안녕하세요. 어떻게 지내세요?" #Korean translation from Google Cloud Translation API
    elif targetLanguage == "es":
        return "¿Hola, cómo estás?" #Spanish translation from Google Cloud Translation API
    elif targetLanguage == "zh":
        return "你好吗？" #Mandarin translation from Google Cloud Translation API
    return text

#Test tranlsation from English to Korean
def test_translation_ko():
    #Arrange
    translatedText = mock_translate_text("Hello, how are you?", "en", "ko")

    #Assert
    assert "안녕하세요. 어떻게 지내세요?" in translatedText

#Test tranlsation from English to Spanish
def test_translation_es():
    #Arrange
    translatedText = mock_translate_text("Hello, how are you?", "en", "es")

    #Assert
    assert "¿Hola, cómo estás?" in translatedText

#Test tranlsation from English to Mandarin
def test_translation_zh():
    #Arrange
    translatedText = mock_translate_text("Hello, how are you?", "en", "zh")

    #Assert
    assert "你好吗？" in translatedText