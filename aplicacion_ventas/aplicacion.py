from modelos import Producto, Cliente
from pedido import Factura
from descuentos import DescuentoVIP, DescuentoVolumen , DescuentoCompuesto , SinDescuento
from impuestos import IVA, Excentos


cliente = Cliente(123, "juan", True)

producto1 = Producto(567, "Arepas","alimentos", 2000)
producto2 = Producto(495, "sub","servicios", 25000)
producto3 = Producto(123, "Pcerdo","tecnologia", 2500000)

mifactura = Factura(cliente)

mifactura.agregar_linea(producto2, 10)

descuento_a_aplicar = DescuentoCompuesto(DescuentoVIP(), DescuentoVolumen())
impuesto_a_aplicar = IVA()

print(mifactura.calcular_total(descuento_a_aplicar, impuesto_a_aplicar))