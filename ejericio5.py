class Dispositivo:
    def __init__(self, nombre):
        self.nombre = nombre
        self.estado = False

    def encender(self):
        self.estado = True
        print(self.nombre, "Encendido")

    def apagar(self):
        self.estado = False
        print(self.nombre, "Apagado")

class Espacio:
    def __init__(self, nombre):
        self.nombre = nombre
        self.__dispositivos = []


    def agregar_dispositivo(self, dispositivo):
        self.__dispositivos.append(dispositivo)
        print("Dispositivo agregado")

    def mostrar_dispositivo(self):
        for dispositivo in self.__dispositivos:
            print(dispositivo.nombre)
        
class casa:
    def __init__(self, direccion):
        self.direccion = direccion
        self.__lista_espacios = []


    def agregar_espacio(self, nombre):
        self.__lista_espacios.append(Espacio(nombre))
        print("Espacio agregado")


    def buscar_espacio(self,nombre):
        for espacio in self.__lista_espacios:
            if espacio.nombre == nombre:
                return espacio
        return None


    def mostrar_espacio(self):
        for espacio in self.__lista_espacios:
            print(espacio.nombre)


mi_casa = casa("Calle 12")
mi_casa.agregar_espacio("Cocina")
mi_casa.agregar_espacio("Baño")
mi_casa.agregar_espacio("Habitacion")
mi_casa.mostrar_espacio()
tv = Dispositivo("Tv")
mi_casa.buscar_espacio("Habitacion").agregar_dispositivo(tv)
mi_casa.buscar_espacio("Habitacion").mostrar_dispositivo()