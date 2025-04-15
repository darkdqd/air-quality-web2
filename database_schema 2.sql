-- Database schema for event management system

CREATE DATABASE IF NOT EXISTS event_management;
USE event_management;

-- Drop existing tables if they exist
DROP TABLE IF EXISTS evenement_activiter;
DROP TABLE IF EXISTS evenement_adresse;
DROP TABLE IF EXISTS evenement_tarifs;
DROP TABLE IF EXISTS evenement_date;
DROP TABLE IF EXISTS evenement;
DROP TABLE IF EXISTS organisateur;
DROP TABLE IF EXISTS lieu;
DROP TABLE IF EXISTS adresse;
DROP TABLE IF EXISTS activiter;
DROP TABLE IF EXISTS date;
DROP TABLE IF EXISTS tarifs;

-- Table: organisateur
CREATE TABLE organisateur (
    id_organisateur INT PRIMARY KEY AUTO_INCREMENT,
    telephone VARCHAR(20),
    site_web VARCHAR(255)
);

-- Table: adresse
CREATE TABLE adresse (
    id_adresse INT PRIMARY KEY AUTO_INCREMENT,
    avenue VARCHAR(255),
    ville VARCHAR(100),
    departement VARCHAR(100)
);

-- Table: activiter
CREATE TABLE activiter (
    id_activiter INT PRIMARY KEY AUTO_INCREMENT,
    nom_activiter VARCHAR(100)
);

-- Table: lieu
CREATE TABLE lieu (
    id_lieu INT PRIMARY KEY AUTO_INCREMENT,
    nom_lieu VARCHAR(255),
    proprietaire VARCHAR(255),
    commentaire TEXT
);

-- Table: evenement
CREATE TABLE evenement (
    id_evenement INT PRIMARY KEY AUTO_INCREMENT,
    titre_evenement VARCHAR(255),
    description_evenement TEXT,
    duree_evenement TIME,
    email_contact VARCHAR(255),
    langue VARCHAR(50),
    id_organisateur INT,
    id_lieu INT,
    FOREIGN KEY (id_organisateur) REFERENCES organisateur(id_organisateur),
    FOREIGN KEY (id_lieu) REFERENCES lieu(id_lieu)
);

-- Table: date
CREATE TABLE date (
    id_date INT PRIMARY KEY AUTO_INCREMENT,
    date_debut DATETIME,
    date_fin DATETIME
);

-- Table: tarifs
CREATE TABLE tarifs (
    id_tarifs INT PRIMARY KEY AUTO_INCREMENT,
    tarif VARCHAR(1000)
);

-- Junction table: evenement_date
CREATE TABLE evenement_date (
    id_evenement INT,
    id_date INT,
    PRIMARY KEY (id_evenement, id_date),
    FOREIGN KEY (id_evenement) REFERENCES evenement(id_evenement),
    FOREIGN KEY (id_date) REFERENCES date(id_date)
);

-- Junction table: evenement_tarifs
CREATE TABLE evenement_tarifs (
    id_evenement INT,
    id_tarifs INT,
    PRIMARY KEY (id_evenement, id_tarifs),
    FOREIGN KEY (id_evenement) REFERENCES evenement(id_evenement),
    FOREIGN KEY (id_tarifs) REFERENCES tarifs(id_tarifs)
);

-- Junction table: evenement_adresse
CREATE TABLE evenement_adresse (
    id_evenement INT,
    id_adresse INT,
    PRIMARY KEY (id_evenement, id_adresse),
    FOREIGN KEY (id_evenement) REFERENCES evenement(id_evenement),
    FOREIGN KEY (id_adresse) REFERENCES adresse(id_adresse)
);

-- Junction table: evenement_activiter
CREATE TABLE evenement_activiter (
    id_evenement INT,
    id_activiter INT,
    PRIMARY KEY (id_evenement, id_activiter),
    FOREIGN KEY (id_evenement) REFERENCES evenement(id_evenement),
    FOREIGN KEY (id_activiter) REFERENCES activiter(id_activiter)
);
