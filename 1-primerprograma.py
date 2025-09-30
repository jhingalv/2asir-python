
num1 = float(input("Ingresa el primer número: "))
num2 = float(input("Ingresa el segundo número: "))

operador = input("Ingresa el operador (+, -, *, /): ")

if operador == "+":
    resultado = num1 + num2
    print(f"Resultado: {num1} + {num2} = {resultado}")
elif operador == "-":
    resultado = num1 - num2
    print(f"Resultado: {num1} - {num2} = {resultado}")
elif operador == "*":
    resultado = num1 * num2
    print(f"Resultado: {num1} * {num2} = {resultado}")
elif operador == "/":
    if num2 != 0:
        resultado = num1 / num2
        print(f"El resultado es: {num1} / {num2} = {resultado}")
    else:
        print("Error: No se puede dividir entre cero.")
else:
    print("Operador no válido. Usa uno de estos: +, -, *, /")
