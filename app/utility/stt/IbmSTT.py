import os
import time
from ibm_watson import SpeechToTextV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

api_key = os.environ.get('IBM_STT_API_KEY')
api_url = os.environ.get('IBM_STT_API_URL')

if not api_key or not api_url:
    raise ValueError('IBM_STT_API_KEY and IBM_STT_API_URL must be set')

ibm_authenticator = IAMAuthenticator(api_key)
ibm_stt = SpeechToTextV1(authenticator=ibm_authenticator)
ibm_stt.set_service_url(api_url)

def transcribe(audio):
    """
    Transcribe audio file using IBM Watson STT
    :param audio: audio file to transcribe
    """
    start_time = time.time()
    response = ibm_stt.recognize(audio, content_type='audio/wav').get_result()
    end_time = time.time()

    results = response['results']
    alternatives = [result['alternatives'][0] for result in results]
    transcripts = [alternative['transcript'] for alternative in alternatives]
    confidences = [alternative['confidence'] for alternative in alternatives]

    text = ''

    for transcript in transcripts:
        transcript = transcript.strip()
        transcript = transcript.capitalize()
        text += transcript + '. '
    
    text = text.strip()

    return {
        'provider': 'IBM',
        'result': text,
        'confidence': round(sum(confidences) / len(confidences), 2),
        'time': round(end_time - start_time, 2)
    }

def process_transcription(audio, return_list):
    """
    Process transcription results
    :param audio: audio file to transcribe
    :param return_list: list to append results to
    """
    result = transcribe(audio)
    return_list.append(result)