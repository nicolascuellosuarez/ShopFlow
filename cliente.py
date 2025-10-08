from carrito import Carrito
from pedido import Pedido

class Cliente:
    def _init_(self, id, nombre, telefono, correo) -> None:
        self.__id = id
        self.__nombre = nombre
        self.__telefono = telefono
        self.__correo = correo
        self.__carrito = Carrito(f"C{id}", self)
        self.__historial = []
    
    def get_id(self) -> str:
        return self.__id
    
    def get_nombre(self) -> str:
        return self.__nombre
    
    def get_telefono(self) -> str:
        return self.__telefono
    
    def get_correo(self) -> str:
        return self.__correo
    
    def get_carrito(self) -> str:
        return self.__carrito
    
    def agregar_al_carrito(self, producto, cantidad, inventario) -> bool:
        return self.__carrito.agregar_producto(producto, cantidad, inventario)
    
    def realizar_pedido(self, inventario) -> Optional[Pedido]:
        if not self.__carrito.verificar_stock(inventario):
            return None
        
        pedido = Pedido(f"P{len(self._historial) + 1}", self, self._carrito.get_productos())
        
        for producto, cantidad in self.__carrito.get_productos().items():
            inventario.actualizar_stock(producto.get_id(), producto.get_stock() - cantidad)
        
        self.__historial.append(pedido)
        self.__carrito.vaciar()
        return pedido
    
    def ver_historial(self) -> List[Pedido]:
        return self.__historial.copy()
    
    def _str_(self) -> str:
        return f"Cliente {self._id}: {self.nombre} - {self.telefono} - {self._correo}"
