from flask import Flask, jsonify, request, send_from_directory
import sqlite3
import os

app = Flask(__name__)

# Conectar a la base de datos
def connect_db():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn

# Ruta para servir la página HTML
@app.route('/')
def index():
    return send_from_directory(os.path.join(app.root_path, ''), 'index.html')

# Ruta para obtener todos los clientes
@app.route('/clients', methods=['GET'])
def get_clients():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM clients')
    clients = [dict(row) for row in cursor.fetchall()]
    conn.close()
    return jsonify(clients)

# Ruta para obtener un cliente por ID
@app.route('/clients/<int:id>', methods=['GET'])
def get_client(id):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM clients WHERE id=?', (id,))
    client = cursor.fetchone()
    conn.close()
    if client:
        return jsonify(dict(client))
    return jsonify({'error': 'Client not found'}), 404

# Ruta para añadir un nuevo cliente
@app.route('/clients', methods=['POST'])
def add_client():
    new_client = request.get_json()
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('INSERT INTO clients (name, address, phone) VALUES (?, ?, ?)',
                   (new_client['name'], new_client['address'], new_client['phone']))
    conn.commit()
    conn.close()
    return jsonify(new_client), 201

# Ruta para actualizar un cliente existente
@app.route('/clients/<int:id>', methods=['PUT'])
def update_client(id):
    updated_client = request.get_json()
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('UPDATE clients SET name=?, address=?, phone=? WHERE id=?',
                   (updated_client['name'], updated_client['address'], updated_client['phone'], id))
    conn.commit()
    conn.close()
    return jsonify(updated_client)

# Ruta para eliminar un cliente
@app.route('/clients/<int:id>', methods=['DELETE'])
def delete_client(id):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('DELETE FROM clients WHERE id=?', (id,))
    conn.commit()
    conn.close()
    return jsonify({'message': 'Client deleted'})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
