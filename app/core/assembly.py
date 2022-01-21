import os
import time
import requests

api_key = os.environ.get('ASSEMBLYAI_API_KEY')
api_url = os.environ.get('ASSEMBLYAI_API_URL')

class AssemblyService():
    """
    Define a service to perform speech to text from the Assembly API.
    """

    def __init__(self) -> None:
        self.headers = { "authorization": api_key, "content-type": "application/json" }

    def _upload_audio(self, audio_file):
        """
        Upload the audio file to the Assembly API.
        :param audio_file: The audio file to upload.
        """
        url = api_url + "upload"

        upload_response = requests.post(
            url, 
            headers=self.headers, 
            data=audio_file
        )

        return upload_response.json()["upload_url"]

    def _submit_audio(self, audio_url):
        """
        Submit the audio file to the Assembly API.
        :param audio_url: The audio file url to submit.
        """
        url = api_url + "transcript"

        transcript_request = { "audio_url" : audio_url }
        transcript_response = requests.post(
            url, 
            json=transcript_request, 
            headers=self.headers
        )

        return transcript_response.json()["id"]

    def _poll_audio(self, audio_id):
        """
        Poll the Assembly API for the status of the audio file.
        :param audio_id: The audio file id.
        """
        url = api_url + "transcript/" + audio_id

        polling_response = requests.get(
            url, 
            headers=self.headers
        )

        return polling_response.json()

    def transcribe(self, audio_file):
        """
        Transcribe the audio file.
        :param audio_file: The audio file to transcribe.
        """
        audio_url = self._upload_audio(audio_file)
        audio_id = self._submit_audio(audio_url)

        transcript_text = ""
        transcript_confidence = 0.0

        while True:
            poll_response = self._poll_audio(audio_id)
            poll_status = poll_response["status"]

            if poll_status == "error":
                failure_detail = poll_response["error"]
                print(f"Job Failed : {failure_detail}")
                break
            elif poll_status == "completed":
                # retrieve transcript text
                transcript_text = poll_response["text"]

                # retrieve transcript confidence
                transcript_confidence = round(poll_response["confidence"], 2)
                break

            time.sleep(0.3)

        return (transcript_text, transcript_confidence)

    async def transcribe_async(self, audio_file):
        """
        Transcribe the audio file asynchronously.
        :param audio_file: The audio file to transcribe.
        """
        start_time = time.time()
        transcribed_text, confidence = self.transcribe(audio_file)
        end_time = time.time()
        execution_time = round(end_time - start_time, 2)

        return transcribed_text, confidence, execution_time, 'assembly'