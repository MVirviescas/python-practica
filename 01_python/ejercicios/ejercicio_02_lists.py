#En este ejercicio se aprenden metodos como .append, .pop(Indice), insert(indice, "Objeto"), remplazar indice variable[indice], .remove('valor'),lista[inicio:fin], variable[-1],len(lista)
#Metodo in y not in
productos = ["Xbox", "Monitor", "Teclado"]
productos.append("Mouse")
print(productos)
productos.insert(1, "Control")
print(productos)
productos.remove('Monitor')
print(productos)
producto_eliminado = productos.pop()
print(producto_eliminado)
productos[0] = 'PlayStation'
print(productos)
print('Teclado' in productos)
#Con este ejercicio ya demostraste manejo básico sólido de listas: acceso por índice, modificación, append(), insert(), remove(), pop(), len(), slicing e in.