#1
precios = [100, 250, 80]

for precio in precios:
    precio_con_impuesto = precio * 1.10
    print(precio_con_impuesto)

#2
numeros = [5, 10, 15]

for numero in numeros:
    doble = numero * 2
    print(f"{numero} x 2 = {doble}")    
  
#3    
productos = [
    {"nombre": "Xbox", "precio": 500},
    {"nombre": "Monitor", "precio": 250},
    {"nombre": "Mouse", "precio": 50}
]

for producto in productos:
    print(f"{producto['nombre']}: ${producto['precio']}")
    
