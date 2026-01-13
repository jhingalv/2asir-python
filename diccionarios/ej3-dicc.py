precios = {
    "plátano": 1.35,
    "manzana": 0.80,
    "pera": 0.85,
    "naranja": 0.70
}

fruta = input("Introduce el nombre de la fruta: ").lower()
kilos = float(input("Introduce el número de kilos: "))

if fruta in precios:
    precio_total = precios[fruta] * kilos
    print(f"El precio de {kilos} kg de {fruta} es {precio_total:.2f} €")
else:
    print("La fruta introducida no está disponible.")
