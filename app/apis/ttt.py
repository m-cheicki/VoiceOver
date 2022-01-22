from flask import request, abort
from flask_restx import Resource, Namespace, fields

from app.core.ibm import IBMService
from app.core.google import GoogleService

api = Namespace('Translation', description='Text translation API')

translationResult = api.model(
    'TranslationResult', {
        'source': fields.String(description='The source text.'),
        'translation': fields.String(description='The translated text.'),
        'provider': fields.String(description='The provider of the translated text.'),
        'language': fields.String(description='The language of the translated text.')
    }
)

@api.route('/', endpoint='translate')
class TTT(Resource):
    def _check_provider_exist(self, provider):
        """
        Checks if the provider is valid.
        :param provider: The provider to check.
        """
        if provider != 'ibm' and provider != 'google':
            return False

        return True

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
        except Exception as e:
            api.logger.error(f"Error while translating text with provider {provider} : {e}")

        return translated_text

    @api.doc(description='Translate text to english.')
    @api.param('provider', 'The provider to perform of the translation.', _in="formData", required=True, type=str)
    @api.param('text', 'The text to translate.', _in="formData", required=True, type=str)
    @api.expect('application/form-data')
    @api.marshal_with(translationResult, description='The translation result.')
    def post(self):
        text = request.form.get('text')
        provider = request.form.get('provider')

        if not self._check_provider_exist(provider):
            return abort(400, "Provider not supported.")

        translated_text = ""

        if text and len(text) > 0:
            translated_text = self._handle_translation(text, provider)

        return {
            'source': text,
            'translation': translated_text,
            'provider': provider,
            'language': 'en'
        }