import os
import logging
from flask import Flask, jsonify

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = Flask(__name__)

# Configure server name
app.config['SERVER_NAME'] = os.getenv('SERVER_NAME', 'projet-bdd.railway.app')

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
    try:
        return jsonify({
            'status': 'ok',
            'message': 'Air Quality Web is running',
            'path': path,
            'server_name': app.config['SERVER_NAME']
        })
    except Exception as e:
        logger.exception('Error in route')
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    port = int(os.getenv('PORT', 5000))
    logger.info('Starting app on port %d with server name %s', 
                port, app.config['SERVER_NAME'])
    app.run(host='0.0.0.0', port=port)
