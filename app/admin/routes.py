from flask import render_template, redirect, url_for, flash, request
from flask_login import login_required, current_user
from app.admin import bp
from app.models import User, Station, AirQualityData
from app.data_gov import DataGovAPI
from app import db

@bp.route('/')
@login_required
def dashboard():
    if not current_user.is_admin:
        flash('Accès réservé aux administrateurs', 'error')
        return redirect(url_for('main.index'))
    
    users = User.query.all()
    stations = Station.query.all()
    recent_data = AirQualityData.query.order_by(
        AirQualityData.timestamp.desc()
    ).limit(10).all()
    
    return render_template('admin/dashboard.html',
                         users=users,
                         stations=stations,
                         recent_data=recent_data)

@bp.route('/users')
@login_required
def users():
    if not current_user.is_admin:
        return redirect(url_for('main.index'))
    users = User.query.all()
    return render_template('admin/users.html', users=users)

@bp.route('/stations')
@login_required
def stations():
    if not current_user.is_admin:
        return redirect(url_for('main.index'))
    stations = Station.query.all()
    return render_template('admin/stations.html', stations=stations)

@bp.route('/refresh-data')
@login_required
def refresh_data():
    if not current_user.is_admin:
        flash('Action non autorisée', 'error')
        return redirect(url_for('main.index'))
    
    success = DataGovAPI.fetch_air_quality_data()
    if success:
        flash('Données mises à jour avec succès', 'success')
    else:
        flash('Erreur lors de la mise à jour des données', 'error')
    
    return redirect(url_for('admin.dashboard'))

@bp.route('/user/<int:id>/toggle-admin', methods=['POST'])
@login_required
def toggle_admin(id):
    if not current_user.is_admin:
        return redirect(url_for('main.index'))
    
    user = User.query.get_or_404(id)
    if user == current_user:
        flash('Vous ne pouvez pas modifier vos propres droits', 'error')
    else:
        user.is_admin = not user.is_admin
        db.session.commit()
        flash(f'Droits administrateur {"accordés" if user.is_admin else "retirés"} pour {user.username}', 'success')
    
    return redirect(url_for('admin.users'))
