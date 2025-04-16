import requests
from datetime import datetime
from app.models import AirQualityData, Station
from app import db

class DataGovAPI:
    BASE_URL = "https://www.data.gouv.fr/api/1"
    DATASET_ID = "qualite-de-l-air-france"  # À remplacer par l'ID réel du dataset

    @staticmethod
    def fetch_air_quality_data():
        """Récupère les données de qualité de l'air depuis data.gouv.fr"""
        try:
            response = requests.get(f"{DataGovAPI.BASE_URL}/datasets/{DataGovAPI.DATASET_ID}/")
            if response.status_code == 200:
                data = response.json()
                return DataGovAPI._process_air_quality_data(data)
            else:
                print(f"Erreur lors de la récupération des données: {response.status_code}")
                return None
        except Exception as e:
            print(f"Erreur lors de la requête API: {str(e)}")
            return None

    @staticmethod
    def _process_air_quality_data(data):
        """Traite les données brutes et les enregistre dans la base de données"""
        try:
            for record in data.get('records', []):
                # Extraction des données
                fields = record.get('fields', {})
                
                # Création ou mise à jour de la station
                station = Station.query.filter_by(station_id=fields.get('code_station')).first()
                if not station:
                    station = Station(
                        station_id=fields.get('code_station'),
                        name=fields.get('nom_station'),
                        latitude=fields.get('latitude'),
                        longitude=fields.get('longitude'),
                        city=fields.get('commune'),
                        region=fields.get('region')
                    )
                    db.session.add(station)

                # Création de la mesure
                measurement = AirQualityData(
                    station_id=fields.get('code_station'),
                    station_name=fields.get('nom_station'),
                    pollutant=fields.get('polluant'),
                    value=fields.get('valeur'),
                    unit=fields.get('unite'),
                    timestamp=datetime.fromisoformat(fields.get('date_mesure')),
                    latitude=fields.get('latitude'),
                    longitude=fields.get('longitude')
                )
                db.session.add(measurement)

            db.session.commit()
            return True
        except Exception as e:
            db.session.rollback()
            print(f"Erreur lors du traitement des données: {str(e)}")
            return False

    @staticmethod
    def get_station_list():
        """Récupère la liste des stations de mesure"""
        try:
            response = requests.get(f"{DataGovAPI.BASE_URL}/datasets/{DataGovAPI.DATASET_ID}/resources/")
            if response.status_code == 200:
                data = response.json()
                stations = []
                for resource in data:
                    if resource.get('format') == 'csv' and 'stations' in resource.get('title', '').lower():
                        stations_response = requests.get(resource['url'])
                        if stations_response.status_code == 200:
                            # Traitement du CSV des stations
                            # À implémenter selon le format exact du fichier
                            pass
                return stations
            return None
        except Exception as e:
            print(f"Erreur lors de la récupération des stations: {str(e)}")
            return None
