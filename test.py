import os
import logging
from flask import Flask, jsonify, request

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

app = Flask(__name__)

@app.route('/')
def index():
    logger.debug(f'Index endpoint called from {request.remote_addr}')
    logger.debug(f'Headers: {dict(request.headers)}')
    return jsonify({
        'status': 'ok',
        'message': 'Air Quality Web is running',
        'remote_addr': request.remote_addr
    })

if __name__ == '__main__':
    port = int(os.getenv('PORT', 5000))
    logger.info(f'Starting app on port {port}')
    logger.info(f'Environment: {os.environ}')
    app.run(host='0.0.0.0', port=port, debug=True)
