"""class Animal:
    def __init__(self, nombre):
        self.nombre= nombre


    def hacer_sonido(self):
        pass


    def orinar(self):
        print(f"{self.nombre} esta orinando")

    
class Perro(Animal):
    def  __init__(self, nombre, color_pelota):
        super().__init__(nombre)
        self.color_pelota = color_pelota
    def hacer_sonido(self):
        print(f"{self.nombre} hace guau guau")

    def salir_a_pasear(self):
        print(f"{self.nombre} está paseando")


class Gato(Animal):
    def hacer_sonido(self):
        print(f"{self.nombre} hace miau miau")


animal1 = Perro("mia", "Rojo")
animal1.hacer_sonido()
animal1.salir_a_pasear()
animal1.orinar()
    
animal2 = Gato("Milú")
animal2.hacer_sonido()
animal2.orinar()



print(isinstance(animal1, Perro))
print(isinstance(animal1, Animal))

print(issubclass(Perro, Gato))
print(issubclass(Gato, Animal))
"""
class Persona:
    def __init__(self, nombre):
        self.nombre = nombre

    def hablar(self):
        print(f"{self.nombre} esta hablando")


class Estudiante(Persona):
    def __init__(self, nombre, carrera):
        super().__init__(nombre)
        self.carrera = carrera

    def estudiando (self):
        print(f"{self.nombre} esta estudiando {self.carrera}")


persona1= Persona("juan")
persona1.hablar()

persona2 = Estudiante("emma", "ing sistemas")
persona2.estudiando()