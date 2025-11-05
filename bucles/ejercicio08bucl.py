x8a = int(input("Introduce un número entero: "))

for i in range(1, x8a + 1):
    x8fila = [str(2 * j - 1) for j in range(i, 0, -1)]
    print(" ".join(x8fila))
