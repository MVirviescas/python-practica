nombre_cliente = input("Cual es tu nombre: ")
producto = input("Nombre del Producto: ")
precio = int(input("Cual es el precio: "))
cantidad = int(input("Cual es la cantidad: "))
descuento = int(input("Cual es el descuento: ")) / 100

subtotal = precio * cantidad 
descuento_aplicado = subtotal * descuento 
total = subtotal - descuento_aplicado

print(f"Cliente: {nombre_cliente}")
print(f"Producto: {producto}")
print(f"Cantidad: {cantidad}")
print(f"Subtotal: {subtotal}")
print(f"Descuento: {descuento_aplicado}")
print(f"Total a pagar: {total}")

#Este ejercicio es para aprender acerca de los tipos STR, INT, FLOAT. Como hacer Input y Print
