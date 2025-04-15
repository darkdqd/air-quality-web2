import requests
import pandas as pd
from datetime import datetime
import mysql.connector
from dotenv import load_dotenv
import os

load_dotenv()

def get_air_quality_data():
    # URL de l'API data.gouv.fr pour la qualité de l'air
    url = "https://www.data.gouv.fr/api/1/datasets/indices-qualite-air-france/"
    
    try:
        response = requests.get(url)
        data = response.json()
        return data
    except Exception as e:
        print(f"Erreur lors de la récupération des données: {e}")
        return None

def connect_to_db():
    # Try using DATABASE_URL first
    database_url = os.getenv('DATABASE_URL')
    if database_url:
        # Parse DATABASE_URL
        from urllib.parse import urlparse
        url = urlparse(database_url)
        return mysql.connector.connect(
            host=url.hostname,
            user=url.username,
            password=url.password,
            database=url.path[1:],  # Remove leading slash
            port=url.port or 3306
        )
    # Fallback to individual variables
    return mysql.connector.connect(
        host=os.getenv('DB_HOST'),
        user=os.getenv('DB_USER'),
        password=os.getenv('DB_PASSWORD'),
        database=os.getenv('DB_NAME'),
        port=int(os.getenv('DB_PORT', 3306))
    )

def update_stations(conn, stations_data):
    cursor = conn.cursor()
    for station in stations_data:
        cursor.execute("""
            INSERT INTO stations (id, name, latitude, longitude, city, region)
            VALUES (%s, %s, %s, %s, %s, %s)
            ON DUPLICATE KEY UPDATE
            name=VALUES(name), latitude=VALUES(latitude), longitude=VALUES(longitude),
            city=VALUES(city), region=VALUES(region)
        """, (station['id'], station['name'], station['latitude'], 
              station['longitude'], station['city'], station['region']))
    conn.commit()

def update_measurements(conn, measurements_data):
    cursor = conn.cursor()
    for measurement in measurements_data:
        cursor.execute("""
            INSERT INTO measurements 
            (station_id, timestamp, pm25, pm10, no2, o3, so2, co)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
        """, (measurement['station_id'], measurement['timestamp'],
              measurement['pm25'], measurement['pm10'], measurement['no2'],
              measurement['o3'], measurement['so2'], measurement['co']))
    conn.commit()

if __name__ == "__main__":
    data = get_air_quality_data()
    if data:
        conn = connect_to_db()
        try:
            update_stations(conn, data['stations'])
            update_measurements(conn, data['measurements'])
            print("Données mises à jour avec succès!")
        except Exception as e:
            print(f"Erreur lors de la mise à jour: {e}")
        finally:
            conn.close()
