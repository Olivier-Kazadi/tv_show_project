import psycopg2

# Établir une connexion à la base de données
URL_DB = "postgres://ben_appli_5474:xTBmIHQcRx-Z8ru3d0co@ben-appli-5474.postgresql.a.osc-fr1.scalingo-dbs.com:33375/ben_appli_5474?sslmode=prefer"

conn = psycopg2.connect(URL_DB)
cur = conn.cursor()

# Requête SQL pour extraire les épisodes diffusés en octobre
cur.execute('''
    SELECT channel, COUNT(*) as episode_count
    FROM episode
    WHERE EXTRACT(MONTH FROM TO_DATE(date, 'DD-MM-YYYY')) = 10
    GROUP BY channel
    ORDER BY episode_count DESC
''')

# Récupérer les résultats de la requête
results = cur.fetchall()

# Afficher le nombre d'épisodes par chaîne
print("Nombre d'épisodes diffusés par chaîne en Octobre :")
for row in results:
    channel, episode_count = row
    print(f"{channel}: {episode_count} épisodes")

# Fermer la connexion à la base de données
cur.close()
conn.close()