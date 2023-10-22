import sqlite3

# Établir une connexion à la base de données
conn = sqlite3.connect('ma_base_de_donnees.db')
cur = conn.cursor()

# Vider la table 'episode'
cur.execute('DELETE FROM episode')

# Confirmer la suppression
conn.commit()

# Fermer la connexion
conn.close()