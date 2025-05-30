import sqlite3

conn = sqlite3.connect('logs.db')
cursor = conn.cursor()

cursor.execute('SELECT * FROM logs ORDER BY id DESC')
rows = cursor.fetchall()

print("Последние записи логов:")
for row in rows:
    print(row)

conn.close()
