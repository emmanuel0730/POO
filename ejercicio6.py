class empleado:
    def __init__(self,nombre, documento , edad):
       self.__nombre = nombre
       self.__documento  = documento
       self.__edad = edad


    def mostrar_datos(self):
        return {"Nombre": self.__nombre, "Documento": self.__documento, "edad": self.__edad }
    

    def set_nombre(self, nombre):
        self.__nombre
    


class desarrollador(empleado):
    def __init__(self, nombre, documento,edad,tipo):
        super().__init__(nombre, documento, edad)
        self.__tipo = tipo


    def mostrar_datos(self):
        datos = super().mostrar_datos()
        datos["tipo"] = self.__tipo
        return datos
       
class gerente(empleado):
    def __init__(self, nombre, documento, edad, area):
        super().__init__(nombre, documento, edad)
        self.__area = area
        self.empleados_a_cargo = []


    def mostrar_datos(self):
        datos = super().mostrar_datos()
        datos["area"] = self.__area
        return datos
    

    def mostrar_personas(self):
        for empleado in self.empleados_a_cargo:
            print(empleado.mostrar_datos())


    def asiganr_empleado(self, empleado):
        self.empleados_a_cargo.append(empleado)
        

empleado2 = desarrollador("Juan", 111, 35, "Backend")
"""print(empleado2.mostrar_datos())"""


empleado1 = gerente("emma", 2222, 5 , "desarrollado")

empleado3= empleado("carlos", 333, 20)

empleado1.asiganr_empleado(empleado2)
empleado1.asiganr_empleado(empleado3)
empleado1.mostrar_personas()

print(empleado1.mostrar_datos())