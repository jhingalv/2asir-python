x5cantidad = float(input("Introduce la cantidad a invertir: "))
x5interesAnual = float(input("Introduce el interés anual (en %): "))
x5anios = int(input("Introduce el número de años: "))

for i in range(1, x5anios + 1):
    x5cantidad *= 1 + x5interesAnual / 100
    print(f"Año {i}: capital = {x5cantidad:.2f}")
