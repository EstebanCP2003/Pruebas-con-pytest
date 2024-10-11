# def sum (x,y):
#     return x + y 

# def rest (x,y):
#     return x - y

# def multiplicacion (x,y):
#     return x * y

# def division (x,y):
#     return x / y

# def Opera_Combi (x, y, z):
#     return (x + y) * z

# def negativos(x, y):
#     return (x + y)

# def entrada_no_numerica (x, y):
#     return (x, y)

# def division0 (x, y):
#     return (x, y)

# def decimales(x, y):
#     return x - y

# def interfaz(x, y):
#     return x * y

# def par(n):
#     return n % 2 == 0

# from datetime import datetime

# def calcular_edad(fecha_nacimiento):
#     fecha_nac = datetime.strptime(fecha_nacimiento, '%Y-%m-%d')
#     hoy = datetime.today()
#     edad = hoy.year - fecha_nac.year - ((hoy.month, hoy.day) < (fecha_nac.month, fecha_nac.day))
#     return edad

# import random
# import string

# # Implementación
# def generar_id():
#     return ''.join(random.choices(string.ascii_letters + string.digits, k=8))

# def ordenar_por_longitud(lista_palabras):
#     return sorted(lista_palabras, key=len)

# class Carrito:
#     def __init__(self):
#         self.productos = []
    
#     def agregar_producto(self, nombre, precio):
#         self.productos.append((nombre, precio))
    
#     def calcular_total(self, descuento=0):
#         subtotal = sum(precio for _, precio in self.productos)
#         return subtotal - (subtotal * (descuento / 100))

# class Inventario:
#     def __init__(self):
#         self.productos = {}
    
#     def agregar_producto(self, id_producto, nombre, cantidad):
#         if id_producto in self.productos:
#             raise ValueError("Producto ya existe")
#         self.productos[id_producto] = {"nombre": nombre, "cantidad": cantidad}
    
#     def eliminar_producto(self, id_producto):
#         if id_producto not in self.productos:
#             raise ValueError("Producto no existe")
#         del self.productos[id_producto]
    
#     def actualizar_stock(self, id_producto, cantidad):
#         if id_producto not in self.productos:
#             raise ValueError("Producto no existe")
#         self.productos[id_producto]["cantidad"] = cantidad
    
#     def consultar_producto(self, id_producto):
#         return self.productos.get(id_producto, None)

# def calcular_descuento(precio, descuento):
#     if precio <= 0:
#         raise ValueError("El precio debe ser mayor que cero")
#     if not 0 <= descuento <= 100:
#         raise ValueError("El descuento debe estar entre 0 y 100")
#     return precio - (precio * (descuento / 100))

# class SistemaAutenticacion:
#     def __init__(self):
#         self.usuarios = {}
    
#     def registrar_usuario(self, username, password):
#         if username in self.usuarios:
#             raise ValueError("Usuario ya registrado")
#         self.usuarios[username] = password
    
#     def iniciar_sesion(self, username, password):
#         if username not in self.usuarios or self.usuarios[username] != password:
#             raise ValueError("Credenciales incorrectas")
#         return True

# class Tarea:
#     def __init__(self, titulo, fecha_vencimiento):
#         self.titulo = titulo
#         self.fecha_vencimiento = fecha_vencimiento
#         self.completada = False
    
#     def completar(self):
#         self.completada = True

class Reserva:
    def __init__(self):
        self.reservas = []
    
    def crear_reserva(self, fecha, hora, personas):
        self.reservas.append((fecha, hora, personas))
    
    def cancelar_reserva(self, fecha, hora):
        self.reservas = [r for r in self.reservas if r[:2] != (fecha, hora)]


















