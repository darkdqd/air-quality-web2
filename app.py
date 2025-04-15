from flask import Flask, render_template, jsonify
import os
import logging
from dotenv import load_dotenv

# Basic logging configuration
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Load environment variables
load_dotenv()

# Initialize Flask app
app = Flask(__name__)
app.secret_key = os.getenv('SECRET_KEY', 'default-secret-key')

logger.info('Starting application...')

# Database connection will be added later
def get_db_status():
    try:
        return {'status': 'configured'}
    except Exception as e:
        logger.error(f'Database error: {str(e)}')
        return {'status': 'error', 'message': str(e)}

# Routes
@app.route('/')
def index():
    logger.info('Accessing dashboard route')
    return render_template('dashboard.html')

@app.route('/health')
def health():
    logger.info('Health check endpoint accessed')
    return jsonify({
        'status': 'healthy',
        'version': '1.0.0',
        'database': get_db_status()
    })

if __name__ == '__main__':
    port = int(os.getenv('PORT', 5000))
    app.run(host='0.0.0.0', port=port)

# User roles and credentials
USERS = {
    'admin': {'password': 'admin123', 'role': 'admin'},
    'guest': {'password': 'guest123', 'role': 'guest'}
}

def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'user' not in session:
            flash('Please log in first')
            return redirect(url_for('login'))
        return f(*args, **kwargs)
    return decorated_function

def get_db_connection():
    return mysql.connector.connect(
        host="localhost",
        user=os.getenv('DB_USER', 'root'),
        password=os.getenv('DB_PASSWORD', ''),
        database="air_quality_db"
    )

@app.route('/')
@login_required
def index():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        
        if username in USERS and USERS[username]['password'] == password:
            session['user'] = username
            session['role'] = USERS[username]['role']
            flash(f'Welcome {username}!')
            return redirect(url_for('index'))
        else:
            flash('Invalid username or password')
    
    return render_template('login.html')

@app.route('/logout')
def logout():
    session.clear()
    flash('You have been logged out')
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True)
