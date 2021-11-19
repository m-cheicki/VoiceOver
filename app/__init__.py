from flask import Flask
from flask_cors import CORS
from dotenv import load_dotenv

dotenv_path = '.env'
load_dotenv(dotenv_path)

app = Flask(__name__)
cors = CORS(app, resources={r"/api/*": {"origins": "*"}})

# register blueprints
from app.routes import static, translate
app.register_blueprint(translate.blueprint)
app.register_blueprint(static.blueprint)