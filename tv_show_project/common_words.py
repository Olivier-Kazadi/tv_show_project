import psycopg2
import requests
from bs4 import BeautifulSoup
from collections import Counter

# Récupère les données du site web
url = "https://www.spin-off.fr/"
r = requests.get(url)
soup = BeautifulSoup(r.text, "html.parser")

# Initialise la liste de données
data = []

# Extrait les informations des séries à partir du BeautifulSoup passé en paramètre
dates_divs = soup.find_all('div', class_='div_jour')
tds = soup.find_all('td', class_='td_jour')

for td in tds:
    if td.text.strip() != "":
        div_date = td.find('div').get('id')
        dates_final = div_date.split('_')[1]
        series_info = td.find_all('span', class_='calendrier_episodes')

        for serie in series_info:
            country_img = serie.find_previous('img', alt=True)
            country = country_img['alt']
            channel_img = country_img.find_next('img', alt=True)
            channel = channel_img['alt']
            series_name = serie.find('a').text
            episode_details = serie.find('a', class_='liens').text
            url_episode = serie.find('a', class_='liens')['href']
            season, episode = episode_details.split('.')
            data.append([dates_final, country, channel, series_name, season, episode, url + url_episode])

# Crée une liste pour stocker les noms des séries
series_names = [entry[3] for entry in data]

# Trouver les 10 mots les plus courants dans les noms des séries
all_series_names = ' '.join(series_names)  # Combine tous les noms des séries en une seule chaîne de caractères
words = all_series_names.split()  # Divise les noms en mots
word_counts = Counter(words)  # Compte la fréquence de chaque mot
top_10_words = word_counts.most_common(10)  # Obtient les 10 mots les plus courants

for word, count in top_10_words:
    print(f"{word}: {count}")