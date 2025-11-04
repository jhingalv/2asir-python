x3int = abs(int(input("Introduce tu un numero entero positivo: ")))
i = 0

while i <= x3int:
    if i % 2 != 0:
        print(i, end=", ")
    i = i + 1
print("")