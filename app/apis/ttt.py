from flask import request
from flask_restx import Resource, Namespace, fields

from app.core.ibm import IBMService
from app.core.google import GoogleService

api = Namespace('ttt', description='Text translation API')

translationResult = api.model(
    'TranslationResult', {
        'source': fields.String(description='The source text.'),
        'translation': fields.String(description='The translated text.'),
        'provider': fields.String(description='The provider of the translated text.'),
        'language': fields.String(description='The language of the translated text.')
    }
)

@api.route('/')
@api.param('text', 'The text to translate.')
@api.param('provider', 'The provider to perform of the translation.')
class TTT(Resource):
    def _handle_translation(self, text, provider):
        """
        Handles the translation of text.
        :param text: The text to be translated.
        :param provider: The translation provider to use.
        """
        translated_text = ""

        try:
            if provider == 'ibm':
                ibm_service = IBMService()
                translated_text = ibm_service.translate(text)
            elif provider == 'google':
                google_service = GoogleService()
                translated_text = google_service.translate(text)
        except Exception:
            pass

        return translated_text

    @api.doc(description='Translate text to english.')
    @api.marshal_with(translationResult)
    def get(self):
        text = request.args.get('text')
        provider = request.args.get('provider')

        if not provider:
            provider = 'google'

        translated_text = ""

        if text and len(text) > 0:
            translated_text = self._handle_translation(text, provider)

        return {
            'source': text,
            'translation': translated_text,
            'provider': provider,
            'language': 'en'
        }