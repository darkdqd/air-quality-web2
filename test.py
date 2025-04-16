import os
import logging
from flask import Flask, jsonify

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

app = Flask(__name__)

@app.route('/')
def index():
    logger.debug('Index endpoint called')
    return jsonify({
        'status': 'ok',
        'message': 'Air Quality Web is running'
    })

if __name__ == '__main__':
    port = int(os.getenv('PORT', 5000))
    logger.info(f'Starting app on port {port}')
    app.run(host='0.0.0.0', port=port)
