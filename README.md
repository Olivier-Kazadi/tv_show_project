# TV Show Project

Ce projet qui est un projet de fin du module Python pour le cycle de Mastère en Développement Web Full-Stack avec LiveCampus consiste à scraper un site web pour en extraire les données dans un format spécifique (dans notre cas le format choisit est CSV) puis les insérer dans une base de données et aussi réaliser certaines manipulations sur ces données.

# Table de matières

* Contributeurs
* Prérequis
* Installation

# Contributeurs

Pour ce projet, nous avons choisis de travailler en groupe de trois. Il a dont été réalisé par Ben Yamine Ali, Pierre Boscus et Kazadi Olivier.

# Prérequis

Afin de pouvoir exécuter ce projet, vous devez vous assurer d'avoir la bonne version de Python installé sur votre PC:

* Python 3.6 ou un version ultérieure

# Installation

1. Pour clôner ce dépot :

   * git clone https://github.com/Olivier-Kazadi/tv_show_project.git
   
2. Certaines dépendances doivent être installées pour le bon déroulement du projet:

   cd your_project

   * Création de l'environnement Windows :

      python -m venv venv
      venv\scripts\activate

   * Sur Linux :

      python3 -m venv venv
      source venv/bin/activate

   * Sur MacOs :

      python3 -m venv venv
      source ven/bin/activate

   * Ne pas oublier d'installer les packages nécessaires au bon déroulement du   
     projet (voir fichier requirements.txt):

      pip3 install -r requirements.txt --upgrade
   
3. Fichier principal d'utilisation :

   * python3 main.py
