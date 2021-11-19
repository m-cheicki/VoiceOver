from googletrans import Translator

translator = Translator()

def translate(text, target_language):
    """
    Translate text to target language using Google Translate API
    :param text: text to translate
    :param target_language: target language
    """
    translation = translator.translate(text, dest=target_language)
    return translation.text