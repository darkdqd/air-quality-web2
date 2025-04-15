-- Schema for Air Quality Database
CREATE TABLE IF NOT EXISTS stations (
    id VARCHAR(50) PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    latitude DECIMAL(10, 8) NOT NULL,
    longitude DECIMAL(11, 8) NOT NULL,
    city VARCHAR(100),
    region VARCHAR(100),
    last_update TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS measurements (
    id BIGINT AUTO_INCREMENT PRIMARY KEY,
    station_id VARCHAR(50),
    timestamp DATETIME NOT NULL,
    pm25 DECIMAL(8, 2),
    pm10 DECIMAL(8, 2),
    no2 DECIMAL(8, 2),
    o3 DECIMAL(8, 2),
    so2 DECIMAL(8, 2),
    co DECIMAL(8, 2),
    temperature DECIMAL(5, 2),
    humidity DECIMAL(5, 2),
    pressure DECIMAL(7, 2),
    FOREIGN KEY (station_id) REFERENCES stations(id),
    INDEX idx_station_timestamp (station_id, timestamp)
);

CREATE TABLE IF NOT EXISTS daily_averages (
    id BIGINT AUTO_INCREMENT PRIMARY KEY,
    station_id VARCHAR(50),
    date DATE NOT NULL,
    avg_pm25 DECIMAL(8, 2),
    avg_pm10 DECIMAL(8, 2),
    avg_no2 DECIMAL(8, 2),
    avg_o3 DECIMAL(8, 2),
    avg_so2 DECIMAL(8, 2),
    avg_co DECIMAL(8, 2),
    FOREIGN KEY (station_id) REFERENCES stations(id),
    UNIQUE INDEX idx_station_date (station_id, date)
);

CREATE TABLE IF NOT EXISTS alerts (
    id BIGINT AUTO_INCREMENT PRIMARY KEY,
    station_id VARCHAR(50),
    timestamp DATETIME NOT NULL,
    pollutant VARCHAR(10) NOT NULL,
    level VARCHAR(20) NOT NULL,
    message TEXT,
    resolved_at DATETIME,
    FOREIGN KEY (station_id) REFERENCES stations(id),
    INDEX idx_active_alerts (station_id, resolved_at)
);
