import bcrypt

class RegistroUsuarios:
    
    def __init__(self):
        self.usuarios = {}
        
    def hashearContrasena(self, contrasena):
        return bcrypt.hashpw(contrasena.encode('utf-8'), bcrypt.gensalt())
    
    def autenticacion(self, hasheo, contrasena):
        if isinstance(contrasena, str):
            contrasena = contrasena.encode('utf-8')
        return bcrypt.checkpw(contrasena, hasheo)
    
    def agregarUsuario(self, usuario):
        if usuario.idUsuario in self.usuarios:
            raise ValueError("Usuario existente")
        
        hasheo = self.hashearContrasena(usuario.contrasena)
        usuario.contrasena = hasheo
        self.usuarios[usuario.idUsuario] = usuario
        return True
        
    def autenticarUsuario(self, usuario):
        if usuario.idUsuario not in self.usuarios:
            return False
        
        usuarioExistente = self.usuarios[usuario.idUsuario]
        
        return self.autenticacion(usuarioExistente.contrasena, usuario.contrasena)
    
    def Limpiar(self):
        self.usuarios.clear()