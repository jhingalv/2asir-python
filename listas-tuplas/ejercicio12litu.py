A = [
    [1, 2, 3],
    [4, 5, 6]
]

B = [
    [1, 1],
    [2, 2],
    [3, 3]
]

x12resultado = [[sum(a*b for a, b in zip(fila, col)) for col in zip(*B)] for fila in A]

for x12fila in x12resultado:
    print(x12fila)
