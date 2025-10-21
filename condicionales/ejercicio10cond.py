x10ingredientesVegetarianos = ['Pimiento', 'Tofu']
x10ingredientesNoVegetarianos = ['Peperoni', 'Jamón', 'Salmón']

x10respuesta = input("¿Desea una pizza vegetariana? (sí/no): ").strip().lower()

if x10respuesta == "sí" or x10respuesta == "si":
    x10tipoPizza = "vegetariana"
    x10ingredientesDisponibles = x10ingredientesVegetarianos
else:
    x10tipoPizza = "no vegetariana"
    x10ingredientesDisponibles = x10ingredientesNoVegetarianos

print("\nIngredientes disponibles:")
for i, x10ingrediente in enumerate(x10ingredientesDisponibles, 1):
    print(f"{i}. {x10ingrediente}")

opcion = int(input("Elija el número del ingrediente que desea: "))
x10ingredienteElegido = x10ingredientesDisponibles[opcion - 1]

print("\n--- Resumen de tu pizza ---")
print(f"Tipo de pizza: {x10tipoPizza.capitalize()}")
print("Ingredientes: Mozzarella, Tomate y " + x10ingredienteElegido)
