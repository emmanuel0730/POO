tupla_ejemplo = (1,1,0,150,11)

import random

tupla = tuple(random.randint(1,100)for i in range(5))
print(tupla)



class libreria:
    def __init__(self, nombre):
        self.nombre = nombre
        self.libros = []
        self.ultima_venta = None


    def agregar_libro(self,nombre_libro):
        for i in range (0, len(self.libros)):
            print("El libro numero", i ,"es", self.libros[i])
      

    def registrar_venta(self, cliente, total):
        self.ultima_venta = (cliente,total)


print("Bienvenido al programa")
librerias = []
while True:
    print("Seleccine la opcion deseada: ")
    print("1. crear libreria: ")
    print("2.Agregar un libro a una libreria ")
    print("3. mostrar libros de una libreria ")
    opcion = int(input())
    if opcion == 1:
        nombre = input("Ingrese le nombre de la libreria").lower()
        neuva_libreria = libreria(nombre)
        librerias.append(neuva_libreria)

    elif opcion == 2:
        nombre = input("Ingrese le nombre de la libreria")
        existe = False 
        for libria in librerias:
            if libreria.nombre == nombre:
                existe = True
                nombre_libro = input("Ingrese le nombre del libro")
                libreria.agregar_libro(nombre_libro)
        if existe == False:
            print("Esta libreria no existe")
    if opcion ==3:
        nombre = input("Ingrese le nombre de la libreria")
        existe = False 
        for libria in librerias:
            if libreria.nombre == nombre:
                existe = True
                libreria.mostrar_librp
