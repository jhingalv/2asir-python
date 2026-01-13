creditos = {
    'Matemáticas': 6,
    'Física': 4,
    'Química': 5
}

total_creditos = 0

for asignatura, creditos_asignatura in creditos.items():
    print(f"{asignatura} tiene {creditos_asignatura} créditos")
    total_creditos += creditos_asignatura

print(f"El número total de créditos del curso es {total_creditos}")
