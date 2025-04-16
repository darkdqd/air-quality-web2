// Fonctions utilitaires
function formatDateTime(date) {
    return new Date(date).toLocaleString('fr-FR', {
        year: 'numeric',
        month: 'long',
        day: 'numeric',
        hour: '2-digit',
        minute: '2-digit'
    });
}

function formatNumber(number, decimals = 2) {
    return new Intl.NumberFormat('fr-FR', {
        minimumFractionDigits: decimals,
        maximumFractionDigits: decimals
    }).format(number);
}

// Gestion des notifications
function showNotification(message, type = 'info') {
    const alertDiv = document.createElement('div');
    alertDiv.className = `alert alert-${type} alert-dismissible fade show`;
    alertDiv.role = 'alert';
    
    alertDiv.innerHTML = `
        ${message}
        <button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button>
    `;
    
    const container = document.querySelector('.notifications-container') || document.body;
    container.appendChild(alertDiv);
    
    // Auto-suppression après 5 secondes
    setTimeout(() => {
        alertDiv.classList.remove('show');
        setTimeout(() => alertDiv.remove(), 150);
    }, 5000);
}

// Gestion des formulaires
function handleFormSubmit(form, successCallback, errorCallback) {
    form.addEventListener('submit', async (e) => {
        e.preventDefault();
        
        const formData = new FormData(form);
        const submitButton = form.querySelector('button[type="submit"]');
        
        try {
            submitButton.disabled = true;
            submitButton.innerHTML = '<span class="spinner-border spinner-border-sm" role="status" aria-hidden="true"></span> Chargement...';
            
            const response = await fetch(form.action, {
                method: form.method,
                body: formData
            });
            
            const data = await response.json();
            
            if (response.ok) {
                showNotification(data.message || 'Opération réussie', 'success');
                if (successCallback) successCallback(data);
            } else {
                throw new Error(data.message || 'Une erreur est survenue');
            }
        } catch (error) {
            showNotification(error.message, 'danger');
            if (errorCallback) errorCallback(error);
        } finally {
            submitButton.disabled = false;
            submitButton.innerHTML = 'Envoyer';
        }
    });
}

// Gestion des tableaux de données
function initDataTable(tableId, options = {}) {
    const defaultOptions = {
        language: {
            url: '//cdn.datatables.net/plug-ins/1.10.24/i18n/French.json'
        },
        pageLength: 10,
        responsive: true,
        dom: '<"row"<"col-sm-12 col-md-6"l><"col-sm-12 col-md-6"f>>' +
             '<"row"<"col-sm-12"tr>>' +
             '<"row"<"col-sm-12 col-md-5"i><"col-sm-12 col-md-7"p>>',
        buttons: ['copy', 'excel', 'pdf']
    };
    
    return new DataTable(`#${tableId}`, { ...defaultOptions, ...options });
}

// Initialisation et mises à jour en temps réel
document.addEventListener('DOMContentLoaded', function() {
    // Initialisation des tooltips
    const tooltipTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="tooltip"]'));
    tooltipTriggerList.map(function(tooltipTriggerEl) {
        return new bootstrap.Tooltip(tooltipTriggerEl);
    });
    
    // Initialisation des popovers
    const popoverTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="popover"]'));
    popoverTriggerList.map(function(popoverTriggerEl) {
        return new bootstrap.Popover(popoverTriggerEl);
    });

    // Fonction pour mettre à jour l'heure
    function updateTime() {
        const now = new Date();
        const timeString = formatDateTime(now);
        const timeElement = document.querySelector('.stat-value.text-primary');
        if (timeElement) {
            timeElement.textContent = timeString;
        }
    }

    // Simuler des mises à jour de qualité de l'air
    function updateAirQuality() {
        const qualities = [
            { class: 'quality-good', text: 'Bonne', index: Math.floor(Math.random() * 30) + 20 },
            { class: 'quality-moderate', text: 'Modérée', index: Math.floor(Math.random() * 20) + 50 },
            { class: 'quality-poor', text: 'Mauvaise', index: Math.floor(Math.random() * 20) + 70 }
        ];

        const quality = qualities[Math.floor(Math.random() * qualities.length)];
        const indicator = document.querySelector('.quality-indicator');
        if (indicator) {
            const statValue = indicator.nextElementSibling;
            const indexText = indicator.parentElement.querySelector('.card-text');

            // Mettre à jour les classes
            indicator.className = 'quality-indicator ' + quality.class;
            statValue.textContent = quality.text;
            indexText.textContent = `Indice: ${quality.index}/100`;

            // Afficher une notification si la qualité est mauvaise
            if (quality.class === 'quality-poor') {
                showNotification('Attention : La qualité de l\'air est dégradée', 'warning');
            }
        }
    }

    // Simuler des mises à jour du nombre de stations
    function updateStations() {
        const total = 15;
        const active = Math.floor(Math.random() * 5) + 10; // Entre 10 et 15 stations actives
        const stationValue = document.querySelector('.stat-value.text-success');
        if (stationValue) {
            const stationText = stationValue.nextElementSibling;
            const previousValue = parseInt(stationValue.textContent);

            stationValue.textContent = active;
            stationText.textContent = `Sur ${total} stations totales`;

            // Notification si le nombre de stations actives diminue
            if (active < previousValue) {
                showNotification(`${previousValue - active} station(s) hors ligne`, 'danger');
            }
        }
    }

    // Démarrer les mises à jour
    setInterval(updateTime, 1000);      // Mise à jour de l'heure chaque seconde
    setInterval(updateAirQuality, 30000); // Mise à jour de la qualité toutes les 30 secondes
    setInterval(updateStations, 45000);   // Mise à jour des stations toutes les 45 secondes

    // Exécuter une première fois pour initialiser
    updateTime();
    updateAirQuality();
    updateStations();
});
