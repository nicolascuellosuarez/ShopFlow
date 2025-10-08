from producto import Producto

class Inventario:
    def __init__(self):
        self.__productos: dict[str, Producto] = {}
    
    def agregar_producto(self, producto):
        if producto.get_id() not in self.__productos:
            self.__productos[producto.get_id()] = producto
            return True
        return False
    
    def eliminar_producto(self, id_producto):
        if id_producto in self.__productos:
            del self.__productos[id_producto]
            return True
        return False
    
    def buscar_por_id(self, id_producto):
        return self.__productos.get(id_producto)
    
    def buscar_por_nombre(self, nombre):
        resultados = []
        for producto in self.__productos.values():
            if nombre.lower() in producto.get_nombre().lower():
                resultados.append(producto)
        return resultados
    
    def actualizar_stock(self, id_producto, nueva_cantidad):
        producto = self.buscar_por_id(id_producto)
        if producto:
            return producto.actualizar_stock(nueva_cantidad)
        return False
    
    def filtrar_por_categoria(self, categoria):
        resultados = []
        for producto in self.__productos.values():
            if producto.get_categoria().lower() == categoria.lower():
                resultados.append(producto)
        return resultados
    
    def ordenar_por_precio(self, ascendente=True):
        productos = list(self.__productos.values())
        return sorted(productos, key=lambda x: x.get_precio(), reverse=not ascendente)
    
    def verificar_disponibilidad(self, id_producto, cantidad):
        producto = self.buscar_por_id(id_producto)
        if producto and producto.get_stock() >= cantidad:
            return True
        return False
    
    def obtener_todos_productos(self):
        return list(self.__productos.values())
    
    def __str__(self):
        if not self.__productos:
            return "Inventario vacío"
        return "\n".join(str(producto) for producto in self.__productos.values())
