x10int = int(input("Introduce un número entero: "))

if x10int < 2:
    print("No es primo.")
else:
    es_primo = True
    for i in range(2, int(x10int ** 0.5) + 1):
        if x10int % i == 0:
            es_primo = False
            break
    if es_primo:
        print("Es primo.")
    else:
        print("No es primo.")
