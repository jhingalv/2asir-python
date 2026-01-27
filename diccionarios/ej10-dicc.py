clientes = {}

while True:
    print("""
1. Añadir cliente
2. Eliminar cliente
3. Mostrar cliente
4. Listar todos los clientes
5. Listar clientes preferentes
6. Terminar
""")

    opcion = input("Elige una opción: ")

    if opcion == "1":
        nif = input("NIF: ")
        clientes[nif] = {
            "nombre": input("Nombre: "),
            "direccion": input("Dirección: "),
            "telefono": input("Teléfono: "),
            "correo": input("Correo: "),
            "preferente": input("¿Es preferente? (s/n): ").lower() == "s"
        }

    elif opcion == "2":
        nif = input("NIF del cliente a eliminar: ")
        clientes.pop(nif, None)

    elif opcion == "3":
        nif = input("NIF del cliente: ")
        print(clientes.get(nif, "Cliente no encontrado"))

    elif opcion == "4":
        for nif, datos in clientes.items():
            print(nif, "-", datos["nombre"])

    elif opcion == "5":
        for nif, datos in clientes.items():
            if datos["preferente"]:
                print(nif, "-", datos["nombre"])

    elif opcion == "6":
        break
