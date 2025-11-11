x4numeros = []

for i in range(6):
    x4numero = int(input(f"Introduce el número ganador {i+1}: "))
    x4numeros.append(x4numero)

x4numeros.sort()
print("\nLos números ganadores ordenados son:", x4numeros)
