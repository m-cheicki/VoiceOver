import io
from flask import request, send_file, abort
from flask_restx import Resource, Namespace

from app.core.ibm import IBMService
from app.core.google import GoogleService

api = Namespace('TTS', description='Text to speech API')

@api.route('/')
class TTS(Resource):
    def _check_provider_exist(self, provider):
        """
        Checks if the provider is valid.
        :param provider: The provider to check.
        """
        if provider != 'ibm' and provider != 'google':
            return False

        return True
    
    def _handle_synthesis(self, text, provider):
        """
        Handles the synthesis of text.
        :param text: The text to be synthesized.
        :param provider: The synthesis provider to use.
        """
        synthesized_audio = None

        try:
            if provider == 'ibm':
                ibm_service = IBMService()
                synthesized_audio = ibm_service.synthesize(text)
            elif provider == 'google':
                google_service = GoogleService()
                synthesized_audio = google_service.synthesize(text)
        except Exception:
            pass

        return synthesized_audio

    @api.doc(description='Synthesize text to speech.')
    @api.param('provider', 'The provider to perform of the synthesis.', _in="formData", required=True, type=str)
    @api.param('text', 'The text to synthesize.', _in="formData", required=True, type=str)
    @api.expect('application/form-data')
    @api.produces(['application/octet-stream'])
    def post(self):
        text = request.form.get('text')
        provider = request.form.get('provider')

        if not text or len(text) == 0:
            return abort(400, "Text cannot be empty.")

        if not self._check_provider_exist(provider):
            return abort(400, "Provider not supported.")

        synthesized_audio = self._handle_synthesis(text, provider)

        if synthesized_audio:
            return send_file(io.BytesIO(synthesized_audio), mimetype='audio/mp3')

        return abort(500, "Text could not be synthesized.")