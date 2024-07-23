from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)

# Initialize the database
def init_db():
    conn = sqlite3.connect('queries.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS queries
                 (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, phone TEXT, email TEXT, query TEXT)''')
    conn.commit()
    conn.close()

@app.route('/submit-query', methods=['POST'])
def submit_query():
    data = request.get_json()
    name = data['name']
    phone = data['phone']
    email = data['email']
    query = data['query']

    conn = sqlite3.connect('queries.db')
    c = conn.cursor()
    c.execute("INSERT INTO queries (name, phone, email, query) VALUES (?, ?, ?, ?)",
              (name, phone, email, query))
    conn.commit()
    conn.close()

    return jsonify({'message': 'Query submitted successfully'}), 200

if __name__ == '__main__':
    init_db()
    app.run(debug=True)
