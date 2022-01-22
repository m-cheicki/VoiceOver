from flask_restx import Api

from .ttt import api as ttt_api
from .tts import api as tts_api
from .stt import api as stt_api

api = Api(
    title='Voice Over APIs',
    version='1.0',
    description='API for the Voice Over application.',
    prefix='/api',
    doc='/swagger/'
)

api.add_namespace(ttt_api, path='/translate')
api.add_namespace(tts_api, path='/synthesize')
api.add_namespace(stt_api, path='/recognize')