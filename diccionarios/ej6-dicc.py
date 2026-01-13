persona = {}

campos = ['nombre', 'edad', 'sexo', 'teléfono', 'correo electrónico']

for campo in campos:
    valor = input(f"Introduce tu {campo}: ")
    persona[campo] = valor
    
    print("\nDiccionario actualizado:")
    print(persona)
