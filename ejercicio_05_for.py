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
    
#4 for + if
productos = [
    {"nombre": "Xbox", "precio": 500},
    {"nombre": "Monitor", "precio": 250},
    {"nombre": "Mouse", "precio": 50}
]

for producto in productos:
    if producto["precio"] >= 200:
        print(f"{producto['nombre']}: Producto costoso")
    else:
        print(f"{producto['nombre']}: Producto económico")

#5 acumular valores dentro de un loop
ventas = [
    {"producto": "Xbox", "cantidad": 2},
    {"producto": "Monitor", "cantidad": 3},
    {"producto": "Mouse", "cantidad": 5}
]

total_unidades = 0

for venta in ventas:
    total_unidades = total_unidades + venta["cantidad"]

print(f"Unidades vendidas: {total_unidades}")

#6 acumular valores dentro de un loop - 2do ejemplo
ventas = [
    {"producto": "Xbox", "precio": 500, "cantidad": 2},
    {"producto": "Monitor", "precio": 250, "cantidad": 3},
    {"producto": "Mouse", "precio": 50, "cantidad": 5}
]

total_ventas = 0

for venta in ventas:
    subtotal = venta["precio"] * venta["cantidad"]
    total_ventas = total_ventas + subtotal

print(f"Total vendido: {total_ventas}")

#7 Ahora combinemos acumulación + condición
productos = [
    {"nombre": "Xbox", "precio": 500},
    {"nombre": "Monitor", "precio": 250},
    {"nombre": "Mouse", "precio": 50},
    {"nombre": "Teclado", "precio": 80}
]

total_costosos = 0

for producto in productos:
    if producto["precio"] >= 200:
        total_costosos += producto["precio"]

print(f"Total de productos costosos: {total_costosos}")

#8 Aquí ya estás combinando correctamente for, if, acceso a diccionarios y acumuladores.
#Ahora añadimos otro patrón muy común: contar elementos que cumplen una condición.
usuarios = [
    {"nombre": "Laura", "edad": 28, "premium": True},
    {"nombre": "Carlos", "edad": 17, "premium": False},
    {"nombre": "Ana", "edad": 35, "premium": True},
    {"nombre": "Pedro", "edad": 16, "premium": True}
]

mayores = 0
premium = 0

for usuario in usuarios:
    if usuario["edad"] >= 18:
        mayores += 1

    if usuario["premium"]:
        premium += 1

print(f"Mayores de edad: {mayores}")
print(f"Usuarios premium: {premium}")

#9 Ahora vamos a modificar la pregunta: queremos contar solamente usuarios que sean mayores de edad y premium al mismo tiempo.
usuarios = [
    {"nombre": "Laura", "edad": 28, "premium": True},
    {"nombre": "Carlos", "edad": 17, "premium": False},
    {"nombre": "Ana", "edad": 35, "premium": True},
    {"nombre": "Pedro", "edad": 16, "premium": True}
]

mayores_premium = 0

for usuario in usuarios:
    if usuario["edad"] >= 18 and usuario["premium"]:
        mayores_premium += 1

print(f"Mayores y premium: {mayores_premium}")

#10 Ahora añadimos range(), que se usa cuando quieres repetir algo una cantidad concreta de veces
    #ejercicio 1
for numero in range(1, 6):
    print(f"Número: {numero}")
    #ejercicio 2
total = 0

for numero in range(1, 5):
    total += numero

print(total)    

#11 Ahora vamos a usar range() junto con índices de una lista:
productos = ["Xbox", "Monitor", "Mouse"]

for i in range(len(productos)):
    print(i, productos[i])