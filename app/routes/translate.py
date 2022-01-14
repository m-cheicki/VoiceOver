from flask import Blueprint, request
from app.utility.translator import GoogleTranslator, IbmTranslator

blueprint = Blueprint('translate', __name__, url_prefix='/api/translate')

def __handle_translate(text, lang, provider):
    """
    Handles the translation of text.
    :param text: The text to be translated.
    :param lang: The language to translate to.
    :param provider: The translation provider to use.
    """
    try:
        if provider == 'google':
            translated_text = GoogleTranslator.translate(text, lang)
        elif provider == 'ibm':
            translated_text = IbmTranslator.translate(text, lang)
    except Exception:
        translated_text = ''

    return { 'translation': translated_text, 'source': text, 'lang': lang, 'provider': provider }

@blueprint.route('/', methods=['GET'])
def translate():
    """
    Translate text to target language
    :param text: text to translate
    :param target_language: target language
    """
    text = request.args.get('text')
    lang = request.args.get('lang')
    provider = request.args.get('provider')

    if not text:
        return { 'translation': '', 'source': text, 'lang': lang, 'provider': provider }
    
    if not lang:
        lang = 'en'

    if not provider:
        provider = 'google'

    return __handle_translate(text, lang, provider)