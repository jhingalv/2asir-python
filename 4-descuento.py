
print ("\n---------------------------------------------")
print ("Calculadora de precio final:")
print ("---------------------------------------------")

precio = float(input("Ingresa el precio original: "))
descuento = float(input("Ingresa porcentaje de descuento: "))

print ("---------------------------------------------")

preciofinal = precio - (precio * (descuento / 100))

print (f"El precio final es {preciofinal:.2f}") # Usar {x:.2f} redondea la parte decimal a 2 dígitos.
print ("---------------------------------------------\n")
