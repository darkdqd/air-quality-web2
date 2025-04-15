import os
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    port = os.getenv('PORT', '5000')
    return f'Hello from port {port}!'

@app.route('/health')
def health():
    return {'status': 'ok'}

if __name__ == '__main__':
    port = int(os.getenv('PORT', 5000))
    print(f'Starting app on port {port}')
    app.run(host='0.0.0.0', port=port)
