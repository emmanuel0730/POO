from excepciones import pesoYDistanciaErorr
class LineaPedido:
    def __init__(self,descripcion, cantidad, peso_unitario):
        self.descripcion = descripcion
        self.cantidad = cantidad
        self.precio_unitario = peso_unitario


class Pedido:
    def __init__(self):
        pedido = LineaPedido()


class Transporte:
    def __init__(self, capacidad, velocidad, costo_base):
        self.capacidad = capacidad
        self.velocidad = velocidad
        self.costo_base = costo_base


    def calcular_tiempo(self, distancia, velocidad):
        return distancia / velocidad
    

    def calcular_costo(self):
        pass

class Bicicleta(Transporte):
    def __init__(self, capacidad, velocidad, costo_base):
        super().__init__(capacidad, velocidad, costo_base)
        self.Costo = 0
        self.costo_base = 3000

    def calcular_tiempo(self, distancia, velocidad):
        return super().calcular_tiempo(distancia, velocidad)
    
    def calcular_costo(self, distancia, peso):
        self.Costo = self.costo_base + 0.20 * distancia



class Moto(Transporte):
    def __init__(self, capacidad, velocidad, costo_base):
        super().__init__(capacidad, velocidad, costo_base)
        self.Costo = 0
        self.costo_base = 5000

    def calcular_tiempo(self, distancia, velocidad):
        return super().calcular_tiempo(distancia, velocidad)
    
    def calcular_costo(self, distancia, peso):
        self.Costo = self.costo_base + 0.60 * distancia + 0.05 * peso


class Furgoneta(Transporte):
    def __init__(self, capacidad, velocidad, costo_base):
        super().__init__(capacidad, velocidad, costo_base)
        self.Costo = 0
        self.costo_base = 10000

    def calcular_tiempo(self, distancia, velocidad):
        return super().calcular_tiempo(distancia, velocidad)
    
    def calcular_costo(self, distancia, peso):
        self.Costo = self.costo_base + 1.20 * distancia + 0.10 * peso
       

class GestorEnvios:
    def __init__(self):
        self.transportes = []

    def validar_peso_y_distancia(self, peso, distancia):
        while True:
            if 0 > peso and 0 > distancia:
                raise pesoYDistanciaErorr
            else:
                break

    def filtrar(self,peso):
        if 0 < peso <= 5:
            return self.transportes[0]  # Bicicleta
        elif 5 < peso <= 20:
            return self.transportes[1]  # Moto
        elif peso > 20:
            return self.transportes[2]  # Furgoneta
        

    def asignar(self, peso, distancia):
        self.validar_peso_y_distancia(peso, distancia)
        transporte = self.filtrar(peso)
        tiempo = transporte.calcular_tiempo(distancia, transporte.velocidad)
        costo = transporte.calcular_costo(distancia, peso)
        return transporte, tiempo, costo
    
