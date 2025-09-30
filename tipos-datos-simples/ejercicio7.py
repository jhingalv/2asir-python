#Ejercicio 7

peso = float(input("Ingresa tu peso en kilogramos (kg): "))
altura = float(input("Ingresa tu altura en metros (m): "))

if peso <= 0 or altura <= 0:
    print("El peso y la altura deben ser valores positivos.")
else:
    imc = peso / (altura ** 2)

    if imc < 18.5:
        interpretacion = "Bajo peso"
    elif 18.5 <= imc < 24.9:
        interpretacion = "Peso normal"
    elif 25 <= imc < 29.9:
        interpretacion = "Sobrepeso"
    else:
        interpretacion = "Obesidad"

    print(f"\nTu IMC es: {imc:.2f}") # Usar {imc:.2f} redondea la parte decimal a 2 dígitos.
    print(f"Interpretación: {interpretacion}")
