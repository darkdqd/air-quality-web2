import os
import logging
from flask import Flask, jsonify

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s [%(levelname)s] %(message)s'
)

app = Flask(__name__)

@app.route('/')
def index():
    port = os.environ.get('PORT', '8000')
    logging.info(f'Handling request on port {port}')
    return jsonify({
        'status': 'ok',
        'message': 'Air Quality Web is running',
        'port': port
    })

if __name__ == '__main__':
    port = int(os.environ.get('PORT', '8000'))
    logging.info(f'Starting server on port {port}')
    app.run(host='0.0.0.0', port=port)
