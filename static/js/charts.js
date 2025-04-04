// Configuration globale des graphiques
Chart.defaults.font.family = "'Segoe UI', 'Helvetica Neue', 'Arial', sans-serif";
Chart.defaults.font.size = 12;
Chart.defaults.plugins.tooltip.backgroundColor = 'rgba(0, 0, 0, 0.8)';
Chart.defaults.plugins.tooltip.padding = 10;
Chart.defaults.plugins.tooltip.cornerRadius = 6;
Chart.defaults.plugins.tooltip.titleFont.size = 14;

// Couleurs par défaut pour les graphiques
const chartColors = {
    primary: '#36A2EB',
    secondary: '#FF6384',
    success: '#4BC0C0',
    warning: '#FFCE56',
    danger: '#FF6384',
    gray: '#E2E8F0'
};

// Options communes pour les graphiques linéaires
const lineChartOptions = {
    responsive: true,
    maintainAspectRatio: false,
    plugins: {
        legend: {
            position: 'top',
            labels: {
                padding: 20,
                usePointStyle: true
            }
        },
        tooltip: {
            mode: 'index',
            intersect: false
        }
    },
    scales: {
        x: {
            grid: {
                display: false
            }
        },
        y: {
            beginAtZero: true,
            grid: {
                color: 'rgba(0, 0, 0, 0.05)'
            }
        }
    },
    elements: {
        line: {
            tension: 0.4
        },
        point: {
            radius: 4,
            hitRadius: 10,
            hoverRadius: 6
        }
    }
};

// Options communes pour les graphiques circulaires
const pieChartOptions = {
    responsive: true,
    maintainAspectRatio: false,
    plugins: {
        legend: {
            position: 'right',
            labels: {
                padding: 20,
                usePointStyle: true
            }
        }
    },
    cutout: '50%',
    animation: {
        animateScale: true,
        animateRotate: true
    }
};

// Options communes pour les graphiques en barres
const barChartOptions = {
    responsive: true,
    maintainAspectRatio: false,
    plugins: {
        legend: {
            position: 'top',
            labels: {
                padding: 20
            }
        }
    },
    scales: {
        x: {
            grid: {
                display: false
            }
        },
        y: {
            beginAtZero: true,
            grid: {
                color: 'rgba(0, 0, 0, 0.05)'
            }
        }
    }
};

// Fonction pour créer un graphique linéaire
function createLineChart(ctx, data, options = {}) {
    return new Chart(ctx, {
        type: 'line',
        data: data,
        options: { ...lineChartOptions, ...options }
    });
}

// Fonction pour créer un graphique circulaire
function createPieChart(ctx, data, options = {}) {
    return new Chart(ctx, {
        type: 'doughnut',
        data: data,
        options: { ...pieChartOptions, ...options }
    });
}

// Fonction pour créer un graphique en barres
function createBarChart(ctx, data, options = {}) {
    return new Chart(ctx, {
        type: 'bar',
        data: data,
        options: { ...barChartOptions, ...options }
    });
}

// Fonction pour formater les dates
function formatDate(date) {
    return new Date(date).toLocaleDateString('fr-FR', {
        year: 'numeric',
        month: 'short',
        day: 'numeric'
    });
}

// Fonction pour formater les nombres
function formatNumber(number) {
    return new Intl.NumberFormat('fr-FR').format(number);
}
