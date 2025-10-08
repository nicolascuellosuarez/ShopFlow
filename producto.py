class Producto:
    def __init__(self, id: str, nombre: str, categoria: str, precio: float, stock: int):
        self.__id: str = id
        self.__nombre: str = nombre
        self.__categoria_: str = categoria
        self.__precio: float = precio
        self.__stock: int = stock
    
    def actualizar_precio(self, nuevo_precio):
        if nuevo_precio > 0:
            self.__precio = nuevo_precio
            return f"Precio cambiado de forma exitosa."
        return f"El precio nuevo no es válido"
    
    def actualizar_stock(self, nueva_cantidad):
        if nueva_cantidad >= 0:
            self.__stock = nueva_cantidad
            return f"Stock cambiado con éxito."
        return f"La nueva cantidad no es válida."
    
    def reducir_stock(self, cantidad) -> str:
        if cantidad > 0 and self.__stock >= cantidad:
            self.__stock -= cantidad
            return f"Stock disminuído con éxito."
        return f"No se puede disminuir el Stock con esta cantidad."
    
    def aumentar_stock(self, cantidad) -> str:
        if cantidad > 0:
            self.__stock += cantidad
            return f"Stock aumentado con éxito."
        return f"No se pudo aumentar el stock."
    
    def __str__(self) -> str:
        return f"ID: {self.__id}, Nombre: {self.__nombre}, Categoría: {self.__categoria}, Precio: ${self.__precio:.2f}, Stock: {self.__stock}"
    
    def __eq__(self, other) -> bool | str:
        if isinstance(other, Producto):
            return self.__id == other.get_id()
        return False
