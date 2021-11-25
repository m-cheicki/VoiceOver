from googletrans import Translator

def translate(text, target_language):
    """
    Translate text to target language using Google Translate API
    :param text: text to translate
    :param target_language: target language
    """
    translator = Translator()
    translation = translator.translate(text, dest=target_language)
    return translation.text