import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_migrate import Migrate
from flask_assets import Environment, Bundle

db = SQLAlchemy()
login_manager = LoginManager()
migrate = Migrate()
assets = Environment()

def create_app():
    app = Flask(__name__)
    
    # Configuration
    app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'dev-key-change-in-production')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # Database configuration with fallback
    database_url = os.getenv('DATABASE_URL')
    if database_url:
        app.config['SQLALCHEMY_DATABASE_URI'] = database_url
        # Initialize database extensions
        db.init_app(app)
        migrate.init_app(app, db)

    # Initialize other extensions
    login_manager.init_app(app)
    login_manager.login_view = 'auth.login'
    assets.init_app(app)

    # Register blueprints
    from app.main import bp as main_bp
    app.register_blueprint(main_bp)

    # Only register other blueprints if database is configured
    if database_url:
        from app.auth import bp as auth_bp
        app.register_blueprint(auth_bp, url_prefix='/auth')

        from app.admin import bp as admin_bp
        app.register_blueprint(admin_bp, url_prefix='/admin')

        # User loader
        from app.models import User
        
        @login_manager.user_loader
        def load_user(id):
            return User.query.get(int(id))

        # Create database tables
        with app.app_context():
            db.create_all()
            
            # Create admin user if doesn't exist
            if not User.query.filter_by(username='admin').first():
                admin = User(
                    username='admin',
                    email='admin@example.com',
                    is_admin=True
                )
                admin.set_password('changeme123')
                db.session.add(admin)
                db.session.commit()

    return app
