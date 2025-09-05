class Personas:
    def __init__(self, nombre, cedula, ti):
        self.nombre = nombre
        self.__cedula = cedula
        self.__ti = ti

    def obtener_documneto(self):
        if self.__cedula is not None:
            return self.__cedula
        else:
            return self.__ti



persona1 = Personas("Juan", 111, None)
persona2 = Personas("Maria",222, None)
niño1 = Personas("Pedro",None, 333)

print(persona1.nombre)
print(persona1.obtener_documneto())
print(niño1.nombre)
print(niño1.obtener_documneto())
print(persona2.nombre)
                                              