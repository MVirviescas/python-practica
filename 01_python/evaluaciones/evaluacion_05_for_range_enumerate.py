"""Escribe un programa que recorra todos los productos y:

imprima el índice y nombre de cada producto;
si stock > 0, imprima "Disponible";
si stock == 0, imprima "Agotado";
cuente cuántos productos están agotados;
al final imprima Productos agotados: X"""

productos = [
    {"nombre": "Xbox", "precio": 500, "stock": 3},
    {"nombre": "Monitor", "precio": 250, "stock": 0},
    {"nombre": "Mouse", "precio": 50, "stock": 8},
    {"nombre": "Teclado", "precio": 80, "stock": 0}
]

for i, producto in enumerate(productos):
    if producto['stock'] > 0:
        print(f'{i}: {producto['nombre']} - Disponible')
    elif producto['stock'] == 0:
        print(f'{i}: {producto['nombre']} - Agotado')
    else:
        print('no es por aca')
        
total = 0        
for producto in productos:
    if producto['stock'] == 0:
        total += 1
    print(f'Productos agotados: {total}')

#Ahora usando un solo ciclo for
inventario = 0
for i, producto in enumerate(productos):
    if producto['stock'] > 0:
       print(f"{i}: {producto['nombre']} - Disponible")
    else:
        print(f"{i}: {producto['nombre']} - Agotado")
        inventario += 1
        
print(f"Productos agotados: {inventario}")
            