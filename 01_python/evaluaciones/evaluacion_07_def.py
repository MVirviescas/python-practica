#1 
'''Ahora escribe tú una función llamada:
calcular_venta(precio, cantidad)
Debe:

calcular subtotal = precio * cantidad;
calcular un impuesto del 10%;
calcular total = subtotal + impuesto;
devolver un diccionario con las claves "subtotal", "impuesto" y "total".

Después llama la función con:

calcular_venta(200, 3)'''

def calcular_venta(precio, cantidad):
    subtotal = precio * cantidad
    impuesto = subtotal * 0.10
    total = subtotal + impuesto
    
    return {
        'subtotal': subtotal,
        'impuesto': impuesto,
        'total': total        
    }
    
venta = calcular_venta(200,3)    
#print(venta)

#2 
def crear_producto(nombre, precio, stock, descuento=0):
      descuento_final = precio * descuento
      total = precio - descuento_final 
      return {
        'nombre': nombre,
        'precio': precio,
        'stock': stock,
        'descuento': descuento,
        'precio_final': total
    }
      
producto_1 = crear_producto('Xbox', 500, 4, 0)
producto_2 = crear_producto(precio=300, stock=2, nombre='Monitor', descuento=0.2)

print(producto_1)
print(producto_2)      

# 3 Mini proyecto: sistema de ventas

# 3.1
productos = [
    {"nombre": "Xbox", "precio": 500, "stock": 5},
    {"nombre": "Monitor", "precio": 250, "stock": 3},
    {"nombre": "Mouse", "precio": 50, "stock": 10}
]

def mostrar_productos(productos):
    for i in productos:
        print(f"{i['nombre']} - ${i['precio']} - stock: {i['stock']}")
        
mostrar_productos(productos)          

#3.2

def calcular_compra(precio, cantidad, descuento=0):
    subtotal = precio * cantidad
    descuento_aplicado = subtotal * descuento    
    total = subtotal - descuento_aplicado
    return {
        "precio": precio,
        "cantidad": cantidad,
        "descuento": descuento_aplicado,
        "subtotal": subtotal,
        "total": total
    }
    
calculo_final = calcular_compra(2000,15,0.2)    
print(calculo_final)    

# 3.3 

def hay_stock(stock, cantidad):
    return stock >= cantidad
    
print(hay_stock(20,10))       