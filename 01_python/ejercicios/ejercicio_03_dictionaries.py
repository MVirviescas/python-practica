#clave > Valor
"""producto = {
    "nombre": "Xbox",
    "precio": 500,
    "stock": 10,
    "disponible": True
}"""
"""keys()   → las claves
values() → los valores
items()  → pares clave-valor"""
#importante para tener en cuenta!
"""Lista de Diccionarios
productos = [
    {"nombre": "Xbox", "precio": 500},
    {"nombre": "Monitor", "precio": 250},
    {"nombre": "Teclado", "precio": 80}]"""
usuarios = [
    {"nombre": "Laura", "edad": 28},
    {"nombre": "Carlos", "edad": 31},
    {"nombre": "Miguel", "edad": 25}
]

usuarios[1]["edad"] = 32 #se remplaza el valor inicial de la clave 'edad' en el diccionario del indice 1
usuarios[0]["premium"] = True #añade la clave 'premium' con valor True al diccionario del indice 0 de la lista de la variable Usuario.
usuarios.append({"nombre": "Ana", "edad": 27}) #agrega un diccionario al final de la lista con las claves y valores indicadas dentro de los {}

print(usuarios[1]["edad"])
print(usuarios[0])
print(usuarios[-1]["nombre"])
print(len(usuarios))