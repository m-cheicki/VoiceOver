import os
from app import app

# setup tmp folder
if not os.path.exists('tmp'):
    os.mkdir('tmp')

# run the application
if __name__ == '__main__':
    app.run(debug=True)