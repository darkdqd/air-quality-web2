from datetime import datetime
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from app import db

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(128))
    is_admin = db.Column(db.Boolean, default=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

class AirQualityData(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    station_id = db.Column(db.String(50), nullable=False)
    station_name = db.Column(db.String(100))
    pollutant = db.Column(db.String(50), nullable=False)
    value = db.Column(db.Float, nullable=False)
    unit = db.Column(db.String(20))
    timestamp = db.Column(db.DateTime, nullable=False)
    latitude = db.Column(db.Float)
    longitude = db.Column(db.Float)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    @staticmethod
    def get_latest_readings():
        return db.session.query(
            AirQualityData.station_name,
            db.func.max(AirQualityData.value).label('max_value'),
            db.func.avg(AirQualityData.value).label('avg_value'),
            AirQualityData.pollutant,
            AirQualityData.unit
        ).group_by(
            AirQualityData.station_name,
            AirQualityData.pollutant,
            AirQualityData.unit
        ).order_by(
            AirQualityData.station_name
        ).all()

    @staticmethod
    def get_station_history(station_name, days=7):
        cutoff = datetime.utcnow() - timedelta(days=days)
        return AirQualityData.query.filter(
            AirQualityData.station_name == station_name,
            AirQualityData.timestamp >= cutoff
        ).order_by(AirQualityData.timestamp.asc()).all()

class Station(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    station_id = db.Column(db.String(50), unique=True, nullable=False)
    name = db.Column(db.String(100), nullable=False)
    latitude = db.Column(db.Float, nullable=False)
    longitude = db.Column(db.Float, nullable=False)
    city = db.Column(db.String(100))
    region = db.Column(db.String(100))
    last_updated = db.Column(db.DateTime)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    @property
    def latest_readings(self):
        return AirQualityData.query.filter_by(
            station_id=self.station_id
        ).order_by(
            AirQualityData.timestamp.desc()
        ).limit(5).all()
