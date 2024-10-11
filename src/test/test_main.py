# from src.main import sum
# from src.main import rest
# from src.main import multiplicacion
# from src.main import division
# from src.main import Opera_Combi
# from src.main import negativos
# from src.main import entrada_no_numerica
# from src.main import division0
# from src.main import decimales
# from src.main import interfaz

# def test_sum ():
#     assert sum (5,3)==8

# def test_rest ():
#     assert rest (10,4) == 6

# def test_rest ():
#     assert rest (10,4) == 6

# def test_multi ():
#     assert multiplicacion (7, 6) == 42

# def test_divi ():
#     assert division (20, 5) == 4

# def test_combi ():
#     assert Opera_Combi (2, 3, 4) == 2

# def test_negativos ():
#     assert negativos(-5, 3) == -2

# def test_nnumber ():
#     assert entrada_no_numerica("abc", 5) =="Error: Entrada no válida"

# def test_d0 ():
#     assert division0(10, 10) == 0

# def test_decimales ():
#     assert decimales(7.5, 2.2) == 5.3

# def test_interfaz ():
#     assert interfaz(8, 3) == 24

# from src.main import par

# def test_par():
#     assert par(4) == True
#     assert par(7) == False
#     assert par(0) == True
#     assert par(-2) == True

# from src.main import calcular_edad
# from datetime import datetime

# def test_calcular_edad():
#     assert calcular_edad("2000-01-01") == 24
#     assert calcular_edad("2024-01-01") == 0
#     assert calcular_edad("1990-09-28") == (datetime.today().year - 1990)

# from src.main import generar_id

# def test_generar_id():
#     id1 = generar_id()
#     id2 = generar_id()
#     assert len(id1) == 8
#     assert id1.isalnum()
#     assert id1 != id2

# from src.main import ordenar_por_longitud

# def test_ordenar_por_longitud():
#     assert ordenar_por_longitud(["perro", "gato", "elefante"]) == ["gato", "perro", "elefante"]
#     assert ordenar_por_longitud(["sol", "estrella", "luna"]) == ["sol", "luna", "estrella"]
#     assert ordenar_por_longitud([]) == []
#     assert ordenar_por_longitud(["sol", "sol", "sol"]) == ["sol", "sol", "sol"]

# from src.main import Carrito

# def test_carrito():
#     carrito = Carrito()
#     carrito.agregar_producto("Producto1", 100)
#     carrito.agregar_producto("Producto2", 50)
    
#     assert carrito.calcular_total() == 150
#     assert carrito.calcular_total(10) == 135
#     assert carrito.calcular_total(50) == 75
#     assert carrito.calcular_total(0) == 150
#     assert carrito.calcular_total(100) == 0

# from src.main import Inventario

# def test_inventario():
#     inventario = Inventario()
#     inventario.agregar_producto(1, "Producto1", 10)
    
#     assert inventario.consultar_producto(1) == {"nombre": "Producto1", "cantidad": 10}
    
#     inventario.actualizar_stock(1, 20)
#     assert inventario.consultar_producto(1)["cantidad"] == 20
    
#     inventario.eliminar_producto(1)
#     assert inventario.consultar_producto(1) is None

# from src.main import calcular_descuento
# import pytest

# def test_calcular_descuento():
#     assert calcular_descuento(100, 10) == 90
#     assert calcular_descuento(100, 0) == 100
#     assert calcular_descuento(100, 100) == 0
#     with pytest.raises(ValueError):
#         calcular_descuento(0, 10)
#     with pytest.raises(ValueError):
#         calcular_descuento(100, 150)

# from src.main import SistemaAutenticacion
# import pytest

# def test_autenticacion():
#     auth = SistemaAutenticacion()
#     auth.registrar_usuario("user1", "pass1")
    
#     assert auth.iniciar_sesion("user1", "pass1") == True
#     with pytest.raises(ValueError):
#         auth.iniciar_sesion("user1", "wrong_pass")

# from src.main import Tarea

# def test_tarea():
#     tarea = Tarea("Tarea 1", "2024-10-01")
#     assert tarea.completada == False
    
#     tarea.completar()
#     assert tarea.completada == True

from src.main import Reserva

def test_reserva():
    reserva = Reserva()
    reserva.crear_reserva("2024-10-10", "20:00", 4)
    
    assert ("2024-10-10", "20:00", 4) in reserva.reservas
    
    reserva.cancelar_reserva("2024-10-10", "20:00")
    assert ("2024-10-10", "20:00", 4) not in reserva.reservas













