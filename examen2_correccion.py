from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import List

class PedidoInvalidadoError(Exception):...

@dataclass
class Lineapedido:
    descripcion: str
    cantidad: int
    peso_unitario: float

class Pedido:
    def __init__(self):
        self.lineas = List[Lineapedido] = []
    
    def agregar_lineas(self, desc, cantidad, peso):
        linea = Lineapedido(desc, cantidad, peso)
        self.lineas.append(linea)

    def calcular_total(self):
        return sum(l.cantidad for l in self.lineas)
    
    def calcular_peso(self):
        return sum(l.cantidad * l.peso_unitario for l in self.lineas)
    

class Transporte(ABC):
    def __init__(self, capacidad, velocidad, costo_base):
        self.capacidad = capacidad
        self.velocidad = velocidad
        self.costo_base = costo_base

    @abstractmethod
    def calcular_tiempo(self,velocidad, distancia):
        ...

    @abstractmethod
    def calcular_costo(self, distancia, peso):
        ...
    
    @abstractmethod
    def soporta(self):
        ...

class Bicicleta (Transporte):
    def calcular_tiempo(self, distancia):
        return distancia/self.velocidad
    
    def calcular_costo(self, distancia, peso):
        ...
    
    def soporta(self, peso):
        if peso <= 15:
            return True
        else: 
            return False
        

class Moto (Transporte):
    def calcular_tiempo(self, distancia):
        return distancia/self.velocidad
    
    def calcular_costo(self, distancia, peso):
        ...
    
    def soporta(self, peso):
        if peso <= 50:
            return True
        else: 
            return False


class Furgoneta (Transporte):
    def calcular_tiempo(self, distancia):
        return distancia/self.velocidad
    
    def calcular_costo(self, distancia, peso):
        ...
    
    def soporta(self,peso):
        return True

@dataclass
class GestordeEnvio:
    listaTransporte = []

    def registrar_transporte(self, transporte):
        self.listaTransporte.append(transporte)
        with open("transportes.txt", "a") as f:
            f.write(f'{transporte.capacidad}, {transporte.velocidad}, {transporte.costo_base}')
        
    def cargar_medios_de_transporte(self):
        with open ("transportes.txt", "r") as f:
            for linea in f:

                linea = f.read()
                linea = linea.strip().split(",")
                if linea[0] == "Bicicleta":
                    self.listaTransporte.append(Bicicleta(int(linea[1]), int(linea[2]), int(linea[3])))
                if linea[0] == "Moto":
                    self.listaTransporte.append(Moto(int(linea[1]), int(linea[2]), int(linea[3])))
                if linea[0] == "Furgoneta":
                    self.listaTransporte.append(Furgoneta(int(linea[1]), int(linea[2]), int(linea[3])))


    def asignar(self, pedido, distancia, estrategia="cualquiera"):
        peso = pedido.calcular_peso()
        if peso <= 0 or distancia <= 0:
            raise PedidoInvalidadoError("Distancia y peso deben ser mayores a 0")
        
        candidatos = [t for t in self.transportes if t.soporta(peso) == True]

        if estrategia == "cualquiera":
            elegido = candidatos[0]
        else: 
            elegido = min(candidatos, key=lambda t: t.calcular_costo(distancia, peso))

        return elegido
    
bicicleta = Bicicleta(15, 10, 2000)
moto = Moto(50, 50, 5000)
furgoneta = Furgoneta(500, 60, 10000)

gestor = GestordeEnvio()
gestor.registrar_transporte(furgoneta)
gestor.registrar_transporte(moto)
gestor.registrar_transporte(bicicleta)

pedido = Pedido()
pedido.agregar_lineas("Arepas", 5, 0.5)
pedido.agregar_lineas("Gaseosa", 6, 0.7)

print(gestor.asignar(pedido, 5, "mas barato"))
