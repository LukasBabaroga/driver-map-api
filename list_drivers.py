import sqlite3

conn = sqlite3.connect('drivers.db')
cursor = conn.cursor()

cursor.execute("SELECT id, name, location FROM drivers")
drivers = cursor.fetchall()

for d in drivers:
    print(f"ID: {d[0]} | Name: {d[1]} | Location: {d[2]}")

conn.close()
