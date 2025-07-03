import sqlite3

conn = sqlite3.connect('drivers.db')
cursor = conn.cursor()

cursor.execute('''
INSERT INTO drivers (name, location, dimensions, specifications, is_available, next_location, available_date)
VALUES (?, ?, ?, ?, ?, ?, ?)
''', (
    'John Doe',
    'New York, USA',
    '5x2x2',
    'Truck with lift',
    True,
    None,
    None
))

conn.commit()
conn.close()

print("Test driver ubacen!")
