'''proyecto/
├── main.py
└── operaciones.py
from module
import function
module.function() se usa si no se importa con from sino solo con import'''
#Ejercicio práctico de módulos

'''mini_tienda/
├── main.py
└── operaciones.py

#operaciones.py

Escribe tres funciones:
calcular_subtotal(precio, cantidad)
aplicar_descuento(subtotal, descuento=0)
hay_stock(stock, cantidad)

Deben hacer lo siguiente:
calcular_subtotal() → devolver precio * cantidad.
aplicar_descuento() → devolver el subtotal después de aplicar el descuento.
hay_stock() → devolver True si stock >= cantidad, si no False.

#main.py
Importa el módulo completo:
import operaciones

precio = 500
cantidad = 2
stock = 5
descuento = 0.10

El programa debe calcular y mostrar algo parecido a:

Subtotal: 1000
Total con descuento: 900.0
Stock disponible: True

La condición importante es que en main.py debes llamar las funciones así:

operaciones.nombre_de_la_funcion(...)
'''