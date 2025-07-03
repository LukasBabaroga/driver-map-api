import sqlite3

conn = sqlite3.connect('drivers.db')
cursor = conn.cursor()

# Dodavanje vozača Jacob Davis
cursor.execute('''
INSERT INTO drivers (name, location, dimensions, specifications, is_available, next_location, available_date)
VALUES (?, ?, ?, ?, ?, ?, ?)
''', (
    'Jacob Davis',
    '0,0',
    '5x2x2',
    'Truck',
    True,
    None,
    None
))

# Dodavanje vozača Luka Andj
cursor.execute('''
INSERT INTO drivers (name, location, dimensions, specifications, is_available, next_location, available_date)
VALUES (?, ?, ?, ?, ?, ?, ?)
''', (
    'Luka Andj',
    '0,0',
    '4x2x2',
    'Van',
    True,
    None,
    None
))

conn.commit()
conn.close()

print("Jacob Davis i Luka Andj su uspešno dodati!")
