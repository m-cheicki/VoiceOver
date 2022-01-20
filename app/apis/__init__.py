from flask_restx import Api

api = Api(
    title='Voice Over APIs',
    version='1.0',
    description='API for the Voice Over application.',
    prefix='/swagger',
    doc='/swagger/'
)