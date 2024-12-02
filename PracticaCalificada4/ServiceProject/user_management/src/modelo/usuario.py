class Usuario:
    def __init__(self, id, nombre, correo):
        self.id = id
        self.nombre = nombre
        self.correo = correo
    
    def sumary(self):
        return {
            'id': self.id,
            'nombre': self.nombre,
            'correo': self.correo
        }