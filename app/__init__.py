import re
import mimetypes
import logging
from flask import Flask
from flask_cors import CORS
from dotenv import load_dotenv

# Load correct mimetypes for js files
mimetypes.add_type('application/javascript', '.js')

# Load environment variables
dotenv_path = '.env'
load_dotenv(dotenv_path)

# Create app
app = Flask(__name__, static_folder='static')
cors = CORS(app, resources={r"/api/*": {"origins": "*"}})

# Configure logging
gunicorn_logger = logging.getLogger('gunicorn.error')
app.logger.handlers.extend(gunicorn_logger.handlers)
app.logger.setLevel(gunicorn_logger.level)

# Register APIs
from .apis import api
api.init_app(app)

# Serve static files
@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def serve_static_files(path: str):
    """
    Serves static files.
    :param path: The path to the file.
    """
    # check if path is a file
    is_file = re.search('^(.*)\.(\w+)$', path)

    if is_file:
        return app.send_static_file(path)
    else:
        return app.send_static_file('index.html')

@app.errorhandler(413)
def request_entity_too_large(error):
    return 'File Too Large', 413
