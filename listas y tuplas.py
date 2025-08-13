"""
import random

lista_random = []
for i in range(0,10):
    lista_random.append(random.randint(1,100))
print(lista_random)

#solucion corta 
lista_random2 = [random.randint(1, 100) for _ in range(10)]
print(lista_random2)

lista_ejemplo =  [ i for i in range (0,10)]  
print(lista_ejemplo)
#cambiar elemento
lista_ejemplo[2] = 10
print(lista_ejemplo)

#quitar elemento
lista_ejemplo.remove(3)
print(lista_ejemplo)

#eliminar por posicion
del lista_ejemplo[2]
print(lista_ejemplo)


lista_ejemplo = [elemento for elemento in lista_ejemplo if elemento != 1 ]
print (lista_ejemplo)

#ordenar lista
lista_ejemplo.sort()
print(lista_ejemplo)

lista_ejemplo.reverse
print(lista_ejemplo)

lista_ejemplo.sort(reverse= True)
"""
import random
class perosnas:
    def __init__(self, nombre):
        self.nombre = nombre
        self.lista_numeros = [random.randint(100,999) for _ in range(5)]
perosna1 = perosnas("Emmanuel")
perosna2 = perosnas("pepito")
print("lso numeros para ", perosna1.nombre,"son", perosna1.lista_numeros)
print("lso numeros para ", perosna2.nombre,"son", perosna2.lista_numeros)
        


