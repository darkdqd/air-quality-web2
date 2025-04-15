-- 1. Liste de toutes les agences
SELECT a.nom, r.nom as region, a.adresse
FROM agences a
JOIN regions r ON a.region_id = r.id
ORDER BY r.nom, a.nom;

-- 2. Liste des agents techniques de l'agence de Bordeaux
SELECT e.nom, e.prenom, e.date_prise_poste
FROM employes e
JOIN agences a ON e.agence_id = a.id
WHERE a.nom LIKE '%Bordeaux%'
AND e.type_employe = 'technique'
ORDER BY e.date_prise_poste;

-- 3. Nombre total de capteurs déployés
SELECT COUNT(*) as total_capteurs,
       SUM(CASE WHEN actif = 1 THEN 1 ELSE 0 END) as capteurs_actifs
FROM capteurs;

-- 4. Liste des rapports publiés entre 2018 et 2022
SELECT r.titre, r.date_creation, r.territoire,
       GROUP_CONCAT(CONCAT(e.prenom, ' ', e.nom)) as auteurs
FROM rapports r
JOIN rapports_employes re ON r.id = re.rapport_id
JOIN employes e ON re.employe_id = e.id
WHERE YEAR(r.date_creation) BETWEEN 2018 AND 2022
GROUP BY r.id
ORDER BY r.date_creation DESC;

-- 5. Concentrations de CH₄ en Île-de-France, Bretagne et Occitanie (mai-juin 2023)
SELECT r.nom as region, 
       c.prefecture,
       AVG(rel.concentration) as concentration_moyenne
FROM releves rel
JOIN capteurs c ON rel.capteur_id = c.id
JOIN agences a ON c.agence_id = a.id
JOIN regions r ON a.region_id = r.id
JOIN gaz g ON c.gaz_id = g.id
WHERE g.symbole = 'CH₄'
AND r.nom IN ('Île-de-France', 'Bretagne', 'Occitanie')
AND rel.date_releve BETWEEN '2023-05-01' AND '2023-06-30'
GROUP BY r.nom, c.prefecture
ORDER BY r.nom, concentration_moyenne DESC;

-- 6. Liste des agents techniques responsables des capteurs de GESI
SELECT DISTINCT e.nom, e.prenom, g.nom as gaz
FROM employes e
JOIN capteurs c ON e.id = c.agent_technique_id
JOIN gaz g ON c.gaz_id = g.id
WHERE g.description LIKE '%industriel%'
ORDER BY e.nom, e.prenom;

-- 7. Titres et dates des rapports sur NH₃ (tri décroissant)
SELECT r.titre, r.date_creation
FROM rapports r
WHERE r.contenu LIKE '%NH₃%'
OR r.titre LIKE '%NH₃%'
OR r.titre LIKE '%ammoniac%'
ORDER BY r.date_creation DESC;

-- 8. Mois où la concentration de PFC a été la plus basse dans chaque région
WITH MinConcentrations AS (
    SELECT r.nom as region,
           DATE_FORMAT(rel.date_releve, '%Y-%m') as mois,
           MIN(rel.concentration) as min_concentration,
           ROW_NUMBER() OVER (PARTITION BY r.nom ORDER BY MIN(rel.concentration)) as rn
    FROM releves rel
    JOIN capteurs c ON rel.capteur_id = c.id
    JOIN agences a ON c.agence_id = a.id
    JOIN regions r ON a.region_id = r.id
    JOIN gaz g ON c.gaz_id = g.id
    WHERE g.symbole = 'PFC'
    GROUP BY r.nom, DATE_FORMAT(rel.date_releve, '%Y-%m')
)
SELECT region, mois, min_concentration
FROM MinConcentrations
WHERE rn = 1
ORDER BY region;

-- 9. Moyenne des concentrations par gaz en Île-de-France en 2020
SELECT g.symbole, g.nom,
       ROUND(AVG(rel.concentration), 2) as moyenne_concentration,
       MIN(rel.concentration) as min_concentration,
       MAX(rel.concentration) as max_concentration
FROM releves rel
JOIN capteurs c ON rel.capteur_id = c.id
JOIN agences a ON c.agence_id = a.id
JOIN regions r ON a.region_id = r.id
JOIN gaz g ON c.gaz_id = g.id
WHERE r.nom = 'Île-de-France'
AND YEAR(rel.date_releve) = 2020
GROUP BY g.id
ORDER BY moyenne_concentration DESC;

-- 10. Taux de productivité des agents administratifs de Toulouse
SELECT 
    e.nom,
    e.prenom,
    COUNT(DISTINCT re.rapport_id) as nombre_rapports,
    ROUND(COUNT(DISTINCT re.rapport_id) / 
          TIMESTAMPDIFF(MONTH, e.date_prise_poste, CURRENT_DATE), 2) as rapports_par_mois
FROM employes e
LEFT JOIN rapports_employes re ON e.id = re.employe_id
JOIN agences a ON e.agence_id = a.id
WHERE a.nom LIKE '%Toulouse%'
AND e.type_employe = 'administratif'
GROUP BY e.id
ORDER BY rapports_par_mois DESC;

-- 11. Liste des rapports contenant des relevés d'un gaz donné (paramètre dynamique)
DELIMITER //
CREATE PROCEDURE rapports_par_gaz(IN p_symbole_gaz VARCHAR(10))
BEGIN
    SELECT DISTINCT r.titre, r.date_creation, r.territoire
    FROM rapports r
    JOIN rapports_employes re ON r.id = re.rapport_id
    WHERE r.periode_debut >= (
        SELECT MIN(rel.date_releve)
        FROM releves rel
        JOIN capteurs c ON rel.capteur_id = c.id
        JOIN gaz g ON c.gaz_id = g.id
        WHERE g.symbole = p_symbole_gaz
    )
    AND r.periode_fin <= (
        SELECT MAX(rel.date_releve)
        FROM releves rel
        JOIN capteurs c ON rel.capteur_id = c.id
        JOIN gaz g ON c.gaz_id = g.id
        WHERE g.symbole = p_symbole_gaz
    )
    ORDER BY r.date_creation DESC;
END //
DELIMITER ;

-- 12. Régions où il y a plus de capteurs que d'employés d'agence
SELECT r.nom as region,
       COUNT(DISTINCT c.id) as nombre_capteurs,
       COUNT(DISTINCT e.id) as nombre_employes
FROM regions r
JOIN agences a ON r.id = a.region_id
LEFT JOIN capteurs c ON a.id = c.agence_id
LEFT JOIN employes e ON a.id = e.agence_id
GROUP BY r.id
HAVING nombre_capteurs > nombre_employes
ORDER BY (nombre_capteurs - nombre_employes) DESC;
