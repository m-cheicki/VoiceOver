import os
import time
from multiprocessing import Process, Manager
from flask import Blueprint, request, jsonify
from app.utility.stt import IbmSTT, AssemblyAiSST

blueprint = Blueprint('stt', __name__, url_prefix='/api/stt')

def __save_audio(audio):
    """
    Save audio to file
    :param audio: audio data
    """
    file_name = 'audio_' + time.strftime('%Y%m%d%H%M%S') + '.wav'
    file_path = os.path.join('tmp/', file_name)
    with open(file_path, 'wb') as f:
        f.write(audio)
    return file_path

@blueprint.route('/all', methods=['POST'])
def transcribe_with_all():
    """
    Transcribe with every available STT engine
    """
    audio = request.data

    if not audio:
        return jsonify({'error': 'No audio data provided'}), 400
    else:
        audio_path = __save_audio(audio)
    
    # Initialize manager
    manager = Manager()
    results = manager.list([])

    # IBM Watson STT
    ibm_job = Process(
        target=IbmSTT.process_transcription, 
        args=(audio, results))
    ibm_job.start()

    # Assembly.ai STT
    assembly_job = Process(
        target=AssemblyAiSST.process_transcription, 
        args=(audio, results))
    assembly_job.start()

    # join all processes
    ibm_job.join()
    assembly_job.join()

    results = list(results)

    # remove audio file
    os.remove(audio_path)

    return jsonify(results)

@blueprint.route('/', methods=['POST'])
def transcribe_with_provider():
    """
    Transcribe audio with provider
    :param provider: provider name
    """
    provider = request.args.get('provider')
    audio = request.data

    if not audio:
        return jsonify({'error': 'No audio data provided'}), 400
    else:
        audio_path = __save_audio(audio)
    
    result = {}

    try:
        if provider == 'ibm':
            result = IbmSTT.transcribe(audio)
        elif provider == 'assembly':
            result = AssemblyAiSST.transcribe(audio)
        else:
            return jsonify({'error': 'Invalid provider'}), 400

        os.remove(audio_path)

        return jsonify(result), 200
    except Exception as e:
        os.remove(audio_path)

        return jsonify({'error': str(e)}), 500