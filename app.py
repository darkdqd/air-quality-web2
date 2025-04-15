from flask import Flask, render_template, request, jsonify, flash, redirect, url_for, session
import mysql.connector
import pandas as pd
from datetime import datetime
import os
import sys
import logging
from dotenv import load_dotenv
from functools import wraps

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.StreamHandler(sys.stdout)
    ]
)
logger = logging.getLogger(__name__)

load_dotenv()

app = Flask(__name__)
app.secret_key = os.getenv('SECRET_KEY', 'default-secret-key')

logger.info('Starting application...')
logger.info(f'Environment: {os.getenv("FLASK_ENV", "development")}')

# Database connection
def get_db_connection():
    try:
        database_url = os.getenv('DATABASE_URL')
        logger.info('Attempting database connection...')
        
        if database_url:
            logger.info('Using DATABASE_URL for connection')
            from urllib.parse import urlparse
            url = urlparse(database_url)
            conn = mysql.connector.connect(
                host=url.hostname,
                user=url.username,
                password=url.password,
                database=url.path[1:],
                port=url.port or 3306
            )
        else:
            logger.info('Using individual environment variables for connection')
            conn = mysql.connector.connect(
                host=os.getenv('DB_HOST'),
                user=os.getenv('DB_USER'),
                password=os.getenv('DB_PASSWORD'),
                database=os.getenv('DB_NAME'),
                port=int(os.getenv('DB_PORT', 3306))
            )
        
        logger.info('Database connection successful')
        return conn
    except Exception as e:
        logger.error(f'Database connection failed: {str(e)}')
        raise

# Routes
@app.route('/')
def index():
    try:
        logger.info('Accessing dashboard route')
        # Test database connection
        conn = get_db_connection()
        conn.close()
        logger.info('Database connection test successful')
        return render_template('dashboard.html')
    except Exception as e:
        logger.error(f'Error in dashboard route: {str(e)}')
        return jsonify({'error': str(e)}), 500

@app.route('/health')
def health():
    try:
        logger.info('Checking application health')
        # Test database connection
        conn = get_db_connection()
        conn.close()
        logger.info('Health check successful')
        return jsonify({
            'status': 'healthy',
            'database': 'connected',
            'environment': os.getenv('FLASK_ENV', 'development')
        })
    except Exception as e:
        logger.error(f'Health check failed: {str(e)}')
        return jsonify({
            'status': 'unhealthy',
            'error': str(e)
        }), 500

if __name__ == '__main__':
    port = int(os.getenv('PORT', 5000))
    app.config['SERVER_NAME'] = os.getenv('SERVER_NAME', 'air-quality-web2.up.railway.app')
    app.run(host='0.0.0.0', port=port, debug=False)

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
