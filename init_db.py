import sqlite3

# Kreira se baza podataka (fajl će se zvati drivers.db)
conn = sqlite3.connect('drivers.db')
cursor = conn.cursor()

# Kreiranje tabele za vozače
cursor.execute('''
CREATE TABLE IF NOT EXISTS drivers (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    location TEXT NOT NULL,
    dimensions TEXT,
    specifications TEXT,
    is_available BOOLEAN,
    next_location TEXT,
    available_date TEXT
)
''')

conn.commit()
conn.close()

print("Baza i tabela uspešno kreirane.")