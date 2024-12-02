from src.repositorio.repositorio_usuario import RepositorioUsuario

class ServicioUsuario:
    def __init__(self):
        self.repositorio = RepositorioUsuario()
    
    def crearUsuario(self, nombre, correo):
        return self.repositorio.crearUsuario(nombre, correo)
    
    def obtenerUsuario(self, id):
        return self.repositorio.obtenerUsuario(id)
    
    def actualizarUsuario(self, id, nombre, correo):
        return self.repositorio.actualizarUsuario(id, nombre, correo)
    
    def eliminarUsuario(self, id):
        return self.repositorio.eliminarUsuario(id)
    
    def todos(self):
        return list(self.repositorio.todos())
