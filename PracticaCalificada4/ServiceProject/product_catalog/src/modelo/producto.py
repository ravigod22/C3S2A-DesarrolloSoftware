class Producto:
    def __init__(self, id, nombre, descripcion, usuario_id):
        self.id = id
        self.nombre = nombre
        self.descripcion = descripcion
        self.usuario_id = usuario_id
    
    def sumary(self):
        return {
            'id': self.id,
            'nombre': self.nombre,
            'descripcion': self.descripcion,
            'usuario_id': self.usuario_id
        }