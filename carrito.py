from producto import Producto
from inventario import Inventario

class Carrito:
    def _init_(self, id, cliente):
        self.__id = id
        self.__cliente = cliente
        self.__productos = {}
        self.__estado = "activo"
    
    def get_id(self):
        return self.__id
    
    def get_cliente(self):
        return self.__cliente
    
    def get_productos(self):
        return self.__productos.copy()
    
    def agregar_producto(self, producto, cantidad, inventario):
        if not inventario.verificar_disponibilidad(producto.get_id(), cantidad):
            return False
        
        if producto in self.__productos:
            self.__productos[producto] += cantidad
        else:
            self.__productos[producto] = cantidad
        return True
    
    def eliminar_producto(self, producto):
        if producto in self.__productos:
            del self.__productos[producto]
            return True
        return False
    
    def actualizar_cantidad(self, producto, nueva_cantidad, inventario):
        if producto not in self.__productos:
            return False
        
        if not inventario.verificar_disponibilidad(producto.get_id(), nueva_cantidad):
            return False
        
        self.__productos[producto] = nueva_cantidad
        return True
    
    def calcular_total(self):
        total = 0
        for producto, cantidad in self.__productos.items():
            total += producto.get_precio() * cantidad
        return total
    
    def vaciar(self):
        self.__productos.clear()
    
    def verificar_stock(self, inventario):
        for producto, cantidad in self.__productos.items():
            if not inventario.verificar_disponibilidad(producto.get_id(), cantidad):
                return False
        return True
    
    def _str_(self):
        if not self.__productos:
            return f"Carrito {self.__id} vacío"
        
        items = []
        for producto, cantidad in self.__productos.items():
            items.append(f"{producto.get_nombre()} x{cantidad} - ${producto.get_precio() * cantidad:.2f}")
        
        return f"Carrito {self.__id} - Total: ${self.calcular_total():.2f}\n" + "\n".join(items)
