import os
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    try:
        return jsonify({
            'status': 'ok',
            'message': 'Air Quality Web is running',
            'port': os.getenv('PORT', '5000')
        })
    except Exception as e:
        app.logger.error(f'Error in index route: {str(e)}')
        return jsonify({'error': str(e)}), 500

@app.errorhandler(404)
def not_found(e):
    return jsonify({'error': 'Not found'}), 404

@app.errorhandler(500)
def server_error(e):
    return jsonify({'error': 'Internal server error'}), 500

if __name__ == '__main__':
    port = int(os.getenv('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=False)
