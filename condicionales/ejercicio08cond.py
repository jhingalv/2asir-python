x7puntuacion = float(input("Introduce la puntuación del empleado (0.0, 0.4, 0.6 o más): "))

x7nivel = ""
x7cantidad = 0

if x7puntuacion == 0.0:
    x7nivel = "Inaceptable"
    x7cantidad = 2400 * x7puntuacion
elif x7puntuacion == 0.4:
    x7nivel = "Aceptable"
    x7cantidad = 2400 * x7puntuacion
elif x7puntuacion >= 0.6:
    x7nivel = "Meritorio"
    x7cantidad = 2400 * x7puntuacion
else:
    print("Puntuación inválida. Debe ser 0.0, 0.4, 0.6 o más.")

if x7nivel:
    print(f"Nivel de rendimiento: {x7nivel}")
    print(f"Cantidad a recibir: {x7cantidad:.2f}€")
