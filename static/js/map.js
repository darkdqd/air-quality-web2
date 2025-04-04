// Configuration de la carte
const defaultMapCenter = [46.85, 2.35]; // Centre de la France
const defaultZoom = 6;

// Styles des marqueurs selon le statut
const markerStyles = {
    online: {
        icon: L.divIcon({
            className: 'sensor-marker online',
            html: '<i class="fas fa-circle"></i>',
            iconSize: [20, 20]
        })
    },
    offline: {
        icon: L.divIcon({
            className: 'sensor-marker offline',
            html: '<i class="fas fa-circle"></i>',
            iconSize: [20, 20]
        })
    },
    warning: {
        icon: L.divIcon({
            className: 'sensor-marker warning',
            html: '<i class="fas fa-circle"></i>',
            iconSize: [20, 20]
        })
    }
};

// Initialisation de la carte
function initMap(containerId, center = defaultMapCenter, zoom = defaultZoom) {
    const map = L.map(containerId).setView(center, zoom);
    
    L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
        attribution: '© OpenStreetMap contributors',
        maxZoom: 18
    }).addTo(map);
    
    return map;
}

// Ajout d'un capteur sur la carte
function addSensorMarker(map, sensor) {
    const style = markerStyles[sensor.status.toLowerCase()] || markerStyles.offline;
    
    const marker = L.marker([sensor.lat, sensor.lng], {
        icon: style.icon
    });
    
    const popupContent = `
        <div class="sensor-popup">
            <h5>${sensor.name}</h5>
            <p>
                <strong>Status:</strong> 
                <span class="status-badge status-${sensor.status.toLowerCase()}">
                    ${sensor.status}
                </span>
            </p>
            <p><strong>Type:</strong> ${sensor.type}</p>
            <p><strong>Dernière mesure:</strong> ${sensor.last_reading} ppm</p>
            <a href="/sensor/${sensor.id}" class="btn btn-primary btn-sm">
                Voir les détails
            </a>
        </div>
    `;
    
    marker.bindPopup(popupContent);
    marker.addTo(map);
    
    return marker;
}

// Mise à jour d'un marqueur
function updateMarker(marker, sensor) {
    const style = markerStyles[sensor.status.toLowerCase()] || markerStyles.offline;
    marker.setIcon(style.icon);
    
    const popupContent = `
        <div class="sensor-popup">
            <h5>${sensor.name}</h5>
            <p>
                <strong>Status:</strong> 
                <span class="status-badge status-${sensor.status.toLowerCase()}">
                    ${sensor.status}
                </span>
            </p>
            <p><strong>Type:</strong> ${sensor.type}</p>
            <p><strong>Dernière mesure:</strong> ${sensor.last_reading} ppm</p>
            <a href="/sensor/${sensor.id}" class="btn btn-primary btn-sm">
                Voir les détails
            </a>
        </div>
    `;
    
    marker.getPopup().setContent(popupContent);
}

// Centrer la carte sur un capteur
function focusOnSensor(map, sensor, zoom = 13) {
    map.setView([sensor.lat, sensor.lng], zoom);
}

// Ajout de plusieurs capteurs
function addSensors(map, sensors) {
    const markers = {};
    sensors.forEach(sensor => {
        markers[sensor.id] = addSensorMarker(map, sensor);
    });
    return markers;
}

// Mise à jour des données des capteurs
function updateSensors(markers, sensors) {
    sensors.forEach(sensor => {
        if (markers[sensor.id]) {
            updateMarker(markers[sensor.id], sensor);
        }
    });
}
