x9edad = int(input("Por favor, introduce tu edad: "))

if x9edad < 4:
    x9precio = 0
elif 4 <= x9edad <= 18:
    x9precio = 5
else:
    x9precio = 10

if x9precio == 0:
    print("La entrada es gratuita.")
else:
    print(f"El precio de la entrada es {x9precio}€.")
