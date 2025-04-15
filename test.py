import os
import logging
from flask import Flask, jsonify, request

# Configure logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

app = Flask(__name__)

@app.before_request
def log_request_info():
    logger.debug('Headers: %s', dict(request.headers))
    logger.debug('Environment: %s', dict(os.environ))

@app.route('/')
def index():
    try:
        logger.info('Handling request for /')
        return jsonify({
            'status': 'ok',
            'message': 'Air Quality Web is running',
            'environment': {
                'port': os.getenv('PORT', '5000'),
                'flask_env': os.getenv('FLASK_ENV'),
                'railway_domain': os.getenv('RAILWAY_PUBLIC_DOMAIN'),
                'host': request.host,
                'url': request.url
            }
        })
    except Exception as e:
        logger.exception('Error in index route')
        return jsonify({'error': str(e)}), 500

@app.errorhandler(404)
def not_found(e):
    logger.warning('404 error: %s', str(e))
    return jsonify({
        'error': 'Not found',
        'path': request.path,
        'method': request.method
    }), 404

@app.errorhandler(500)
def server_error(e):
    logger.error('500 error: %s', str(e))
    return jsonify({
        'error': 'Internal server error',
        'details': str(e)
    }), 500

if __name__ == '__main__':
    port = int(os.getenv('PORT', 5000))
    logger.info('Starting app on port %d', port)
    app.run(host='0.0.0.0', port=port, debug=True)
