
from dataclasses import dataclass ,field, asdict
from typing import List
import operaciones

@dataclass (frozen=True)

class Persona:
    nombre: str
    edad: int = field(default=35)

    def retornar_edad_por_2(self) -> int:
        return self.edad *2
    
@dataclass
class puesto:
    nombre: str

    persona:Persona

class Persona2:
    def __init__(self, nombre, edad = 35):
        self.nombre = nombre
        self.edad = edad
        
p2 = Persona2("juan", 36)
p1 = Persona("juan")

puesto1 = puesto("Desarrolador", p1)

print(operaciones.suma(p1.edad,p2.edad))

print(p1)
print(p1.nombre)

print(asdict(puesto1))

if p1 == p2:
    print("son iguales")

else:
    print("son diferentes")


@dataclass
class Grupo:
    personas: List[Persona] = field(default_factory=list)


grupo1 = Grupo()
grupo1.personas.append(p1)

grupo1.personas.append(p2)

print(grupo1)