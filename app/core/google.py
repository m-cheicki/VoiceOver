import os
import time
from googletrans import Translator
from gtts import gTTS

class GoogleService():
    def translate(self, text: str, language: str = "en"):
        """
        Translate the text.
        :param text: The text to translate.
        :param language: The language to translate to.
        """
        translator = Translator()
        translation = translator.translate(text, dest=language)        
        return translation.text

    def synthesize(self, text: str, language: str = "en"):
        """
        Synthesize the text.
        :param text: The text to synthesize.
        :param language: The language to synthesize to.
        """
        try:
            result = gTTS(text=text, lang=language)

            file_name = 'tts_audio_' + time.strftime('%Y%m%d%H%M%S') + '.mp3'
            file_path = os.path.join('tmp/', file_name)

            result.save(file_path)

            with open(file_path, 'rb') as audio_file:
                data = audio_file.read()

            os.remove(file_path)

            return data
            
        except Exception as e:
            print(f"Google TTS job failed : {e}")