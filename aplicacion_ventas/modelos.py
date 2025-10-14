from dataclasses import dataclass, field
from typing import List , ClassVar, Set
from excepciones import ProductosError

@dataclass
class Producto:
    codigo: int
    nombre : str
    categoria: str
    precio: float

    CATEGORIAS_PERMITIDAS: ClassVar[set[str]] = {"alimentos,}", "servicios"}

    def __post_init__(self) -> None:
        try:
            prueba = float(self.precio)

        except:
            raise ProductosError("Error en el precio del producto")
        if prueba <0:
            raise ProductosError ("El precio del producto no puede ser negativo")
        
        self.categoria = self.categoria.lower()

        if self.categorias not in self.CATEGORIAS_PERMITIDAS:
            raise ProductosError(
            f"categoria no permitida: {self.categoria}.")
            f"Categorias permitidas"

@dataclass
class Cliente:
    id: int
    nombre:str
    vip:bool


@dataclass
class LineaFactura:
    producto: Producto
    cantidad : int

    @property
    def subtotal(self) -> float:

        return self.producto.precio * self.cantidad
    