import sqlite3
import requests
from bs4 import BeautifulSoup

# Établir une connexion à la base de données
conn = sqlite3.connect('ma_base_de_donnees.db')
cur = conn.cursor()

# Créer la table 'episode' si elle n'existe pas
cur.execute('''
    CREATE TABLE IF NOT EXISTS episode (
        id INTEGER PRIMARY KEY,
        date TEXT,
        country TEXT,
        channel TEXT,
        series_name TEXT,
        season INTEGER,
        episode INTEGER,
        url TEXT
    )
''')

# Faites votre requête pour obtenir les données
url = "https://www.spin-off.fr/"

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
print(data)
# Insérer les données dans la table
for entry in data:
    cur.execute('''
        INSERT INTO episode (date, country, channel, series_name, season, episode, url)
        VALUES (?, ?, ?, ?, ?, ?, ?)
    ''', entry)

# Valider les modifications
conn.commit()

# Afficher les données de la table 'episode'
cur.execute("SELECT * FROM episode")
results = cur.fetchall()

for row in results:
    print(row)

# Fermer la connexion
conn.close()