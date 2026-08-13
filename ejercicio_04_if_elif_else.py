#and, or, not
usuario = {
    "nombre": "Miguel",
    "edad": 22,
    "premium": False,
    "bloqueado": False
}
if (usuario["edad"] >= 18 and not usuario["bloqueado"]):
    if usuario["premium"]:
        print("Acceso premium")
    else:
        print("Acceso estándar")
elif usuario["edad"] < 18:
    print("Acceso denegado")            
else:
    print("Cuenta Bloqueada")

#codigo correcto
'''if usuario["bloqueado"]:
    print("Cuenta bloqueada")

elif usuario["edad"] >= 18:
    if usuario["premium"]:
        print("Acceso premium")
    else:
        print("Acceso estándar")

else:
    print("Acceso denegado")'''