-- Création de la base de données
CREATE DATABASE IF NOT EXISTS air_quality_db;
USE air_quality_db;

-- Création des utilisateurs
CREATE USER IF NOT EXISTS 'admin'@'localhost' IDENTIFIED BY 'admin_password';
CREATE USER IF NOT EXISTS 'user'@'localhost' IDENTIFIED BY 'user_password';

-- Droits admin
GRANT ALL PRIVILEGES ON air_quality_db.* TO 'admin'@'localhost';

-- Droits user (lecture seule sur certaines tables)
GRANT SELECT ON air_quality_db.* TO 'user'@'localhost';

-- Table des régions
CREATE TABLE regions (
    id INT PRIMARY KEY AUTO_INCREMENT,
    nom VARCHAR(100) NOT NULL,
    chef_lieu VARCHAR(100) NOT NULL
);

-- Table des agences
CREATE TABLE agences (
    id INT PRIMARY KEY AUTO_INCREMENT,
    nom VARCHAR(100) NOT NULL,
    adresse TEXT NOT NULL,
    region_id INT NOT NULL,
    FOREIGN KEY (region_id) REFERENCES regions(id)
);

-- Table des employés
CREATE TABLE employes (
    id INT PRIMARY KEY AUTO_INCREMENT,
    nom VARCHAR(100) NOT NULL,
    prenom VARCHAR(100) NOT NULL,
    date_naissance DATE NOT NULL,
    date_prise_poste DATE NOT NULL,
    adresse TEXT NOT NULL,
    type_employe ENUM('chef', 'technique', 'administratif') NOT NULL,
    agence_id INT NOT NULL,
    dernier_diplome VARCHAR(200),
    FOREIGN KEY (agence_id) REFERENCES agences(id)
);

-- Table des gaz
CREATE TABLE gaz (
    id INT PRIMARY KEY AUTO_INCREMENT,
    nom VARCHAR(50) NOT NULL,
    symbole VARCHAR(10) NOT NULL,
    description TEXT
);

-- Table des capteurs
CREATE TABLE capteurs (
    id INT PRIMARY KEY AUTO_INCREMENT,
    prefecture VARCHAR(100) NOT NULL,
    gaz_id INT NOT NULL,
    actif BOOLEAN DEFAULT true,
    agence_id INT NOT NULL,
    agent_technique_id INT,
    date_installation DATE NOT NULL,
    FOREIGN KEY (gaz_id) REFERENCES gaz(id),
    FOREIGN KEY (agence_id) REFERENCES agences(id),
    FOREIGN KEY (agent_technique_id) REFERENCES employes(id)
);

-- Table des relevés
CREATE TABLE releves (
    id INT PRIMARY KEY AUTO_INCREMENT,
    capteur_id INT NOT NULL,
    date_releve DATE NOT NULL,
    concentration DECIMAL(10,2) NOT NULL,
    FOREIGN KEY (capteur_id) REFERENCES capteurs(id),
    CONSTRAINT unique_releve UNIQUE (capteur_id, date_releve)
) ROW_FORMAT=COMPRESSED;

-- Table des rapports
CREATE TABLE rapports (
    id INT PRIMARY KEY AUTO_INCREMENT,
    titre VARCHAR(200) NOT NULL,
    date_creation DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    periode_debut DATE NOT NULL,
    periode_fin DATE NOT NULL,
    territoire VARCHAR(100) NOT NULL,
    contenu TEXT NOT NULL
);

-- Table de liaison rapports-employés
CREATE TABLE rapports_employes (
    rapport_id INT NOT NULL,
    employe_id INT NOT NULL,
    PRIMARY KEY (rapport_id, employe_id),
    FOREIGN KEY (rapport_id) REFERENCES rapports(id),
    FOREIGN KEY (employe_id) REFERENCES employes(id)
);

-- Triggers pour la protection des données
DELIMITER //

-- Empêcher la modification des relevés
CREATE TRIGGER protect_releves_update
BEFORE UPDATE ON releves
FOR EACH ROW
BEGIN
    SIGNAL SQLSTATE '45000' 
    SET MESSAGE_TEXT = 'La modification des relevés est interdite';
END//

-- Empêcher la modification des rapports
CREATE TRIGGER protect_rapports_update
BEFORE UPDATE ON rapports
FOR EACH ROW
BEGIN
    SIGNAL SQLSTATE '45000'
    SET MESSAGE_TEXT = 'La modification des rapports est interdite';
END//

DELIMITER ;

-- Index pour optimiser les requêtes
CREATE INDEX idx_capteurs_prefecture ON capteurs(prefecture);
CREATE INDEX idx_releves_date ON releves(date_releve);
CREATE INDEX idx_rapports_periode ON rapports(periode_debut, periode_fin);
