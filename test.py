import os
import sys
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return jsonify({
        'status': 'ok',
        'message': 'Air Quality Web is running',
        'python_version': sys.version,
        'env': dict(os.environ)
    })

if __name__ == '__main__':
    try:
        port = int(os.environ.get('PORT', 5000))
        print(f'Starting server on port {port}')
        print(f'Python version: {sys.version}')
        print(f'Environment variables: {dict(os.environ)}')
        app.run(host='0.0.0.0', port=port, debug=True)
    except Exception as e:
        print(f'Error starting server: {e}')
        sys.exit(1)
