from flask import Flask
from flask_cors import CORS
from app.routes import static, translate

app = Flask(__name__)
cors = CORS(app, resources={r"/api/*": {"origins": "*"}})

# register blueprints
app.register_blueprint(translate.blueprint)
app.register_blueprint(static.blueprint)