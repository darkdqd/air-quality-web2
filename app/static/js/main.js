// Animation des cartes statistiques
document.addEventListener('DOMContentLoaded', () => {
    const cards = document.querySelectorAll('.stat-card');
    cards.forEach((card, index) => {
        setTimeout(() => {
            card.classList.add('fade-in');
        }, index * 100);
    });
});

// Graphique de qualité de l'air
function initAirQualityChart(data) {
    const ctx = document.getElementById('airQualityChart').getContext('2d');
    new Chart(ctx, {
        type: 'line',
        data: {
            labels: data.labels,
            datasets: data.datasets
        },
        options: {
            responsive: true,
            maintainAspectRatio: false,
            plugins: {
                legend: {
                    position: 'top',
                },
                title: {
                    display: true,
                    text: 'Évolution de la qualité de l\'air'
                }
            },
            scales: {
                y: {
                    beginAtZero: true
                }
            },
            animations: {
                tension: {
                    duration: 1000,
                    easing: 'linear',
                    from: 1,
                    to: 0,
                    loop: false
                }
            }
        }
    });
}

// Carte des stations
function initMap(stations) {
    const map = L.map('map').setView([46.603354, 1.888334], 6); // Centre de la France

    L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
        attribution: '© OpenStreetMap contributors'
    }).addTo(map);

    stations.forEach(station => {
        const marker = L.marker([station.latitude, station.longitude])
            .bindPopup(`
                <h3>${station.name}</h3>
                <p>Dernière mesure: ${station.lastMeasurement} ${station.unit}</p>
                <p>Mise à jour: ${station.lastUpdate}</p>
                <a href="/station/${station.id}" class="btn btn-primary btn-sm">Détails</a>
            `)
            .addTo(map);

        // Animation du marqueur
        marker.on('add', function() {
            const el = this._icon;
            el.style.opacity = '0';
            el.style.transform = 'translateY(-20px)';
            el.style.transition = 'all 0.3s ease-out';
            
            setTimeout(() => {
                el.style.opacity = '1';
                el.style.transform = 'translateY(0)';
            }, 200);
        });
    });
}

// Gestion des formulaires avec validation
document.querySelectorAll('form').forEach(form => {
    form.addEventListener('submit', function(e) {
        if (!form.checkValidity()) {
            e.preventDefault();
            e.stopPropagation();
        }
        form.classList.add('was-validated');
    });
});

// Animation du menu de navigation
const navLinks = document.querySelectorAll('.nav-link');
navLinks.forEach(link => {
    link.addEventListener('click', function(e) {
        navLinks.forEach(l => l.classList.remove('active'));
        this.classList.add('active');
    });
});

// Gestion des messages flash
const alerts = document.querySelectorAll('.alert');
alerts.forEach(alert => {
    setTimeout(() => {
        alert.style.opacity = '0';
        setTimeout(() => alert.remove(), 300);
    }, 5000);
});
