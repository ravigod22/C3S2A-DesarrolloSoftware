class RepositorioUsuario:
    def __init__ (self):
        self.usuarios = {}
        self.contador = 1
    
    def crearUsuario(self, nombre, correo):
        for usuario in self.usuarios.values():
            if usuario["correo"] == correo:
                raise ValueError("Usuario ya registrado")

        usuario = {"id" : self.contador, "nombre" : nombre, "correo" : correo}
        self.usuarios[self.contador] = usuario
        self.contador += 1
        return usuario
    
    def obtenerUsuario(self, id):
        if id not in self.usuarios:
            raise ValueError("El usuario no existe")
        return self.usuarios[id]
    
    def actualizarUsuario(self, id, nombre, correo):
        if id not in self.usuarios:
            raise ValueError("El usuario no existe")
        
        self.usuarios[id]["nombre"] = nombre
        self.usuarios[id]["correo"] = correo
        return self.usuarios[id]

    def eliminarUsuario(self, id):
        if id not in self.usuarios:
            raise ValueError("El usuario no existe")
        
        usuario = self.usuarios[id]
        del self.usuarios[id]
        return usuario

    def todos(self):
        return self.usuarios
