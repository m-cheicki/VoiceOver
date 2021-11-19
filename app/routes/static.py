import re
from flask import Blueprint, send_from_directory

blueprint = Blueprint('static', __name__, url_prefix='') 

@blueprint.route('/', defaults={'path': ''}, methods=['GET'])
@blueprint.route('/<path:path>', methods=['GET'])
def serve_static_files(path):
    # check if path is a file
    is_file = re.search('^(.*)\.(\w+)$', path)
    if is_file:
        return send_from_directory('static', path)
    else:
        return send_from_directory('static', 'index.html')