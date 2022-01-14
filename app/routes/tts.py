from email.mime import audio
import os
import io
import time
from gtts import gTTS
from flask import Blueprint, request, jsonify, send_file

blueprint = Blueprint('tts', __name__, url_prefix='/api/tts')

@blueprint.route('/', methods=['GET'])
def tts():
    text = request.args.get('text')

    if not text or text == '':
        return jsonify({ 'error': 'No text provided' }), 400

    file_name = 'stt_audio_' + time.strftime('%Y%m%d%H%M%S') + '.mp3'
    file_path = os.path.join('tmp/', file_name)

    tts = gTTS(text=text, lang='en')
    tts.save(file_path)

    if not os.path.isfile(file_path):
        return jsonify({ 'error': 'Could not create the audio file' }), 500

    with open(file_path, 'rb') as f:
        audio_file = f.read()
    os.remove(file_path)

    return send_file(io.BytesIO(audio_file), mimetype='audio/mp3')