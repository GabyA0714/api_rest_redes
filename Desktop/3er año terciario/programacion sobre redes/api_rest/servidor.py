from flask import Flask, request, jsonify
from werkzeug.security import generate_password_hash, check_password_hash
import sqlite3

app = Flask(__name__)

# Función para inicializar la base de datos si no existe
def inicializar_bd():
    conexion = sqlite3.connect('base_datos.db')
    cursor = conexion.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS usuarios (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            usuario TEXT UNIQUE NOT NULL,
            contrasena TEXT NOT NULL
        )
    ''')
    conexion.commit()
    conexion.close()

# Endpoint 1: Registro
@app.route('/registro', methods=['POST'])
def registro():
    datos = request.get_json()
    usuario = datos.get('usuario')
    contrasena = datos.get('contraseña')

    if not usuario or not contrasena:
        return jsonify({"error": "Faltan datos (usuario o contraseña)"}), 400

    hash_contrasena = generate_password_hash(contrasena)

    try:
        conexion = sqlite3.connect('base_datos.db')
        cursor = conexion.cursor()
        cursor.execute("INSERT INTO usuarios (usuario, contrasena) VALUES (?, ?)", (usuario, hash_contrasena))
        conexion.commit()
        conexion.close()
        return jsonify({"mensaje": "Usuario registrado exitosamente"}), 201
    except sqlite3.IntegrityError:
        # Cierro la conexión antes de devolver el error
        conexion.close() 
        return jsonify({"error": "El usuario ya existe en el sistema"}), 400

# Endpoint 2: Login
@app.route('/login', methods=['POST'])
def login():
    datos = request.get_json()
    usuario = datos.get('usuario')
    contrasena = datos.get('contraseña')

    conexion = sqlite3.connect('base_datos.db')
    cursor = conexion.cursor()
    cursor.execute("SELECT contrasena FROM usuarios WHERE usuario = ?", (usuario,))
    resultado = cursor.fetchone()
    conexion.close()

    # Comprobamos si el usuario existe y si la contraseña coincide con el hash
    if resultado and check_password_hash(resultado[0], contrasena):
        return jsonify({"mensaje": "Login exitoso. Bienvenido a tus tareas."}), 200
    else:
        return jsonify({"error": "Credenciales incorrectas"}), 401

# Endpoint 3: Tareas (HTML)
@app.route('/tareas', methods=['GET'])
def tareas():
    html_bienvenida = """
    <!DOCTYPE html>
    <html lang="es">
    <head>
        <meta charset="UTF-8">
        <title>Mis Tareas</title>
    </head>
    <body style="font-family: Arial, sans-serif; padding: 20px;">
        <h2>¡Bienvenido al Gestor de Tareas!</h2>
        <p>Acá vas a poder ver y gestionar tus tareas pendientes.</p>
        <hr>
        <ul>
            <li>Tarea 1: Estudiar para Redes</li>
            <li>Tarea 2: Entregar el PFO 2</li>
        </ul>
    </body>
    </html>
    """
    return html_bienvenida, 200

if __name__ == '__main__':
    inicializar_bd()
    print("Servidor iniciando en el puerto 5000...")
    app.run(debug=True, port=5000)