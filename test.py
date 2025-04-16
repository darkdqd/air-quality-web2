import os
import logging
from datetime import datetime
from flask import Flask, render_template, jsonify
from flask_assets import Environment, Bundle
from flask_bootstrap import Bootstrap5

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s [%(levelname)s] %(message)s'
)

app = Flask(__name__)
bootstrap = Bootstrap5(app)

# Configure Flask-Assets
assets = Environment(app)
assets.url = app.static_url_path
css = Bundle('css/style.css', output='gen/packed.css')
assets.register('css_all', css)

@app.route('/')
def index():
    current_time = datetime.now().strftime('%d/%m/%Y %H:%M:%S')
    logging.info('Rendering index page')
    return render_template('index.html',
                         title='Surveillance Qualité de l\'Air',
                         current_time=current_time)

@app.route('/health')
def health():
    logging.info('Health check request received')
    return jsonify({
        'status': 'ok',
        'timestamp': datetime.now().isoformat(),
        'environment': os.environ.get('FLASK_ENV', 'development')
    })

if __name__ == '__main__':
    port = int(os.environ.get('PORT', '8000'))
    logging.info(f'Starting server on port {port}')
    app.run(host='0.0.0.0', port=port)
