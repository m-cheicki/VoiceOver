import os
import time
from rev_ai import apiclient

api_key = os.environ.get('REV_AI_API_KEY')

if not api_key:
    raise ValueError('REV_AI_API_KEY must be set')

rev_ai_stt = apiclient.RevAiAPIClient(api_key)

def transcribe(audio_file):
    """
    Transcribe the given audio file.
    :param audio_file: the path to the audio file to transcribe.
    """
    start_time = time.time()

    job = rev_ai_stt.submit_job_local_file(audio_file)
    job_details = rev_ai_stt.get_job_details(job.id)
    job_status = job_details.status.name

    while(job_status != 'TRANSCRIBED'):
        job_details = rev_ai_stt.get_job_details(job.id)
        job_status = job_details.status.name
        if job_status != 'TRANSCRIBED':
            time.sleep(0.5)

    end_time = time.time()

    result = rev_ai_stt.get_transcript_object(job.id)

    elements = result.monologues[0].elements
    only_text_el = [element for element in elements if element.type_ == 'text']
    confidences = list(map(lambda x: x.confidence, only_text_el))
    tokens = map(lambda x: x.value, elements)
    text = ''.join(tokens)

    return {
        'provider': 'Rev.ai',
        'result': text,
        'confidence': round(sum(confidences) / len(confidences), 2),
        'time': round(end_time - start_time, 2)
    }

def process_transcription(filename, return_list):
    """
    Process the transcription of the given audio file.
    :param filename: the path to the audio file to transcribe.
    :param return_list: the list to append the result to.
    """
    result = transcribe(filename)
    return_list.append(result)