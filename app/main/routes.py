from flask import render_template, jsonify, current_app
from flask_login import login_required, current_user
from app.main import bp
from app.models import AirQualityData, Station
from app.data_gov import DataGovAPI

@bp.route('/')
def index():
    # Statistiques pour le dashboard
    stats = {
        'active_stations': Station.query.count(),
        'today_measurements': AirQualityData.query.filter(
            AirQualityData.timestamp >= datetime.utcnow().date()
        ).count(),
        'average_quality': '6.8',  # À calculer selon vos critères
        'active_alerts': 2  # À implémenter selon vos critères
    }

    # Données pour le graphique
    latest_readings = AirQualityData.get_latest_readings()
    chart_data = {
        'labels': [r.station_name for r in latest_readings],
        'datasets': [{
            'label': 'Niveau de pollution',
            'data': [r.max_value for r in latest_readings],
            'borderColor': '#4a90e2',
            'tension': 0.4
        }]
    }

    # Données des stations pour la carte
    stations = [{
        'id': s.id,
        'name': s.name,
        'latitude': s.latitude,
        'longitude': s.longitude,
        'lastMeasurement': s.latest_readings[0].value if s.latest_readings else 'N/A',
        'unit': s.latest_readings[0].unit if s.latest_readings else '',
        'lastUpdate': s.last_updated.strftime('%d/%m/%Y %H:%M') if s.last_updated else 'N/A'
    } for s in Station.query.all()]

    return render_template('index.html',
                         stats=stats,
                         chart_data=chart_data,
                         stations=stations)

@bp.route('/map')
def map():
    stations = Station.query.all()
    return render_template('map.html', stations=stations)

@bp.route('/stats')
@login_required
def stats():
    return render_template('stats.html')

@bp.route('/station/<int:station_id>')
def station_detail(station_id):
    station = Station.query.get_or_404(station_id)
    history = AirQualityData.get_station_history(station.name)
    return render_template('station_detail.html',
                         station=station,
                         history=history)

@bp.route('/api/refresh-data')
@login_required
def refresh_data():
    """Endpoint pour rafraîchir les données depuis data.gouv.fr"""
    if current_user.is_admin:
        success = DataGovAPI.fetch_air_quality_data()
        return jsonify({'success': success})
    return jsonify({'error': 'Unauthorized'}), 403
