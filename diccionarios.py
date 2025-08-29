'''   # Creamos agenda con 3 contactos

agenda = {
    "ana": "3208762398",
    "Emmanuel": "3009723618",
    "mamá": "3145289471"
}

#Mostar el numero de un contacto especifico

print ( "telefono de Emmanuel:", agenda["Emmanuel"])

nombre = input("Ingrese el nombre del contacto: ")

if nombre in agenda:
    print("Telefono de:" + nombre, agenda [nombre])
else:
    print("no está")

#Agregar cosas al diccionario

agenda ["Chirri"] = "3008765432"
nombre = input("Ingrese el nombre del contacto: ")

if nombre in agenda:
    print("Telefono de" + nombre, agenda [nombre])
else:
    print("no está")

#eliminar

del agenda["ana"] 

estudiantes = {"lucia": [4.5, 3.8, 4.2],
                "Mateo": [3.0, 3.5, 4.0, 4.2],
                "Sofia": {5.0, 4.8, 4.9}
 }

promedios = {}

for nombre, notas in estudiantes.items():
     prom = sum(notas) / len(notas)
     print(f"Promedio de {nombre}: {prom:.1f}")
     promedios[nombre] = prom

print(promedios)

mejor_estudiante = max(promedios, key=promedios.get)
print(f"Mejor estudainte es:{mejor_estudiante}") 
 
 '''

inventario = {}

while True:
    print("1. Agregar productos")
    print("2.vender productos")
    print("3. Mostrar inventario")
    print("0. Salir")
    opcion = int(input("Que desea hacer? "))
    if opcion == 1:
        nombre_producto = input("Ingrese el nombre del producto")
        cantidad_producto = int(input("ingrese la cantidad del producto"))
       

        if nombre_producto in inventario:
            inventario [nombre_producto] += cantidad_producto
        else: 
            inventario [nombre_producto] = cantidad_producto
    elif opcion == 2:
        nombreP = input("Ingrese el nombre del producto a vender")
        if nombreP in inventario:
            cantidad_vender = int(input("Ingrese la cantidad a vender del producto"))
            if inventario[nombre_producto] >= cantidad_vender:
                inventario[nombre_producto] -= cantidad_vender
                print("inventario actualizado")
            else: 
                print("Cntidad insuficiente")
    elif opcion == 3:
        print (inventario)

    elif opcion == 0:
        break
    else:
        print("ingrese opcion valida")
        
            

