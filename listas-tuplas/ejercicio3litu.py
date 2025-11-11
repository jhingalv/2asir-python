x3asignaturas = ["Matemáticas", "Física", "Química", "Historia", "Lengua"]
x3notas = []

for asignatura in x3asignaturas:
    nota = input(f"¿Qué nota has sacado en {asignatura}? ")
    x3notas.append(nota)

print("\nResumen de tus notas:")
for i in range(len(x3asignaturas)):
    print(f"En {x3asignaturas[i]} has sacado {x3notas[i]}")
