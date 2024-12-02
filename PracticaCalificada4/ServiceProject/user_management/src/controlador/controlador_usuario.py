from flask import Flask, request, jsonify
from src.servicio.servicio_usuario import ServicioUsuario

app = Flask(__name__)

servicio = ServicioUsuario()

@app.route('/usuario', methods=['POST'])
def crear_Usuario():
    try:
        datos = request.json
        nombre = datos.get('nombre')
        correo = datos.get('correo')

        if not nombre or not correo:
            return jsonify({'error': 'datos incompletos'}), 400

        usuario = servicio.crearUsuario(nombre, correo)
        return jsonify(usuario), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/usuario/<int:id>', methods=['GET'])
def obtener_usuario(id):
    try:
        usuario = servicio.obtenerUsuario(id)
        if usuario:
            return jsonify(usuario), 200
        return jsonify({'error': 'usuario no encontrado'}), 404
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/usuario/<int:id>', methods=['PUT'])
def actualizar_usuario(id):
    try:
        datos = request.json
        nombre = datos.get('nombre')
        correo = datos.get('correo')

        if not nombre or not correo:
            return jsonify({'error': 'datos incompletos'}), 400
        
        usuario = servicio.actualizarUsuario(id, nombre, correo)
        return jsonify(usuario), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/usuario/<int:id>', methods=['DELETE'])
def eliminar_usuario(id):
    try:
        usuario = servicio.eliminarUsuario(id)
        return jsonify({'mensaje' : 'Eliminacion con exito', 'usuario': usuario}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    
@app.route('/usuarios', methods=['GET'])
def obtener_todos():
    try:
        usuarios = servicio.todos()
        return jsonify(usuarios), 200
    except Exception as e:
        return  jsonify({'error': str(e)}), 500

if __name__ == 'main':
    app.run(debug=True)