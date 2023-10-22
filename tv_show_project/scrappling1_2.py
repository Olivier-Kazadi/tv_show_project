import requests
from bs4 import BeautifulSoup
import time
import sqlite3
import csv



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
    # Récupération de la saison et de l'épisode
    # season, episode = episode_details.split('.')
    # data.append((country, channel, series_name, episode_details))
 files = "data/files/episodes.csv"
 with open(files, 'w', newline='') as fichier:
     writer = csv.writer(fichier)
     for ligne in data:
        writer.writerow(ligne)