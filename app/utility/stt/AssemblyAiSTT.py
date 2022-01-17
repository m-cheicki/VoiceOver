import os
import time
import requests

# setting up assembly.ai speech to text
api_key = os.environ.get('ASSEMBLYAI_API_KEY')
api_url = os.environ.get('ASSEMBLYAI_API_URL')

if not api_key or not api_url:
    raise ValueError('ASSEMBLYAI_API_KEY and ASSEMBLYAI_API_URL must be set')

def transcribe(audio):
    """
    Transcribe audio file using Assembly.ai Speech to Text
    :param audio: audio file to transcribe
    """
    upload_url = api_url + 'upload'
    transcript_url = api_url + 'transcript'

    headers = {
        "authorization": api_key, 
        "content-type": "application/json"
    }

    start_time = time.time()

    upload_response = requests.post(
        upload_url, 
        headers=headers, 
        data=audio
    )

    audio_url = upload_response.json()["upload_url"]

    transcript_request = {'audio_url': audio_url}

    transcript_response = requests.post(
        transcript_url, 
        json=transcript_request, 
        headers=headers
    )

    audio_id = transcript_response.json()["id"]

    polling_response = requests.get(
        transcript_url + '/' + audio_id, 
        headers=headers)
    polling_status = polling_response.json()['status']

    while polling_status == 'processing':
        time.sleep(0.3)
        polling_response = requests.get(
            transcript_url + '/' + audio_id, 
            headers=headers)
        polling_status = polling_response.json()['status']

    end_time = time.time()
    text = ''
    confidence = 0

    if polling_status == 'completed':
        text = polling_response.json()['text']
        words = polling_response.json()['words']
        confidences = list(map(lambda x: x['confidence'], words))

        if confidences and len(confidences) > 0:
            confidence = sum(confidences) / len(confidences)
    else:
        print('Assembly.ai job failed with status: ' + polling_status)

    return {
        'provider': 'Assembly.ai',
        'result': text,
        'confidence': round(confidence, 2),
        'time': round(end_time - start_time, 2)
    }

def process_transcription(audio, return_list):
    """
    Process the transcription of a file
    :param audio: audio file to transcribe
    :param return_list: list to append the result to
    """
    result = transcribe(audio)
    return_list.append(result)