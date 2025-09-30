
print ("\n---------------------------------------------")
print ("Calculadora de area y perimetro de triángulo:")
print ("---------------------------------------------")

base = float(input("Ingresa la base: "))
altura = float(input("Ingresa la altura: "))

print ("---------------------------------------------")

area = base * altura
perimetro = (base * 2) + (altura * 2)

print (f"El area del rectángulo es {area:.2f}") # Usar {x:.2f} redondea la parte decimal a 2 dígitos.
print (f"El perimetro del rectángulo es {perimetro:.2f}") 
print ("---------------------------------------------\n")
