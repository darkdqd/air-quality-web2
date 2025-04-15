# Système de Surveillance de la Qualité de l'Air

<<<<<<< HEAD
Application web pour la centralisation des données sur la qualité de l'air en France, utilisant Railway.app pour une base de données MySQL accessible mondialement.

## Déploiement Rapide

1. Base de données (Railway):
   - Créez un compte sur [Railway.app](https://railway.app)
   - Créez un nouveau projet
   - Choisissez "Provision MySQL"
   - Copiez les informations de connexion

2. Configuration locale:
   ```bash
   # Clonez le repository
   git clone <votre-repo>
   cd air-quality-web

   # Créez le fichier .env
   cp .env.example .env
   # Complétez avec vos informations Railway
   ```

3. Démarrez l'application:
```bash
python -m venv .venv
.venv\Scripts\activate  # Windows
source .venv/bin/activate  # Linux/Mac
pip install -r requirements.txt
flask run
```

## Fonctionnalités
- Affichage en temps réel des données de qualité de l'air
- Carte interactive des stations
- Historique et tendances
- Alertes de pollution

## Structure du Projet

```
air-quality-web/
├── app/
│   ├── static/
│   └── templates/
├── database/
│   ├── schema.sql        # Création des tables
│   ├── seed.sql          # Données de test
│   └── queries.sql       # Requêtes SQL
├── docs/
│   └── database_model.md # Documentation du modèle
├── .env.example
├── requirements.txt
└── app.py
```

## Structure de la Base de Données

### Tables Principales

1. **Regions**
   - `id`: Identifiant unique
   - `nom`: Nom de la région
   - `chef_lieu`: Chef-lieu de la région

2. **Agences**
   - `id`: Identifiant unique
   - `nom`: Nom de l'agence
   - `adresse`: Adresse physique
   - `region_id`: Lien vers la région

3. **Employes**
   - `id`: Identifiant unique
   - `nom`, `prenom`: Informations personnelles
   - `date_naissance`, `date_prise_poste`: Dates importantes
   - `type_employe`: chef/technique/administratif
   - `agence_id`: Lien vers l'agence
   - `dernier_diplome`: Formation

4. **Gaz**
   - `id`: Identifiant unique
   - `nom`: Nom du gaz
   - `symbole`: Symbole chimique
   - `description`: Description détaillée

5. **Capteurs**
   - `id`: Identifiant unique
   - `prefecture`: Localisation
   - `gaz_id`: Type de gaz mesuré
   - `actif`: État du capteur
   - `agence_id`: Agence responsable
   - `agent_technique_id`: Technicien responsable
   - `date_installation`: Date de mise en service

6. **Releves**
   - `id`: Identifiant unique
   - `capteur_id`: Lien vers le capteur
   - `date_releve`: Date de la mesure
   - `concentration`: Valeur mesurée

7. **Rapports**
   - `id`: Identifiant unique
   - `titre`: Titre du rapport
   - `date_creation`: Date de création
   - `periode_debut`, `periode_fin`: Période couverte
   - `territoire`: Zone géographique concernée
   - `contenu`: Contenu du rapport

### Sécurité et Optimisation

1. **Utilisateurs et Droits**
   - Admin: Accès complet
   - User: Lecture seule

2. **Protection des Données**
   - Triggers empêchant la modification des relevés
   - Triggers protégeant les rapports

3. **Index de Performance**
   - `idx_capteurs_prefecture`: Optimisation des recherches par préfecture
   - `idx_releves_date`: Optimisation des recherches par date
   - `idx_rapports_periode`: Optimisation des recherches par période

## Fonctionnalités Principales

1. **Gestion des Agences**
   - Liste des agences par région
   - Suivi des employés par agence

2. **Surveillance des Capteurs**
   - Suivi des capteurs actifs/inactifs
   - Attribution des techniciens
   - Historique des installations

3. **Analyse des Données**
   - Calcul des moyennes de concentration
   - Suivi des tendances par région
   - Alertes sur les dépassements

4. **Gestion des Rapports**
   - Création automatisée
   - Historique par territoire
   - Attribution aux employés

## Requêtes Principales

1. **Surveillance**
   - Concentrations moyennes par région
   - Suivi mensuel des gaz spécifiques
   - État des capteurs par préfecture

2. **Administration**
   - Gestion des agents techniques
   - Suivi de la productivité
   - Attribution des responsabilités

3. **Rapports**
   - Génération par période
   - Filtrage par type de gaz
   - Analyse comparative

## Sécurité et Maintenance

1. **Protection des Données**
   - Validation des entrées
   - Historisation des modifications
   - Sauvegarde automatique

2. **Optimisation**
   - Index stratégiques
   - Compression des données
   - Nettoyage périodique

## Installation et Déploiement

1. **Prérequis**
   - MySQL 8.0+
   - Serveur Web compatible
   - Droits d'administration

2. **Installation**
   ```bash
   # Création de la base
   mysql -u root -p < database/schema.sql
   
   # Import des données initiales
   mysql -u root -p air_quality_db < database/initial_data.sql
   ```

3. **Configuration**
   - Paramétrage des accès
   - Configuration des sauvegardes
   - Mise en place des alertes

## Base de Données

### Structure
- Agences régionales
- Employés (chefs d'agence, agents techniques, agents administratifs)
- Capteurs de gaz
- Données de mesure
- Rapports

### Caractéristiques
- MySQL 8.0
- 3e forme normale (3NF)
- Contraintes d'intégrité
- Deux profils utilisateurs (admin/user)

### Jeu de Données
- 200 relevés de capteurs
- 20 employés
- 10 rapports

## Installation

1. Clonez le dépôt :
```bash
git clone https://github.com/votre-nom/air-quality-monitoring.git
cd air-quality-monitoring
```

2. Créez un environnement virtuel :
```bash
python -m venv venv
source venv/bin/activate  # Sur Windows: venv\Scripts\activate
```

3. Installez les dépendances :
```bash
pip install -r requirements.txt
```

4. Configurez MySQL :
```bash
mysql -u root -p < database/schema.sql
mysql -u root -p < database/seed.sql
```

5. Configurez les variables d'environnement :
Créez un fichier `.env` basé sur `.env.example` :
```
SECRET_KEY=votre_clé_secrète
DB_USER=votre_utilisateur_db
DB_PASSWORD=votre_mot_de_passe_db
DB_HOST=localhost
DB_NAME=air_quality_db
```

6. Lancez l'application :
```bash
python app.py
```

## Fonctionnalités

- Interface web pour la consultation des données
- Gestion des agences et employés
- Suivi des capteurs en temps réel
- Génération de rapports
- Visualisation des données par région
- Export des données au format CSV/PDF

## Requêtes SQL Disponibles

1. Liste des agences
2. Agents techniques par agence
3. Statistiques des capteurs
4. Rapports par période
5. Analyses des concentrations par région
6. Suivi de la productivité

## Sécurité

- Authentification requise
- Droits d'accès différenciés
- Protection contre l'injection SQL
- Validation des données
- Journalisation des actions

## Technologies

- Backend: Python/Flask
- Base de données: MySQL 8.0
- Frontend: Bootstrap/JavaScript
- ORM: SQLAlchemy
- Visualisation: Chart.js
