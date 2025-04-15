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

// Initialisation des tooltips et popovers Bootstrap
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
});
