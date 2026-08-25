'''#1 Operaciones básicas 
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
if nota >= 90 and nota <= 100:
    print('Excelente')
elif nota >= 70 and nota <= 89:
    print('Aprobado')
elif nota >= 60 and nota <= 69:   
    print('Puedes mejorar')
elif nota > 100:
    print('Por favor revisa el número ingresado')    
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
precio_total = 0

for precio in precios:
    print(precio)
    precio_total += precio
    
print(precio_total)    

#10 for + condición    
numeros = [3, 8, 12, 5, 20, 7]

for numero in numeros:
    if numero > 10:
        print(numero)
    else:
        None
        
#11 break
productos = ["Xbox", "Monitor", "Mouse", "Teclado", "Laptop"]

for i in productos:
    if i == 'Mouse':
        break

print('llegamos a Mouse y por eso se detuvo') 
print(productos)   

#12 continue
for i in productos:
     if i == 'Mouse':
         continue       \

print('Mouse no se imprime')    
print(productos)

#13 while basico
numero = 1
while numero <= 5:
    print(numero)
    numero += 1
    
#14 while con acumulador
while numero <= 5:
    numero += 1
    total += numero 

print(total)'''

'''#15 operadores numericos
a = 17
b = 5

print(a / b)  #division normal
print(a // b) #division y se queda con el cociente entero
print(a % b) #es lo que sobra al divividir. ej si 17 % 5 > 3 y sobra 2. 2 es el residuo
print(a ** 2) #representa la potencia. por ej. 3 a la 2 = 3 * 3 = 9 // o 2 a la 3 = 2*2*2 = 8 '''
# mezcla while, acumulador, estado de variables, continue, break y condiciones.
numero = 1
total = 0

while numero <= 6:

    if numero == 3:
        numero = numero + 1
        print(numero)
        print(total)
        continue

    total = total + numero

    if total >= 8:
        print(numero)
        print(total)
        break

    numero = numero + 1

print("Numero:", numero)
print("Total:", total)