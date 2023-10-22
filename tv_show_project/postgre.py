URL_DB = "postgres://ben_appli_5474:xTBmIHQcRx-Z8ru3d0co@ben-appli-5474.postgresql.a.osc-fr1.scalingo-dbs.com:33375/ben_appli_5474?sslmode=prefer"

import psycopg2
import requests
from bs4 import BeautifulSoup

conn = None
cur = None

# Extraction des données depuis le site Web
url = "https://www.spin-off.fr/calendrier_des_series.html"

"""Récupère les données du site web."""
r = requests.get(url)
soup = BeautifulSoup(r.text, "html.parser")


"""Extrait les informations des séries à partir du BeautifulSoup passé en paramètre."""
dates_divs = soup.find_all('div', class_='div_jour')
tds = soup.find_all('td',class_ = 'td_jour')


data = []
for  td in tds :
    if td.text.strip() != "":
        div_date = td.find('div').get('id')
        dates_final= div_date.split('_')[1]
        series_info = td.find_all('span', class_='calendrier_episodes')

        for i, serie in enumerate(series_info):
            country_img = serie.find_previous('img', alt=True)
            country = country_img['alt']
            channel_img = country_img.find_next('img', alt=True)
            channel = channel_img['alt']
            series_name = serie.find('a').text
            episode_details = serie.find('a', class_='liens').text
            url_episode = serie.find('a', class_='liens')['href']
            season, episode = episode_details.split('.')
            data.append([dates_final, country, channel, series_name, season, episode, url + url_episode])

try:
    conn = psycopg2.connect(URL_DB)
    print("Connexion réussie")

    # Création d'un curseur pour exécuter des commandes SQL
    cur = conn.cursor()

    # Définition du schéma de la table episode
    cur.execute('''
        CREATE TABLE IF NOT EXISTS episode (
            id SERIAL PRIMARY KEY,
            date TEXT,
            country TEXT,
            channel TEXT,
            series_name TEXT,
            season INTEGER,
            episode INTEGER,
            url TEXT
        )
    ''')

    # Validation des modifications
    conn.commit()

    # Insérer les données dans la table 'episode'
    for entry in data:
        cur.execute('''
            INSERT INTO episode (date, country, channel, series_name, season, episode, url)
            VALUES (%s, %s, %s, %s, %s, %s, %s)
        ''', entry)

    conn.commit()

    # Afficher les données de la table 'episode'
    cur.execute("SELECT * FROM episode")
    results = cur.fetchall()

    for row in results:
        print(row)

except psycopg2.Error as e:
    print(e)

finally:
    # Fermer le curseur et la connexion
    if conn:
        cur.close()
        conn.close()
        print("Connexion à la base de données fermée.")