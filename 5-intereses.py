
print ("\n---------------------------------------------")
print ("Calculadora de interés simple:")
print ("---------------------------------------------")

capinicial = float(input("Ingresa el capital inicial: "))
interes = float(input("Ingresa el porcentaje de interés: "))
periodo = float(input("Ingresa el periodo de tiempo: "))

print ("---------------------------------------------")

interestotal = capinicial * (interes/100) * periodo
capfinal = capinicial + interestotal

print (f"El interés total es {interestotal:.2f}") # Usar {x:.2f} redondea la parte decimal a 2 dígitos.
print (f"El capital final es {capfinal:.2f}")
print ("---------------------------------------------\n")
