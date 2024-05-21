# La-jolie-boite-a-code

Bienvenue dans **La jolie boîte à code** ! Ce projet est un CRM (Customer Relationship Management) développé en Python. Il permet aux entreprises de s'inscrire et de gérer les informations de leurs employés.


## Introduction

**La jolie boîte à code** est un système de gestion de la relation client (CRM) simple et efficace, conçu pour aider les entreprises à organiser et à gérer leurs informations de manière centralisée. Chaque entreprise peut s'inscrire et ajouter des informations sur ses employés.

## Fonctionnalités

- Inscription des entreprises
- Gestion des profils des employés
- Interface utilisateur intuitive
- Sauvegarde des données dans une base de données SQLite
- Authentification sécurisée

## Installation

Pour installer et exécuter ce projet localement, veuillez suivre les étapes ci-dessous :

1. Clonez le dépôt GitHub

2. Créez un environnement virtuel :
    ```bash
    python -m venv env
    ```

3. Activez l'environnement virtuel :

    - Sur Windows :
        ```bash
        .\env\Scripts\activate
        ```
    - Sur macOS/Linux :
        ```bash
        source env/bin/activate
        ```

4. Installez les dépendances requises :
    ```bash
    pip install -r requirements.txt
    ```

5. Initialisez la base de données :
    ```bash
    python manage.py migrate
    ```

6. Démarrez le serveur :
    ```bash
    python manage.py runserver
    ```

7. Ouvrez votre navigateur et accédez à `http://127.0.0.1:8000/`.

## Utilisation

1. Inscrivez-vous en tant qu'entreprise.
2. Connectez-vous à votre tableau de bord.
3. Ajoutez des employés et gérez leurs informations.

