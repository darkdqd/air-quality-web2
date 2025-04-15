# Guide Simple pour Commiter sur GitHub Desktop

## 1. Préparation

1. Ouvrez GitHub Desktop
2. Vérifiez que vous êtes sur le projet `air_quality_web`
3. Vérifiez que vous êtes sur la branche 'main'

## 2. Liste des Fichiers à Commiter

Voici exactement quels fichiers commiter :

✅ COMMITER ces fichiers :
- `app.py`
- `database/schema.sql`
- `database/queries.sql`
- Tout le dossier `static`
- Tout le dossier `templates`
- `requirements.txt`
- `README.md`
- `.gitignore`

❌ NE PAS COMMITER ces fichiers :
- `.env` (contient vos mots de passe)
- Tous les fichiers `.db`
- Le dossier `__pycache__`
- Le dossier `venv`

## 3. Comment Commiter

1. Dans GitHub Desktop :
   - Colonne de gauche : vous voyez tous les fichiers modifiés
   - Les fichiers en jaune = modifiés
   - Les fichiers en vert = nouveaux

2. Pour chaque fichier :
   - Si le fichier est dans la liste '✅ COMMITER' : laissez-le coché
   - Si le fichier est dans la liste '❌ NE PAS COMMITER' : décochez-le

3. Écrivez votre message de commit :
   ```
   Mise à jour : [ce que vous avez changé]
   ```

4. Cliquez sur 'Commit to main'

5. Cliquez sur 'Push origin'

## 4. Vérification

1. Allez sur GitHub.com
2. Ouvrez votre projet `air_quality_web`
3. Vérifiez que :
   - Vos fichiers Python sont là
   - Les dossiers database, static, templates sont là
   - Le fichier `.env` n'est PAS là

## 5. Partager votre Projet

