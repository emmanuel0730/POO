class perro:
    def __init__(self, nombre, raza):
        self.nombre = nombre
        self.raza = raza

    def ladrar(self):
        print("el perro que esta ladrando es: ", self.nombre)

class persona:
    def __unit__(self, nombre, edad, sexo):
        self.nombre = nombre
        self.edad = edad
        self.sexo = sexo

#VAMOS A INSTANCIAR UN OBJETO DESDE LA CLASE PERRO

mi_perrito = perro("Theo", "Golden")
print(f'El nombre de mi perrito es {mi_perrito.nombre} y es de raza {mi_perrito.raza}')

Perrito = perro("tito", "Chanda")
print(f'El nombre de tu perrito es {Perrito.nombre} y es de raza {Perrito.raza}')

nombre = input("Ingrese el nombre de su perro: ")
raza = input("Ingrese la raza de su perro: ")

otro_perrito= perro(nombre,raza)

print(f'El nombre de tu perrito es {otro_perrito.nombre} y es de raza {otro_perrito.raza}')

mi_perrito.ladrar()
Perrito.ladrar()
otro_perrito.ladrar()