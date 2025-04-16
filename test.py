from flask import Flask, render_template
from flask_assets import Environment, Bundle
from flask_bootstrap import Bootstrap5
from datetime import datetime

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
    return render_template('index.html', 
                         title='Surveillance Qualité de l\'Air',
                         current_time=current_time)
