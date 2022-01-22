import os
import time
from rev_ai import apiclient

access_token = os.environ.get("REV_AI_API_KEY")

class RevService():
    """
    Define a service to perform speech to text from the Rev.ai API.
    """

    def __init__(self) -> None:
        self.token = access_token
        self.client = apiclient.RevAiAPIClient(access_token)

    def _save_audio(self, audio_file):
        """
        Save the audio file to disk.
        :param audio_file: The audio file to save.
        """
        file_name = 'stt_audio_' + time.strftime('%Y%m%d%H%M%S') + '.wav'
        file_path = os.path.join('tmp/', file_name)

        with open(file_path, "wb") as f:
            f.write(audio_file)

        return file_path

    def transcribe(self, audio_file, language: str = "en"):
        """
        Transcribe the audio file.
        :param audio_file: The audio file to transcribe.
        :param language: The language to transcribe in.
        """
        audio_path = self._save_audio(audio_file)

        # submtting an audio file
        job = self.client.submit_job_local_file(
            audio_path,
            delete_after_seconds=10,
            language=language
        )

        os.remove(audio_path)
        
        transcript_obj = None

        while True:
            # Obtains details of a job in json format
            job_details = self.client.get_job_details(job.id)
            status = job_details.status.name

            if status == "IN_PROGRESS":
                time.sleep(0.3)
                continue

            elif status == "FAILED":
                failure_detail = job_details.failure_detail
                raise Exception(failure_detail)

            if status == "TRANSCRIBED":
                # obtain transcript object for the job.
                transcript_obj = self.client.get_transcript_object(job.id)
                break

        transcript_text = ""
        transcript_confidence = 0
        
        if transcript_obj is not None:
            monologues = transcript_obj.monologues
            elements = monologues[0].elements

            # retrieve transcript text
            tokens = [el.value for el in elements]
            transcript_text = "".join(tokens)

            # retrieve transcript confidence
            confidences = [el.confidence for el in elements if el.type_ == "text"]
            if len(confidences) > 0:
                transcript_confidence = sum(confidences) / len(confidences)

        self.client.delete_job(job.id)

        return (transcript_text, transcript_confidence)

    async def transcribe_async(self, audio_file, language: str = "en"):
        """
        Transcribe the audio file.
        :param audio_file: The audio file to transcribe.
        :param language: The language to transcribe in.
        """
        start_time = time.time()
        try:
            transcribed_text, confidence = self.transcribe(audio_file, language)
        except Exception:
            transcribed_text, confidence = "", 0
        end_time = time.time()
        execution_time = end_time - start_time

        return transcribed_text, confidence, execution_time, 'rev'