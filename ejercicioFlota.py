class motor:
    def __init__(self):
        self.estado = False

    def encender_motor(self):
        self.estado = True
        print("El motor esta encendido")

    def apagar_motor(self):
        self.estado = False
        print("El motor esta apagado")
    

class carro:
    def __init__(self,marca, placa, tipo, estado):
        self.marca = marca
        self.placa = placa
        self.tipo = tipo
        self.estado = estado
        self.motor = motor()
    

class Flota:
    def __init__(self, nombre):
        self.nombre = nombre
        self.lista_carros = []


    def agregar_carro(self, carro):
        self.lista_carros.append(carro)
        print("El carro fue agregado correctamente")

    def eliminar_carro(self, placa):
        for p in self.lista_carros:
            if placa == p.placa:
                self.lista_carros.remove(p)
        print("El carro fue eliminado correctamente")

    def mostrar_carros(self):
        print("Carros:\n")
        contador = 0
        for carro in self.lista_carros:
            print(f"{contador + 1}. Marca: {carro.marca}-- Placa: {carro.placa}-- Tipo: {carro.tipo}-- Estado: {carro.estado}")
            contador += 1

    def totales(self):
        print("El total de carros es: ",len(self.lista_carros))


    def buscarPorPlaca(self, placa):
        for placa1 in self.lista_carros:
            if placa1.placa == placa:
                return 1 
        return 0



flota1 = Flota("Autoland")
C1 = carro("Mazda","123","Sedan","disponible")
C2 = carro("toyota","12","Camioneta","no disponible")
flota1.agregar_carro(C1)
flota1.agregar_carro(C2)



while True:
    print("\nBienvenido a la flota")
    print("Elija lo que quiera hacer")
    print("1. Agregar carro") 
    print("2. Eliminar carro") 
    print("3. mostrar carros") 
    print("4. Mostrar total de carros")
    print("5. Buscar carro por placa ")
    print("6. Encender motor")
    print("7. Apagar motor")  
    opcion = int(input())    

    if opcion == 1:
        marca = input("ingrese la marca del carro: ")   
        placa = input("Ingrese la placa del carro: ")
        tipo = input("Ingrese el tipo de vehiculo: ")
        estado = "Disponible"
        nuevo_carro = carro(marca,placa,tipo,estado) 
        flota1.agregar_carro(nuevo_carro) 

    elif opcion == 2:
        carro_eliminar = input("Ingrese la placa del carro que desee eliminar: ")
        flota1.eliminar_carro(carro_eliminar)


    elif opcion == 3:
        flota1.mostrar_carros()

    elif opcion == 4:
        flota1.totales()

    elif opcion == 5:
        carro_buscar = input("Ingrese la placa del carro que desee buscar: ")
        flota1.buscarPorPlaca(carro_buscar)
        if flota1.buscarPorPlaca(carro_buscar) == 1:
            print("Existe el carro")
        elif flota1.buscarPorPlaca(carro_buscar) == 0:
            print("No existe el carro")

    elif opcion == 6:
        motor_encender = input("Ingrese la placa del vehiculo que desea encender: ")
        flota1.buscarPorPlaca(motor_encender)
        if flota1.buscarPorPlaca(motor_encender) == 1:
            flota1.lista_carros[flota1.buscarPorPlaca(motor_encender)].motor.encender_motor()
        elif flota1.buscarPorPlaca(motor_encender) == 0:
            print("Carro no encontrado")

    


    
        

 
           
"""flota1 = Flota("Autoland")
C1 = carro("Mazda",123,"Sedan","disponible")
C2 = carro("toyota",12,"Camioneta","no disponible")
flota1.agregar_carro(C1)
flota1.agregar_carro(C2)
flota1.eliminar_carro(C2)

flota1.mostrar_carros()"""
