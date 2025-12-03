x9palabra = input("Introduce una palabra: ").lower()
x9vocales = "aeiou"
x9contador = {v: x9palabra.count(v) for v in x9vocales}

for x9vocal, x9cantidad in x9contador.items():
    print(f"{x9vocal}: {x9cantidad}")
