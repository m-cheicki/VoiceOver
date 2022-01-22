import os
import time
from datetime import date
from ibm_watson import SpeechToTextV1, LanguageTranslatorV3, TextToSpeechV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

stt_api_key = os.environ.get('IBM_STT_API_KEY')
stt_api_url = os.environ.get('IBM_STT_API_URL')

ttt_api_key = os.environ.get('IBM_TRANSLATION_API_KEY')
ttt_api_url = os.environ.get('IBM_TRANSLATION_API_URL')

tts_api_key = os.environ.get('IBM_TTS_API_KEY')
tts_api_url = os.environ.get('IBM_TTS_API_URL')

class IBMService():
    """
    Define a service to perform speech to text and text translation from the IBM Watson API.
    """

    def __init__(self) -> None:
        self.stt_service = None
        self.ttt_service = None
        self.tts_service = None

    def _init_stt_service(self):
        """
        Initialize the STT service.
        """
        if self.stt_service is None:
            authenticator = IAMAuthenticator(stt_api_key)
            self.stt_service = SpeechToTextV1(authenticator=authenticator)
            self.stt_service.set_service_url(stt_api_url)

    def _init_ttt_service(self):
        """
        Initialize the LanguageTranslator service.
        """
        if self.ttt_service is None:
            version = date.today().strftime('%Y-%m-%d')
            authenticator = IAMAuthenticator(ttt_api_key)
            self.ttt_service = LanguageTranslatorV3(version=version, authenticator=authenticator)
            self.ttt_service.set_service_url(ttt_api_url)

    def _init_tts_service(self):
        """
        Initialize the TextToSpeech service.
        """
        if self.tts_service is None:
            authenticator = IAMAuthenticator(tts_api_key)
            self.tts_service = TextToSpeechV1(authenticator=authenticator)
            self.tts_service.set_service_url(tts_api_url)

    def _get_stt_model(self, language: str ='en') -> str:
        """
        Get the STT model for the language.
        :param language: The language.
        """
        model = None

        all_models = self.stt_service.list_models().get_result()["models"]
        filtered_models = [model for model in all_models if model["language"].startswith(language)]
        filtered_models = [model for model in filtered_models if "broadband" in model["description"]]

        if len(filtered_models) > 0:
            model = filtered_models[0]

        return model["name"]

    def _get_tts_model(self, language: str ='en') -> str:
        """
        Get the TTS model for the language.
        :param language: The language.
        """
        model = None

        all_models = self.tts_service.list_voices().get_result()["voices"]
        filtered_models = [model for model in all_models if model["language"].startswith(language)]

        if len(filtered_models) > 0:
            model = filtered_models[0]

        return model["name"]

    def transcribe(self, audio_file: bytes, language: str ='en'):
        """
        Transcribe the audio file.
        :param audio_file: The audio file.
        :param language: The language of the audio file.
        """
        self._init_stt_service()

        transcript_text = ""
        transcript_confidence = 0.0
        transcript_model = self._get_stt_model(language)

        response = self.stt_service.recognize(audio_file, content_type='audio/wav', model=transcript_model).get_result()

        results = response['results']
        alternatives = [result['alternatives'][0] for result in results]
        transcripts = [alternative['transcript'] for alternative in alternatives]
        confidences = [alternative['confidence'] for alternative in alternatives]

        for transcript in transcripts:
            transcript = transcript.strip()
            transcript = transcript.capitalize()
            transcript_text += transcript + '. '

        transcript_text = transcript_text.strip()

        if len(confidences) > 0:
            transcript_confidence = sum(confidences) / len(confidences)

        return (transcript_text, transcript_confidence)

    async def transcribe_async(self, audio_file: bytes, language: str ='en'):
        """
        Transcribe the audio file asynchronously.
        :param audio_file: The audio file.
        :param language: The language of the audio file.
        """
        start_time = time.time()
        try:
            transcribed_text, confidence = self.transcribe(audio_file, language)
        except Exception:
            transcribed_text, confidence = '', 0.0
        end_time = time.time()
        execution_time = end_time - start_time

        return transcribed_text, confidence, execution_time, 'ibm'

    def translate(self, text: str, language: str ='en') -> str:
        """
        Translate the text.
        :param text: The text to translate.
        :param language: The language to translate to.
        """
        self._init_ttt_service()

        translated_text = ""

        result = self.ttt_service.translate(
            text,
            target=language
        ).get_result()

        translations = result["translations"]

        if len(translations) > 0:
            translated_text = translations[0]["translation"]

        return translated_text

    async def translate_async(self, text: str, language: str ='en') -> str:
        """
        Translate the text asynchronously.
        :param text: The text to translate.
        :param language: The language to translate to.
        """
        return self.translate(text, language)

    def synthesize(self, text: str, language: str = 'en') -> bytes:
        """
        Synthesize the text.
        :param text: The text to synthesize.
        :param language: The language of the text.
        """
        self._init_tts_service()

        tts_model = self._get_tts_model(language)

        result = self.tts_service.synthesize(
            text,
            accept='audio/mp3',
            voice=tts_model
        ).get_result()

        return result.content

    async def synthesize_async(self, text: str) -> bytes:
        """
        Synthesize the text asynchronously.
        :param text: The text to synthesize.
        :param language: The language of the text.
        """
        return self.synthesize(text)