### Obtenir le Lien de Partage
1. Allez sur [github.com](https://github.com)
2. Connectez-vous à votre compte
3. Cliquez sur votre profil (en haut à droite)
4. Sélectionnez 'Your repositories'
5. Cliquez sur `air_quality_web`
6. Copiez l'URL dans la barre d'adresse
   - Elle ressemble à : `https://github.com/votre-nom/air_quality_web`

### Partager avec d'Autres
1. Envoyez ce lien aux personnes concernées
2. Elles pourront :
   - Voir tout votre code
   - Télécharger le projet
   - Cloner le projet si elles ont un compte GitHub

### Rendre le Projet Public/Privé
1. Sur la page de votre projet
2. Cliquez sur 'Settings'
3. Descendez jusqu'à 'Danger Zone'
4. Trouvez 'Change repository visibility'
5. Choisissez 'Public' ou 'Private'

## 6. En Cas de Problème

- Si vous avez commis une erreur : demandez de l'aide
- Ne supprimez rien sans être sûr
- En cas de doute, demandez avant de commiter

### Installation de GitHub Desktop
1. Allez sur [desktop.github.com](https://desktop.github.com/)
2. Cliquez sur 'Download for Windows'
3. Exécutez le fichier téléchargé
4. Lancez GitHub Desktop
5. Connectez-vous avec votre compte GitHub

### Configuration de Base
1. Dans GitHub Desktop :
   - File > Options > Accounts
   - Connectez votre compte GitHub
   - Dans l'onglet Git :
     - Nom : Votre nom
     - Email : Votre email GitHub

## 2. Création du Projet

### Sur GitHub.com
1. Connectez-vous sur [github.com](https://github.com)
2. Cliquez sur le '+' en haut à droite
3. 'New repository'
4. Remplissez :
   - Repository name : `air-quality-web`
   - Description : `Application web de surveillance de la qualité de l'air`
   - Public
   - Initialize with README
   - Add .gitignore: Python
5. 'Create repository'

### Sur Votre Ordinateur
1. GitHub Desktop > File > Clone repository
2. URL : votre dépôt GitHub
3. Local path : `C:\Users\[VotreNom]\CascadeProjects\splitwise\air_quality_web`
4. 'Clone'

## 3. Structure du Projet

### Organisation des Dossiers
```
air_quality_web/
├── database/           # Scripts SQL
│   ├── schema.sql     # Structure BD
│   └── queries.sql    # Requêtes
├── static/            # Fichiers statiques
│   ├── css/          # Styles
│   └── js/           # JavaScript
├── templates/         # Templates Flask
│   ├── base.html
│   └── dashboard.html
├── .env              # Configuration
├── .gitignore        # Exclusions
├── app.py            # Application
└── requirements.txt  # Dépendances
```

### Fichiers Essentiels

1. `.gitignore` :
```
# Python
__pycache__/
*.pyc
venv/
.env

# Base de données
*.db
*.sqlite3

# IDE
.vscode/
.idea/
```

2. `requirements.txt` :
```
Flask==3.0.0
SQLAlchemy==2.0.0
python-dotenv==1.0.0
```

## 4. Utilisation Quotidienne

### Faire des Modifications
1. Ouvrez GitHub Desktop
2. Vérifiez que vous êtes sur 'main'
3. Dans la colonne gauche :
   - Fichiers modifiés en jaune
   - Nouveaux fichiers en vert
4. Sélectionnez les fichiers à commiter
5. Ajoutez un titre explicatif
6. 'Commit to main'
7. 'Push origin'

### Récupérer les Mises à Jour
1. 'Fetch origin' (vérifie)
2. Si changements : 'Pull origin'
3. Résolvez les conflits si nécessaire

### Étapes pour Commiter votre Projet Air Quality

#### Étape 1 : Vérification Initiale
1. Ouvrez GitHub Desktop
2. Vous verrez deux types de fichiers :
   - En jaune : fichiers modifiés
   - En vert : nouveaux fichiers

#### Étape 2 : Sélection des Fichiers
Commitez ces fichiers :
- `app.py`
- `database/schema.sql`
- `database/queries.sql`
- Dossier `static`
- Dossier `templates`
- `requirements.txt`
- `README.md`
- `.gitignore`
   - `README.md` : Documentation du projet

3. **Templates et Statiques** :
   - Dossier `templates/` : Tous les fichiers `.html`
   - Dossier `static/` :
     - Fichiers CSS (`.css`)
     - Fichiers JavaScript (`.js`)
     - Images (`.png`, `.jpg`, `.gif`)

4. **Scripts SQL** :
   - `database/schema.sql` : Structure de la base
   - `database/queries.sql` : Requêtes importantes

#### Fichiers à NE JAMAIS Commiter
1. **Fichiers Sensibles** :
   - `.env` : Variables d'environnement
   - Fichiers de configuration avec mots de passe
   - Clés API ou secrets

2. **Fichiers Générés** :
   - `__pycache__/` : Cache Python
   - `*.pyc` : Fichiers Python compilés
   - `venv/` : Environnement virtuel

3. **Bases de Données** :
   - `*.db` : Bases SQLite
   - `*.sqlite3` : Bases SQLite
   - Sauvegardes de base de données

4. **Fichiers Temporaires** :
   - `.vscode/` : Configuration VS Code
   - `.idea/` : Configuration PyCharm
   - `*.log` : Fichiers de logs

#### Comment Vérifier les Fichiers à Commiter
1. Dans GitHub Desktop :
   - Zone gauche : liste des changements
   - ✅ Fichiers en vert : nouveaux fichiers
   - 🔄 Fichiers en jaune : modifications
   - ❌ Fichiers en rouge : suppressions

2. Avant chaque commit :
   - Vérifiez chaque fichier modifié
   - Lisez les changements dans l'onglet 'Changes'
   - Assurez-vous qu'aucun fichier sensible n'est inclus

3. Bonnes Pratiques :
   - Commitez fréquemment (après chaque fonctionnalité)
   - Vérifiez deux fois les fichiers sensibles
   - Groupez les fichiers liés dans le même commit
   - Ajoutez un message de commit clair

### Créer une Branche
1. 'Current Branch' (en haut)
2. 'New Branch'
3. Nommage :
   - `feature/nom` : nouvelle fonction
   - `fix/nom` : correction
4. 'Create branch'
5. 'Publish branch'

## 5. Bonnes Pratiques

### Messages de Commit
```
type: description courte

- détail 1
- détail 2
```
Types :
- `feat` : nouvelle fonction
- `fix` : correction
- `docs` : documentation
- `style` : formatage
- `refactor` : restructuration

### Organisation des Branches
- `main` : code stable
- `develop` : développement
- `feature/*` : nouvelles fonctions
- `fix/*` : corrections

### Sécurité
- Ne jamais commiter :
  - Mots de passe
  - Clés API
  - `.env`
  - Données sensibles

## 6. Résolution de Problèmes

### Conflit de Fusion
1. Les fichiers en conflit sont marqués
2. Ouvrez-les dans votre éditeur
3. Choisissez les modifications à garder
4. Sauvegardez
5. Commitez la résolution

### Annuler des Changements
1. Fichier non commité :
   - Clic droit > Discard changes
2. Dernier commit :
   - History > Revert

## 7. Liens Utiles

- [Documentation GitHub](https://docs.github.com/fr)
- [GitHub Desktop](https://desktop.github.com/)
- [Guide Git](https://training.github.com/downloads/fr/github-git-cheat-sheet/)
- [Flask](https://flask.palletsprojects.com/)