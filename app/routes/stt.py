import os
import time
from multiprocessing import Process, Manager
from flask import Blueprint, request, jsonify
from app.utility.stt import IbmSTT, AssemblyAiSTT, RevAiSTT

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
    audio = request.files.get('audio')

    if not audio:
        return jsonify({'error': 'No audio data provided'}), 400
    else:
        if audio.mimetype not in ['audio/wav']:
            return jsonify({'error': 'Invalid audio format'}), 400
        audio_file = audio.read()
        audio_path = __save_audio(audio_file)
    
    # Initialize manager
    manager = Manager()
    results = manager.list([])

    # IBM Watson STT
    ibm_job = Process(
        target=IbmSTT.process_transcription, 
        args=(audio_file, results))
    ibm_job.start()

    # Assembly.ai STT
    assembly_job = Process(
        target=AssemblyAiSTT.process_transcription, 
        args=(audio_file, results))
    assembly_job.start()

    # Rev.ai STT
    rev_job = Process(
        target=RevAiSTT.process_transcription,
        args=(audio_path, results))
    rev_job.start()

    # join all processes
    ibm_job.join()
    assembly_job.join()
    rev_job.join()

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
    audio = request.files.get('audio')

    if not audio:
        return jsonify({'error': 'No audio data provided'}), 400
    else:
        if audio.mimetype not in ['audio/wav']:
            return jsonify({'error': 'Invalid audio format'}), 400
        audio_file = audio.read()
        audio_path = __save_audio(audio_file)
    
    result = {}

    try:
        if provider == 'ibm':
            result = IbmSTT.transcribe(audio_file)
        elif provider == 'assembly':
            result = AssemblyAiSTT.transcribe(audio_file)
        elif provider == 'rev':
            result = RevAiSTT.transcribe(audio_path)
        else:
            return jsonify({'error': 'Invalid provider'}), 400

        os.remove(audio_path)
        return jsonify(result), 200
    except Exception as e:
        os.remove(audio_path)
        return jsonify({'error': str(e)}), 500