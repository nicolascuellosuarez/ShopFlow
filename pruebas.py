from producto import Producto
from inventario import Inventario
from cliente import Cliente
from carrito import Carrito
from pedido import Pedido

def test_producto()->None:
    print(" TEST PRODUCTO ")
    p = Producto("P001", "Test Product", "Test", 100.0, 10)
    assert p.get_id() == "P001"
    assert p.actualizar_precio(150.0) == True
    assert p.get_precio() == 150.0
    assert p.reducir_stock(5) == True
    assert p.get_stock() == 5
    print("Producto: OK")

def test_inventario()->None:
    print(" TEST INVENTARIO ")
    inv = Inventario()
    p = Producto("P001", "Test", "Test", 100.0, 10)
    
    assert inv.agregar_producto(p) == True
    assert inv.agregar_producto(p) == False
    assert inv.buscar_por_id("P001") == p
    assert inv.verificar_disponibilidad("P001", 5) == True
    assert inv.verificar_disponibilidad("P001", 15) == False
    print("Inventario: OK")

def test_carrito()->None:
    print(" TEST CARRITO ")
    from cliente import Cliente
    cliente = Cliente("C001", "Test", "123", "test@test.com")
    carrito = cliente.get_carrito()
    
    inv = Inventario()
    p = Producto("P001", "Test", "Test", 100.0, 10)
    inv.agregar_producto(p)
    
    assert carrito.agregar_producto(p, 2, inv) == True
    assert carrito.calcular_total() == 200.0
    print("Carrito: OK")

def test_cliente_pedido()->None:
    print(" TEST CLIENTE Y PEDIDO ")
    cliente = Cliente("C001", "Test", "123", "test@test.com")
    inv = Inventario()
    p = Producto("P001", "Test", "Test", 100.0, 10)
    inv.agregar_producto(p)
    
    cliente.agregar_al_carrito(p, 2, inv)
    pedido = cliente.realizar_pedido(inv)
    
    assert pedido is not None
    assert len(cliente.ver_historial()) == 1
    assert p.get_stock() == 8
    print("Cliente y Pedido: OK")

if _name_ == "_main_":
    test_producto()
    test_inventario()
    test_carrito()
    test_cliente_pedido()
    print("\n Todas las pruebas pasaron correctamente!")

