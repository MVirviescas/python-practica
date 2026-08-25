#1
numero = 5

while numero > 2:
    print(numero)
    numero -= 1

print(f"Final: {numero}")

#2
contador = 0

while contador < 3:
    print(f"Contador: {contador}")
    contador += 1

print("Terminado")

#3 Repetir hasta que el usuario escriba algo válido.
opcion = ""

while opcion != "salir":
    opcion = input("Escribe 'salir' para terminar: ")

print("Programa terminado")

#4 while con acumuladores
numero = 1
total = 0

while numero <= 4:
    total += numero
    numero += 1

print(total)

#5 con resta 
numero = 10
total = 0

while numero >= 4:
    total += numero
    numero -= 2

print(total)