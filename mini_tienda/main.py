import operaciones

precio = 500
cantidad = 2
stock = 5
descuento = 0.10

subtotal = operaciones.calcular_subtotal(precio,cantidad)
total_con_descuento = operaciones.aplicar_descuento(subtotal, descuento)
stock = operaciones.hay_stock(stock, cantidad)

print(f"Subtotal: ${subtotal}")
print(f"Total con descuento: ${total_con_descuento}")
print(f"Stock disponible: {stock}")