cesta = {}
total = 0

while True:
    articulo = input("Introduce un artículo (o 'fin' para terminar): ").lower()
    if articulo == "fin":
        break

    precio = float(input("Introduce el precio: "))
    cesta[articulo] = precio
    total += precio

print("\nLista de la compra")
for articulo, precio in cesta.items():
    print(f"{articulo}: {precio}")

print(f"\nTotal: {total}")
