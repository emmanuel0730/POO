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
"""
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
    


    











    

