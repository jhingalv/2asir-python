#Ejercicio 9

cantidad = float(input("Cantidad a invertir: "))
interes_anual = float(input("Interés anual (en %): "))
años = int(input("Número de años: "))

capital_final = cantidad * (1 + interes_anual / 100) ** años

print(f"El capital obtenido en la inversión es: {capital_final:.2f}")
