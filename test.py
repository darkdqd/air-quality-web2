import os
from flask import Flask, jsonify

app = Flask(__name__)

# Configuration for Railway
app.config['SERVER_NAME'] = os.getenv('RAILWAY_PUBLIC_DOMAIN')

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
    return jsonify({
        'status': 'running',
        'path': path,
        'port': os.getenv('PORT', '5000'),
        'domain': os.getenv('RAILWAY_PUBLIC_DOMAIN', 'localhost')
    })

if __name__ == '__main__':
    port = int(os.getenv('PORT', 5000))
    print(f'Starting app on port {port}')
    app.run(host='0.0.0.0', port=port)
