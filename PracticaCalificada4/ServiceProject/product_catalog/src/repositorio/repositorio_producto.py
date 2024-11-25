class RepositorioProducto:
    def __init__(self):
        self.productos = {}
        self.contador = 1

    def crearProducto(self, nombre, descripcion, usuario_id):
        for producto in self.productos.values():
            if producto["nombre"] == nombre:
                raise ValueError("Producto ya registrado")
            
        producto = {
            "id": self.contador,
            "nombre": nombre,
            "descripcion": descripcion,
            "usuario_id": usuario_id
        }
        self.productos[self.contador] = producto
        self.contador += 1
        return producto
    
    def obtenerProducto(self, id):
        if id not in self.productos:
            raise ValueError("El producto no existe")
        return self.productos[id]
    
    def actualizarProducto(self, id, nombre, descripcion):
        if id not in self.productos:
            raise ValueError("El producto no existe")
        
        self.productos[id]["nombre"] = nombre
        self.productos[id]["descripcion"] = descripcion
        return self.productos[id]
    
    def eliminarProducto(self, id):
        if id not in self.productos:
            raise ValueError("El producto no existe")
        
        producto = self.productos[id]
        del self.productos[id]
        return producto

    def obtenerTodos(self):
        return list(self.productos.values())