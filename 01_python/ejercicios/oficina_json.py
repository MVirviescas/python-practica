import json

with open("usuarios.json", "r") as archivo:
    datos = json.load(archivo)

datos["usuarios"][0]["edad"] = 29
datos["usuarios"].append({"nombre": "Ana", "edad": 25})

with open("usuarios.json", "w") as archivo:
    json.dump(datos, archivo)
    
# json.dump(datos, archivo, indent=4)

# si quieres guardar correctamente caracteres como á, é, í, ó, ú, ñ  use ensure_ascii=False    