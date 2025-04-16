from flask import render_template, jsonify
from app.main import bp

@bp.route('/')
def index():
    # Version simplifiée sans base de données
    stats = {
        'active_stations': 0,
        'today_measurements': 0,
        'average_quality': 'N/A',
        'active_alerts': 0
    }

    chart_data = {
        'labels': [],
        'datasets': [{
            'label': 'Niveau de pollution',
            'data': [],
            'borderColor': '#4a90e2',
            'tension': 0.4
        }]
    }

    stations = []

    return render_template('index.html',
                         stats=stats,
                         chart_data=chart_data,
                         stations=stations)

@bp.route('/health')
def health():
    return jsonify({
        'status': 'ok',
        'message': 'Air Quality Web is running'
    })
