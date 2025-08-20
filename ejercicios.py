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

lista_productos = []

while True:
    print("\n Añade un producto")
    nombre = input("Ingrese el nombre del producto: ")
    precio = int(input("Ingrese el precio del producto: "))
    disponibilidad = int(input("Ingrese la disponibilidad del producto: "))

    producto = Producto(nombre, precio, disponibilidad)
    lista_productos.append(producto)

    opcion = input("¿Desea agregar más productos? (si/no): ").lower()
    if opcion == "si":
        print("Agregue el producto")
    elif opcion == "no":    
        break
    else:
        print("Opcion no válida")

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
"""

#Quieres simular un sistema bancario sencillo. Cada cliente debe poder tener un número de cuenta, un titular y un saldo. 
# El sistema debe permitir depositar dinero, retirar dinero (si hay suficiente), y consultar el saldo.
"""
class clientes:
    def __init__(self, numero, titular, saldo):
        self.numero = numero
        self.titular = titular 
        self.saldo = saldo

    def retiros(self, numero, retiro, lista):
        for cuenta in lista:
            if cuenta.numero == numero:
                if retiro <= cuenta.saldo:
                    cuenta.saldo = cuenta.saldo - retiro
                    print("Retiro exitoso")
                else:
                    print("Saldo insuficiente")

    def deposito_dinero(self, deposito):
        if deposito <= self.saldo:
            self.saldo = self.saldo + deposito
        
Lista_titulares = []
titulares_cantidad = int(input("Ingrese la cantidad de titulares que desea agregar"))
for cantidad in range (0,titulares_cantidad):
    print("\n Agrega personas: ")
    numero = int(input("Ingrese el numero de la cuenta: "))
    titular = input("Ingrese le nombre del titular: ") 
    saldo = int(input("Ingrese el saldo: "))
    titulares = clientes(numero, titular, saldo)
    Lista_titulares.append(titulares)

while True:
    print("\nQue desea hacer?")
    print("1.ingresar a mi cuenta")
    print("2.Salir")
    opcion=int(input("Que desea hacer?"))
    if opcion == 1:
        numero_cuenta = int(input("Ingrese su numero de cuenta"))
        for nc in Lista_titulares:
            if numero_cuenta == nc.numero:
             while True:
                print("\n MENÚ")
                print("1.Depositar dinero")
                print("2.Retirar dinero")
                print("3.Ver saldo")
                print("0.salir")
                opcion = int(input("Elija la opcion: "))

                if opcion == 2:
                    retirar = int(input("Ingrese monto a retirar: "))
                    titulares.retiros(numero_cuenta, retirar, Lista_titulares)
                elif opcion == 3:
                    print(f"Su saldo es de: ", titulares.saldo,"$")
                elif opcion == 1:
                    valor_depositar = int(input("Ingrese el valor a depositar en tu cuenta"))
                    titulares.deposito_dinero(valor_depositar)
                    
                elif opcion == 0:
                    break
                else:
                    print("Ingrese opcion valida")
    elif opcion == 2:
        break
    else:
        print("Ingrese opcion valida")

"""
#Forma corregida

class cliente:
    def __init__(self , numero_cuenta, titular):
        self.numero_cuenta = numero_cuenta
        self.titular = titular
        self.saldo = 0


    def depositar(self, cantidad):
        self.saldo += cantidad
        return self.saldo
    

    def reirar(self, cantidad):
        if self.saldo >= cantidad:
            self.saldo -= cantidad
            print("Retiro exitoso")
            return self.saldo
        else:
            print("Saldo insuficiente")
            return -1
        

    def consultar(self):
        return self.saldo
    


lista_cuentas = []

print("BIENVENIDO")
while True:
    print("\nQue desea hacer?")
    print("1. Registrar cuenta")
    print("2. Depsoitar")
    print("3. Retirar")
    print("4. Ver saldo")
    print("0. Salir")

    opcion = int(input())

    if opcion == 1:
        nombre = input("Ingrese el nombre del titular: ")
        numero_cuenta = int(input("Ingrese el numero de la cuenta: "))
        nueva_cuenta = cliente(nombre, numero_cuenta)
        lista_cuentas.append(nueva_cuenta)
        print("Cuenta agregada correctamente")


    elif opcion == 2:
        numero_cuenta = int(input("Ingrese el numero de la cuenta: "))
        existe = False
        for cuenta in lista_cuentas:
           if cuenta.numero_cuenta == numero_cuenta:
               existe = True
               cantidad = float("Ingrese la cantidad a depositar: ")
               nuevo_saldo = cuenta.depositar(cantidad)
               print("El nuevo saldo es", nuevo_saldo)
        if existe == False:
            print("Cuenta inexistente")
           

    elif opcion == 3:
        numero_cuenta = int(input("Ingrese el numero de la cuenta: "))
        existe = False
        for cuenta in lista_cuentas:
           if cuenta.numero_cuenta == numero_cuenta:
               existe = True
               cantidad = float("Ingrese la cantidad a retirar: ")
               nuevo_saldo = cuenta.retirarr(cantidad)
               print("El nuevo saldo es", nuevo_saldo)

               if nuevo_saldo >= 0:
                   print("Retiro exitoso. Su nuevo saldo es", nuevo_saldo)
        if existe == False:
            print("Cuenta inexistente")

    elif opcion == 4:
        numero_cuenta = int(input("Ingrese el numero de la cuenta: "))
        existe = False
        for cuenta in lista_cuentas:
           if cuenta.numero_cuenta == numero_cuenta:
               existe = True
               print("Su saldo es", cuenta.consultar())

        if existe == False:
            print("Cuenta inexistente")

    elif opcion == 0:
        print("Hasta luego")
        break

    else:
        print("Ingrese opcion valida")


            
        


            
    
                


            
        











    

