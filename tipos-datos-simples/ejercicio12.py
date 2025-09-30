#Ejercicio 12

precio_barra = 3.49
descuento = 0.60

barras_no_frescas = int(input("Introduce el número de barras de pan no frescas vendidas: "))

precio_descuento = precio_barra * descuento
precio_final_por_barra = precio_barra - precio_descuento
coste_total = precio_final_por_barra * barras_no_frescas

print(f"Precio habitual por barra: {precio_barra:.2f}€")
print(f"Descuento por barra (60%): {precio_descuento:.2f}€")
print(f"Coste final total: {coste_total:.2f}€")
