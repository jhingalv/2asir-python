x8puntuacion = float(input("Introduce la puntuación del empleado (0.0, 0.4, 0.6 o más): "))

x8nivel = ""
x8cantidad = 0

if x8puntuacion == 0.0:
    x8nivel = "Inaceptable"
    x8cantidad = 2400 * x8puntuacion
elif x8puntuacion == 0.4:
    x8nivel = "Aceptable"
    x8cantidad = 2400 * x8puntuacion
elif x8puntuacion >= 0.6:
    x8nivel = "Meritorio"
    x8cantidad = 2400 * x8puntuacion
else:
    print("Puntuación inválida. Debe ser 0.0, 0.4, 0.6 o más.")

if x8nivel:
    print(f"Nivel de rendimiento: {x8nivel}")
    print(f"Cantidad a recibir: {x8cantidad:.2f}€")
