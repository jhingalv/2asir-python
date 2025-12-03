x6asignaturas = ["Matemáticas", "Física", "Química", "Historia", "Lengua"]
x6repetir = []

for x6asignatura in x6asignaturas:
    nota = float(input(f"¿Qué nota has sacado en {x6asignatura}? "))
    if nota < 5:
        x6repetir.append(x6asignatura)

if x6repetir:
    print("\nTienes que repetir las siguientes asignaturas:")
    for x6asignatura in x6repetir:
        print(x6asignatura)
else:
    print("\n¡Has aprobado todo!")
