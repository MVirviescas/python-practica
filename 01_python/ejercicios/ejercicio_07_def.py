def mostrar_producto(nombre, precio):
    print(f"Producto: {nombre}")
    print(f"Precio: {precio}")

mostrar_producto("Xbox", 500)
mostrar_producto("Mouse", 50)

# def mostrar_producto(nombre, precio): nombre y precio son parametros
# mostrar_producto("Xbox", 500): Xbox y 500 son argumentos que se pasan directamente por la funcion

#2 ejercicio mas complejo
def calcular_total(precio, cantidad, descuento):
    subtotal = precio * cantidad
    descuento_aplicado = subtotal * descuento
    total = subtotal - descuento_aplicado
    return total

resultado = calcular_total(100, 3, 0.10)

print(resultado)