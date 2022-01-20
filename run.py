import os
from app import app

# Setup tmp folder
if not os.path.exists('tmp'):
    os.mkdir('tmp')

# Run the application
if __name__ == '__main__':
    app.run(debug=True)