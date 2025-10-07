x4telefono = input("Introduce un número de teléfono con el formato +34-número-extensión: ")

x4partes = x4telefono.split('-')

if len(x4partes) == 3:
    x4numnoext = x4partes[1]
    print("Número sin prefijo ni extensión:", x4numnoext)
else:
    print("Formato incorrecto.")
