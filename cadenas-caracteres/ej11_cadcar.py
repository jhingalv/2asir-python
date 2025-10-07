x11nombre = input("Nombre del producto: ")
x11precio = float(input("Precio unitario: "))
x11unidades = int(input("Número de unidades: "))

x11coste = x11precio * x11unidades

print(f"{x11nombre}: {x11precio:09.2f} € x {x11unidades:03d} unidades = {x11coste:010.2f} €")