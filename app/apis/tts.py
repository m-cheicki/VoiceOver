import io
from flask import request, send_file, abort
from flask_restx import Resource, Namespace

from app.core.ibm import IBMService
from app.core.google import GoogleService

api = Namespace('tts', description='Text tp speech API')

@api.route('/')
@api.param('text', 'The text to synthesize.')
@api.param('provider', 'The provider to perform of the synthesis.')
class TTS(Resource):
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
    @api.response(200, 'Success')
    @api.response(500, 'Text could not be synthesized.')
    @api.produces(['application/octet-stream'])
    def get(self):
        text = request.args.get('text')
        provider = request.args.get('provider')

        if not provider:
            provider = 'google'

        synthesized_audio = None

        if text and len(text) > 0:
            synthesized_audio = self._handle_synthesis(text, provider)

        if synthesized_audio:
            return send_file(io.BytesIO(synthesized_audio), mimetype='audio/mp3')

        return abort(500, "Text could not be synthesized.")