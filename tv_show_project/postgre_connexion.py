import psycopg2

URL_DB = "postgres://ben_appli_5474:xTBmIHQcRx-Z8ru3d0co@ben-appli-5474.postgresql.a.osc-fr1.scalingo-dbs.com:33375/ben_appli_5474?sslmode=prefer"

# Établir une connexion à la base de données
conn = psycopg2.connect(URL_DB)
cur = conn.cursor()

# Utiliser TRUNCATE pour vider la table 'episode'
cur.execute('TRUNCATE episode RESTART IDENTITY')

# Confirmer la suppression et la réinitialisation de l'ID
conn.commit()

# Fermer la connexion
conn.close()