facturas = {}
cobrado = 0.0

while True:
    opcion = input("\n¿Quieres (a)ñadir factura, (p)agar factura o (t)erminar?: ").lower()

    if opcion == "a":
        num = input("Número de factura: ")
        coste = float(input("Coste de la factura: "))
        facturas[num] = coste

    elif opcion == "p":
        num = input("Número de factura a pagar: ")
        if num in facturas:
            cobrado += facturas[num]
            del facturas[num]
        else:
            print("La factura no existe.")

    elif opcion == "t":
        break

    pendiente = sum(facturas.values())
    print(f"Total cobrado: {cobrado}")
    print(f"Total pendiente: {pendiente}")
