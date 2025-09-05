class Registro:
    def __init__(self, tipo ,cantidad, valor_unitario):
        self.tipo = tipo
        self.cantidad = cantidad
        self.valor_unitario = valor_unitario




class Factura:
    def __init__(self,codigo):
        self.codigo = codigo
        self.registros = []
        self.total = 0


    def agrgar_registro(self, tipo, cantidad ,valor_unitario):
        nuevo_registro = Registro(tipo, cantidad, valor_unitario)
        self.registros.append(nuevo_registro)
        self.total = self.total + (cantidad * valor_unitario)

    
mi_factura = Factura(1234)
mi_factura.agrgar_registro("Gaseosa",5 , 2500)
mi_factura.agrgar_registro("arepas",3 , 2500)

print("El total es", mi_factura.total)


class Registro:
    def __init__(self, tipo ,cantidad, valor_unitario):
        self.tipo = tipo
        self.cantidad = cantidad
        self.valor_unitario = valor_unitario




class Factura:
    def __init__(self,codigo):
        self.codigo = codigo
        self.registros = []
        self.total = 0


    def agrgar_registro(self, registro):
        self.registros.append(registro)
        self.total = self.total + (registro.cantidad * registro.valor_unitario)

    
mi_factura = Factura(1234)
registro1 = Registro("Gaseosa",5 , 2500)
registro2 = Registro("arepa",3 , 2500)

mi_factura.agrgar_registro(registro1)
mi_factura.agrgar_registro(registro2)

print("El total es", mi_factura.total)