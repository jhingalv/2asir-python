x10productos = input("Introduce los productos de la cesta separados por comas: ")
x10lista = x10productos.split(",")

print("Productos:")
for x10producto in x10lista:
    print(x10producto.strip())