from datetime import datetime

class Pedido:
    def __init__(self, id: str, cliente: str, productos: str)->None:
        self.__id: str = id
        self.__cliente: str = cliente
        self.__productos: str = productos.copy()
        self.__total: float = self.calcular_total()
        self.__fecha: datetime = datetime.now()
        self.__estado: str = "pendiente"
    
    def get_id(self)->str:
        return self.__id
    
    def get_cliente(self)->str:
        return self.__cliente
    
    def get_productos(self)->str:
        return self.__productos.copy()
    
    def get_total(self)->str:
        return self.__total
    
    def get_fecha(self)->str:
        return self.__fecha
    
    def get_estado(self)->str:
        return self.__estado
    
    def calcular_total(self)->str:
        total = 0
        for producto, cantidad in self.__productos.items():
            total += producto.get_precio() * cantidad
        return total
    
    def actualizar_estado(self, nuevo_estado)->str:
        self.__estado = nuevo_estado
    
    def generar_comprobante(self)->str:
        comprobante = f"COMPROBANTE DE PEDIDO\n"
        comprobante += f"ID: {self.__id}\n"
        comprobante += f"Cliente: {self.__cliente.get_nombre()}\n"
        comprobante += f"Fecha: {self.__fecha.strftime('%Y-%m-%d %H:%M:%S')}\n"
        comprobante += f"Estado: {self.__estado}\n"
        comprobante += "Productos:\n"
        
        for producto, cantidad in self.__productos.items():
            comprobante += f"  - {producto.get_nombre()} x{cantidad} @ ${producto.get_precio():.2f} = ${producto.get_precio() * cantidad:.2f}\n"
        
        comprobante += f"TOTAL: ${self.__total:.2f}"
        return comprobante
    
    def __str__(self)->str:
        return f"Pedido {self._id} - {self.cliente.get_nombre()} - ${self.total:.2f} - {self._estado}"
