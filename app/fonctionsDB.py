import sqlite3
connection = sqlite3.connect('swiftlinkdb.db')
print(connection.total_changes)
cursor = connection.cursor()

# mettre un cursor.execute initial pour la création de la base de donnée
