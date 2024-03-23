from flask import Flask, request, jsonify
import sqlite3
from flask_cors import CORS
app = Flask(__name__)
CORS(app)
# Receiver function to check if the username is available
@app.route('/check_username', methods=['POST'])
def check_username():
    username = request.json.get('username')

    conn = sqlite3.connect('userdata.db')
    cursor = conn.cursor()

    # Query the database to check if the username exists
    cursor.execute('''SELECT * FROM users WHERE username = ?''', (username,))
    user = cursor.fetchone()

    conn.close()

    if user:
        return jsonify({'available': False})
    else:
        return jsonify({'available': True})

# Receiver function to check if the credentials are correct
@app.route('/check_credentials', methods=['POST'])
def check_credentials():
    print("Request Payload:", request.json)
    username = request.json.get('username')
    password = request.json.get('password')
    conn = sqlite3.connect('userdata.db')
    cursor = conn.cursor()

    # Query the database for the provided username and password
    cursor.execute('''SELECT * FROM users WHERE username = ? AND password = ?''', (username, password))
    user = cursor.fetchone()

    conn.close()
    if user:
        return jsonify({'valid': True})
    else:
        return jsonify({'valid': False})

# Receiver function to add a user
@app.route('/add_user', methods=['POST'])
def add_user():
    # Get data sent by the client-side
    data = request.json
    first_name = data.get('first_name')
    last_name = data.get('last_name')
    username = data.get('username')
    password = data.get('password')
    image_path = data.get('image_path')

    # Connect to SQLite database (creates a new one if not exists)
    conn = sqlite3.connect('userdata.db')
    cursor = conn.cursor()

    # Create table if not exists
    cursor.execute('''CREATE TABLE IF NOT EXISTS users (
                        id INTEGER PRIMARY KEY,
                        first_name TEXT,
                        last_name TEXT,
                        username TEXT,
                        password TEXT,
                        image_path TEXT
                    )''')

    # Insert data into the table
    cursor.execute('''INSERT INTO users (first_name, last_name, username, password, image_path) 
                      VALUES (?, ?, ?, ?, ?)''', (first_name, last_name, username, password, image_path))

    # Commit changes and close connection
    conn.commit()
    conn.close()

    return 'User added successfully'

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)  # Change port number as needed
