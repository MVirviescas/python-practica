import json

productos = [
    {"nombre": "Xbox", "precio": 500},
    {"nombre": "Monitor", "precio": 250}
] 

with open("productos.json", "w", encoding="utf-8") as archivo:
    json.dump(productos, archivo, indent=4, ensure_ascii=False) 
    
with open("productos.json", "r", encoding="utf-8") as archivo:
    datos = json.load(archivo)
    
    datos.append({
        "nombre": "Mouse",
        "precio": 50
    })
    
with open("productos.json", "w", encoding="utf-8") as archivo:    
    json.dump(datos, archivo, indent=4, ensure_ascii=False)
    
    print(f"Productos: {productos}") 
    print(f"datos: {datos}")