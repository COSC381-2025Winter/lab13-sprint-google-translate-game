import os

# Import the Google Cloud Translation library.
from google.cloud import translate_v3

PROJECT_ID = os.environ.get("GOOGLE_CLOUD_PROJECT", "galvanic-circle-456503-r4")

def translate_text(
    text: str = "YOUR_TEXT_TO_TRANSLATE",
    source_language_code: str = "en-US",
    target_language_code: str = "fr",
) -> translate_v3.TranslationServiceClient:
    """Translate Text from a Source language to a Target language.
    Args:
        text: The content to translate.
        source_language_code: The code of the source language.
        target_language_code: The code of the target language.
            For example: "fr" for French, "es" for Spanish, etc.
            Find available languages and codes here:
            https://cloud.google.com/translate/docs/languages#neural_machine_translation_model
    """

    # Initialize Translation client.
    client = translate_v3.TranslationServiceClient()
    parent = f"projects/{PROJECT_ID}/locations/global"

    # MIME type of the content to translate.
    # Supported MIME types:
    # https://cloud.google.com/translate/docs/supported-formats
    mime_type = "text/plain"

    # Translate text from the source to the target language.
    response = client.translate_text(
        contents=[text],
        parent=parent,
        mime_type=mime_type,
        source_language_code=source_language_code,
        target_language_code=target_language_code,
    )

    # Display the translation for the text.
    # For example, for "Hello! How are you doing today?":
    # Translated text: Bonjour comment vas-tu aujourd'hui?
    for translation in response.translations:
        return translation.translated_text

    return response