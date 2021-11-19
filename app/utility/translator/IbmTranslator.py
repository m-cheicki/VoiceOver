import os
from datetime import date
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

api_key = os.environ.get('IBM_TRANSLATION_API_KEY')
api_url = os.environ.get('IBM_TRANSLATION_API_URL')

if not api_key or not api_url:
    raise ValueError('IBM_TRANSLATION_API_KEY or IBM_TRANSLATION_API_URL is not set in environment variables')

ibm_version = date.today().strftime('%Y-%m-%d')
ibm_authenticator = IAMAuthenticator(api_key)
ibm_translator = LanguageTranslatorV3(version=ibm_version, authenticator=ibm_authenticator)
ibm_translator.set_service_url(api_url)

def translate(text, target_language):
    """
    Translate text to target language using IBM Watson Language Translator API
    :param text: text to translate
    :param target_language: target language
    """
    translation = ibm_translator.translate(text=text, target=target_language).get_result()
    return translation['translations'][0]['translation']