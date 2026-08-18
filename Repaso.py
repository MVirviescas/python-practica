#1 Operaciones básicas 
a = 15
b = 4

print(a + b)
print(a - b)
print(a * b)
print(a/b)
print(int(a / b))

nombre = 'Miguel'
edad = 34
altura = 1.77
estudia_python = True

#2 Variables y tipos
print(type(nombre))
print(type(edad))
print(type(altura))
print(type(estudia_python))

#3 input() y conversiones
nombre_usuario = input('Cual es su nombre?: ')
edad_usuario = input('Cuantos años tiene?: ')

print(f'Hola {nombre_usuario}, el próximo año tendras {edad_usuario}.')

#4 f-strings
producto = "Monitor"
precio = 350
cantidad = 2

print(f'Compraste {cantidad} {producto} por un total de ${precio * cantidad}')

#5 Condicional simple
edad_participante = int(input('Cual es tu edad?: '))

if edad_participante >= 18:
    print('Eres mayor de edad')
else:
    print('Eres menor de edad')
    
#6 if/elif/else
nota = int(input('Ingresa tu nota: 0 a 100: '))
if nota >= 90:
    print('Excelente')
elif nota >= 70 and nota <= 89:
    print('Aprobado')
elif nota >= 60 and nota <= 69:   
    print('Puedes mejorar')
else:
    print('Reprobado')    
    
#7 Operadores lógicos
edad_conductor = int(input('Cuantos años tienes?: '))
licencia = True 

if edad_conductor >= 18 and licencia == True:
    print('Puede conducir')
else:
    print('No puede conducir')
    
#8 Listas
productos = ["Xbox", "Monitor", "Mouse", "Teclado"]
print(productos[0])
print(productos[-1])
productos.append('Laptop')
productos.remove('Mouse')
print(productos)  

#9 Ciclo for
precios = [100, 250, 80, 500]