divisas = {
    'Euro': '€',
    'Dollar': '$',
    'Yen': '¥'
}

divisa = input("Introduce una divisa (Euro, Dollar o Yen): ")

if divisa in divisas:
    print(f"El símbolo de {divisa} es {divisas[divisa]}")
else:
    print("La divisa introducida no está en el diccionario.")