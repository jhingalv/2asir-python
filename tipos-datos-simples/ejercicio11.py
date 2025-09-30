#Ejercicio 11

deposito_inicial = float(input("Introduce la cantidad depositada en la cuenta: "))

interes_anual = 0.04
balance = deposito_inicial

for año in range(1, 4):
    balance += balance * interes_anual
    print(f"Saldo tras el año {año}: {balance:.2f}€")
