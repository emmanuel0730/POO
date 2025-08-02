"""
class Estudiantes:
    def __init__(self, nombre, edad, n1,n2,n3):
        self.nombre = nombre
        self.edad = edad
        self.n1 = n1
        self.n2 = n2
        self.n3 = n3
    
    def mostrar_datos(self):
        print("Nombre: ", self.nombre)
        print("Edad: ", self.edad)
        print("Nota 1: ", self.n1)
        print("Nota 2: ", self.n2)
        print("Nota 3: ", self.n3)

    def promedio(self):
        promedio = (self.n1 + self.n2 + self.n3) / 3
        return promedio


print("Bienvenido a notas y servicios UDEM")
print("Ingrese el nombre del estudiante")
nombre = input()
print("Ingrese la edad del estudiante")
edad = int(input())
print("Ingrese la primera nota")
n1 = float(input())
print("Ingrese la segunda nota")
n2 = float(input())
print("Ingrese la tercera nota")
n3 = float(input())

estudiante = Estudiantes(nombre,edad,n1,n2,n3)

promedio_estudiante = estudiante.promedio()
print("El promedio de", estudiante.nombre,"es", promedio_estudiante)

#otra forma

class Estudiantes:
    def __init__(self, nombre, edad, n1,n2,n3):
        self.nombre = nombre
        self.edad = edad
        self.n1 = n1
        self.n2 = n2
        self.n3 = n3
    
    def mostrar_datos(self):
        print("Nombre: ", self.nombre)
        print("Edad: ", self.edad)
        print("Nota 1: ", self.n1)
        print("Nota 2: ", self.n2)
        print("Nota 3: ", self.n3)

    def promedio(self):
        promedio = (self.n1 + self.n2 + self.n3) / 3
        return promedio
    
print("Bienvenido a notas y servicios UDEM")
lista_estudiantes= []
while True:
    print("Seleccione la opcion deseada")
    print("1. Agregar estudiante")
    print("2. Mostrar info de estudiante")
    print("0. salir")
    opcion = int(input())
    if opcion == 1:
        print("Ingrese el nombre del estudiante")
        nombre = input()
        print("Ingrese la edad del estudiante")
        edad = int(input())
        print("Ingrese la primera nota")
        n1 = float(input())
        print("Ingrese la segunda nota")
        n2 = float(input())
        print("Ingrese la tercera nota")
        n3 = float(input())
        estudiante = Estudiantes(nombre,edad,n1,n2,n3)
        lista_estudiantes.append(estudiante)
    elif opcion == 2:
        numero_estudiantes = len(lista_estudiantes)
        print("El numero de estudiantes es: ", numero_estudiantes)
        for estudiante in lista_estudiantes:
            print("El nombre del estudiante es:", estudiante.nombre)
            print("El promedio del estudiante es: ", estudiante.promedio())
    elif opcion == 0:
        print("Hasta luego")
        break
    else:
        print("Opcion no valida")
"""
# Una tienda quiere llevar el control de los productos que vende. Por cada producto, necesita guardar el nombre, el precio y la cantidad disponible.
# El sistema debe permitir vender cierta cantidad de productos y mostrar cuántas unidades quedan.
# Si no hay suficientes unidades, debe mostrar un mensaje de advertencia.
"""
class productos:
    def __init__(self, nombre, precio, disponibilidad):
        self.nombre = nombre
        self.precio = precio
        self.disponibilidad = disponibilidad

    def ventas(self):
        disponibilidad_producto = self.disponibilidad - cantidad_a_comprar
        return disponibilidad_producto
    
print("Añade productos")
Lista_productos = []
print("Ingrese el nombre del productos")
nombre = input()
print("Ingrese el precio del producto")
precio = int(input())
print("Ingrese la disponibilidad del producto")
disponibilidad = int(input())
producto = productos(nombre, precio, disponibilidad)
Lista_productos.append(producto)

while True:
    print("\n menú")
    print("1.Comprar")
    print("2.Salir)")
    opcion = input("Que desea hacer?")
    if opcion == 1:
        for producto in Lista_productos:
            print("Nombre del producto: ",producto.nombre,"Precio: ",producto.precio, "Disponibilidad: ",producto.disponibilidad)

cantidad_a_comprar = int(input("Ingrese la cantidad que desee comprar del producto: "))
"""

class Producto:
    def __init__(self, nombre, precio, disponibilidad):
        self.nombre = nombre
        self.precio = precio
        self.disponibilidad = disponibilidad

    def vender(self, cantidad):
        if cantidad <= self.disponibilidad:
            self.disponibilidad -= cantidad
            print(f" Compra exitosa. Quedan {self.disponibilidad} unidades de '{self.nombre}'.")
        else:
            print(f"No hay suficiente disponibilidad. Solo hay {self.disponibilidad} unidades.")

# Crear lista de productos
lista_productos = []

while True:
    print("\n Añade un producto")
    nombre = input("Ingrese el nombre del producto: ")
    precio = int(input("Ingrese el precio del producto: "))
    disponibilidad = int(input("Ingrese la disponibilidad del producto: "))

    producto = Producto(nombre, precio, disponibilidad)
    lista_productos.append(producto)

    opcion = input("¿Desea agregar más productos? (si/no): ").lower()
    if opcion != "si":
        break

# Menú de opciones
while True:
    print("\n Menú")
    print("1. Comprar")
    print("2. Salir")
    opcion = input("¿Qué desea hacer? ")

    if opcion == "1":
        print("\n Productos disponibles:")
        contador = 0
        for producto in lista_productos:
            print(f"{contador + 1}. {producto.nombre} - Precio: {producto.precio} - Disponibilidad: {producto.disponibilidad}")
            contador += 1

        Producto_a_comprar = int(input("Ingrese el número del producto que desea comprar: "))
        if 0 <= Producto_a_comprar < len(lista_productos):
            cantidad = int(input("¿Cuántas unidades desea comprar? "))
            lista_productos[Producto_a_comprar - 1].vender(cantidad)
        else:
            print("Producto no válido.")
    elif opcion == "2":
        print("Gracias por usar el sistema.")
        break
    else:
        print(" Opción no válida.")

    











    

