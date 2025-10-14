import pytest
from modelos import Producto , Cliente, LineaFactura
from excepciones import ProductosError, ClientesErro


def test_producto_cree_correctamente():
    p = Producto(1, "Manzana", "Alimentos", 2500)
    assert p.codigo == 1