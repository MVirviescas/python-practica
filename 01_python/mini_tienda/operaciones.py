#define el subtotal antes de descuento
def calcular_subtotal(precio, cantidad):
    return precio *  cantidad

#define el descuento total
def aplicar_descuento(subtotal, descuento=0):
    return subtotal - (subtotal * descuento) 

#define si el stock es mayor o igual a la cantidad solicitada por el cliente
def hay_stock(stock, cantidad):
    return stock >= cantidad

print('Esta mierda si funciona')