x6asignaturas = ["Matemáticas", "Física", "Química", "Historia", "Lengua"]
x6repetir = []

for asignatura in x6asignaturas:
    nota = float(input(f"¿Qué nota has sacado en {asignatura}? "))
    if nota < 5:
        x6repetir.append(asignatura)

if x6repetir:
    print("\nTienes que repetir las siguientes asignaturas:")
    for asignatura in x6repetir:
        print(asignatura)
else:
    print("\n¡Has aprobado todo!")
