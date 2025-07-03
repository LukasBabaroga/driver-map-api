from flask import Flask, request, jsonify, send_from_directory
import os
from flask_cors import CORS
import sqlite3

app = Flask(__name__)
CORS(app)  # omogućava da frontend može da pristupi backendu

DB_FILE = 'drivers.db'

def get_db_connection():
    conn = sqlite3.connect(DB_FILE)
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/add_driver', methods=['POST'])
def add_driver():
    data = request.json
    conn = get_db_connection()
    conn.execute('''
        INSERT INTO drivers (name, location, dimensions, specifications, is_available, next_location, available_date)
        VALUES (?, ?, ?, ?, ?, ?, ?)
    ''', (
        data['name'],
        data['location'],
        data['dimensions'],
        data['specifications'],
        data['is_available'],
        data.get('next_location'),
        data.get('available_date')
    ))
    conn.commit()
    conn.close()
    return jsonify({'status': 'success'}), 201

@app.route('/drivers', methods=['GET'])
def get_drivers():
    conn = get_db_connection()
    drivers = conn.execute('SELECT * FROM drivers').fetchall()
    conn.close()
    return jsonify([dict(d) for d in drivers])


@app.route('/')
def serve_index():
    return send_from_directory('.', 'index.html')


@app.route('/driver_page.html')
def serve_driver_page():
    return send_from_directory('.', 'driver_page.html')

@app.route('/debug_drivers')
def debug_drivers():
    conn = get_db_connection()
    drivers = conn.execute("SELECT id, name, location FROM drivers").fetchall()
    conn.close()
    return jsonify([dict(d) for d in drivers])


if __name__ == '__main__':
    app.run(debug=True)