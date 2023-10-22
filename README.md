# TV Show Project

Ce projet qui est un projet de fin du module Python pour le cycle de Mastère en Développement Web Full-Stack avec LiveCampus consiste à scraper un site web pour en extraire les données dans un format spécifique (dans notre cas le format choisit est CSV) puis les insérer dans une base de données et aussi réaliser certaines manipulations sur ces données.

# Table de matières

* Contributeurs
* Prérequis
* Installation
* Algorithmie

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

        - python -m venv venv
        - venv\scripts\activate

   * Sur Linux :

        - python3 -m venv venv
        - source venv/bin/activate

   * Sur MacOs :

        - python3 -m venv venv
        - source ven/bin/activate

   * Ne pas oublier d'installer les packages nécessaires au bon déroulement du   
     projet (voir fichier requirements.txt):

        - pip3 install -r requirements.txt --upgrade
   

# Algorithmie :

1. Pour trouver le nombre d'épisode de chaque chaine, on peut utiliser ce bout de code :

          - Requête SQL pour extraire les épisodes diffusés en octobre :
   
              cur.execute('''
                SELECT channel, COUNT(*) as episode_count
                FROM episode
                WHERE EXTRACT(MONTH FROM TO_DATE(date, 'DD-MM-YYYY')) = 10
                GROUP BY channel
                ORDER BY episode_count DESC
                ''')

            En executant cette requête, nous trouvons qu'il y'a 587 épisodes diffusés en Octobre.
   
3.  Pour trouver le nombre d'épisode de chaque pays :

          - Requête SQL pour extraire les épisodes diffusés en octobre par pays :
    
              cur.execute('''
                SELECT country, COUNT(*) as episode_count
                FROM episode
                WHERE EXTRACT(MONTH FROM TO_DATE(date, 'DD-MM-YYYY')) = 10
                GROUP BY country
                ORDER BY episode_count DESC
                ''')
    
            Voici la liste du nombre d'épisodes diffusées dans chaque pays :

               - Etats-Unis: 357 épisodes
               - France: 76 épisodes
               - Canada: 64 épisodes
               - Royaume-Uni: 34 épisodes
               - Allemagne: 16 épisodes
               - Espagne: 14 épisodes
               - Suède: 13 épisodes
               - Corée du Sud: 5 épisodes
               - Belgique: 4 épisodes
               - Danemark: 1 épisodes
               - Australie: 1 épisodes
    
5.  Les mots le plus utilisées :

    * The : 66
    * of : 31
    * de : 24
    * (2023) : 19
    * Pacto : 18
    * Silencio : 18
    * Les : 17
    * the : 16
    * Everything : 12
    * (UK) : 12
