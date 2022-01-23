from multiprocessing import Process, Manager
import asyncio
import time
from flask import request, abort
from flask_restx import Resource, Namespace, fields, reqparse
from werkzeug.datastructures import FileStorage

from app.core.ibm import IBMService
from app.core.assembly import AssemblyService
from app.core.rev import RevService

api = Namespace('STT', description='Speech to text API')

audio_parser = reqparse.RequestParser()
audio_parser.add_argument('audio/wav', location='files', type=FileStorage, required=True)

transcriptionResult = api.model(
    'TranscriptionResult', {
        'transcription': fields.String(description='The transcription of the audio.'),
        'provider': fields.String(description='The provider of the transcription.'),
        'confidence': fields.Float(description='The confidence of the transcription.'),
        'time': fields.Float(description='Execution time of the transcription.')
    }
)


@api.route('/withOne')
class STTSingle(Resource):
    def _handle_single_transcription(self, audio_file: bytes, provider: str, language: str = 'en'):
        """
        Handles the transcription of audio file.
        :param audio_file: The audio file to be transcribed.
        :param provider: The transcription provider to use.
        :param language: The language of the transcription.
        """
        transcription = ""
        confidence = 0.0

        start_time = time.time()

        try:
            if provider == 'ibm':
                ibm_service = IBMService()
                transcription, confidence = ibm_service.transcribe(audio_file, language)
            elif provider == 'assembly':
                assembly_service = AssemblyService()
                transcription, confidence = assembly_service.transcribe(audio_file)
            elif provider == 'rev':
                rev_service = RevService()
                transcription, confidence = rev_service.transcribe(audio_file)
        except Exception as e:
            api.logger.error(f"Error while transcribing audio file with provider {provider} : {e}")

        end_time = time.time()
        execution_time = round(end_time - start_time)

        return transcription, confidence, execution_time

    @api.doc(description='Transcribe audio file.')
    @api.expect(audio_parser)
    @api.param('language', 'The language of the audio file.')
    @api.param('provider', 'The provider to perform of the transcription.')
    @api.marshal_with(transcriptionResult)
    def post(self):
        """
        Transcribe audio file.
        """
        args = audio_parser.parse_args()
        provider = request.args.get('provider')
        language = request.args.get('language')
        audio = args.get('audio/wav')

        if not audio:
            return abort(400, "No audio file provided.")
        else:
            if audio.mimetype not in ['audio/wav']:
                return abort(400, "Invalid audio file provided.")
            audio_file = audio.read()

        if not provider:
            provider = 'ibm'

        if not language:
            language = 'en'

        transcription, confidence, exec_time = self._handle_single_transcription(audio_file, provider, language)

        return {
            'transcription': transcription,
            'provider': provider,
            'confidence': confidence,
            'time': exec_time
        }

@api.route('/withAll')
class STTAll(Resource):
    async def _handle_all_transcription_async(self, audio_file: bytes):
        """
        Handles the transcription of audio file.
        :param audio_file: The audio file to be transcribed.
        """
        results = []

        try:
            ibm_service = IBMService()
            ibm_task = asyncio.create_task(ibm_service.transcribe_async(audio_file))

            assembly_service = AssemblyService()
            assembly_task = asyncio.create_task(assembly_service.transcribe_async(audio_file))

            rev_service = RevService()
            rev_task = asyncio.create_task(rev_service.transcribe_async(audio_file))

            tasks = [ibm_task, assembly_task, rev_task]
            tmp = await asyncio.gather(*tasks)
            results = [{ 'transcription': x[0], 'confidence': x[1], 'time': x[2], 'provider': x[3] } for x in tmp]

        except Exception as e:
            api.logger.error(f"Error while transcribing audio file : {e}")

        return results

    def _handle_all_transcription_parallel(self, audio_file: bytes):
        """
        Handles the transcription of audio file.
        :param audio_file: The audio file to be transcribed.
        """
        results = []
        language = 'en'

        process_manager = Manager()
        process_result = process_manager.list([])

        try:
            ibm_service = IBMService()
            ibm_task = Process(
                target=ibm_service.transcribe_parallel, 
                args=(audio_file, language, process_result)
            )

            assembly_service = AssemblyService()
            assembly_task = Process(
                target=assembly_service.transcribe_parallel, 
                args=(audio_file, process_result)
            )

            rev_service = RevService()
            rev_task = Process(
                target=rev_service.transcribe_parallel, 
                args=(audio_file, language, process_result)
            )

            tasks = [ibm_task, assembly_task, rev_task]

            for task in tasks:
                task.start()

            for task in tasks:
                task.join()

            results = list(process_result)

        except Exception as e:
            api.logger.error(f"Error while transcribing audio file : {e}")

        return results

    @api.doc(description='Transcribe audio file.')
    @api.expect(audio_parser)
    @api.marshal_list_with(transcriptionResult)
    def post(self):
        """
        Transcribe audio file.
        """
        args = audio_parser.parse_args()
        audio = args.get('audio/wav')

        if not audio:
            return abort(400, "No audio file provided.")
        else:
            if audio.mimetype not in ['audio/wav']:
                return abort(400, "Invalid audio file provided.")
            audio_file = audio.read()

        try:
            loop = asyncio.get_running_loop()
        except RuntimeError:
            loop = None

        if loop and loop.is_running():
            results = self._handle_all_transcription_parallel(audio_file)
        else:
            results = asyncio.run(self._handle_all_transcription_async(audio_file))

        return results
