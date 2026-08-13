usuario = {
    'nombre': input('Cual es tu nombre?'),
    'edad': int(input('Cuantos años tienes?')),
    'premium': int(input("¿Es premium? 1 = Sí, 0 = No: ")),
    'bloqueado': int(input("¿Estás Bloqueado? 1 = Sí, 0 = No: "))
}

if usuario['bloqueado'] == 1:
    print(f'{usuario["nombre"]}: Cuenta bloqueada')
    
elif usuario['edad'] >= 18:
    if usuario['premium'] == 1:
        print(f'{usuario["nombre"]}: Acceso premium')
    else:
        print(f'{usuario["nombre"]}: Acceso estándar')
        
else:
    print(f'{usuario["nombre"]}: Acceso denegado')
#Sí, la lógica de tu programa está correcta y ya combina varias piezas importantes de Python: input(), conversión con int(), diccionarios, acceso por claves, if / elif / else, if anidado y f-strings.