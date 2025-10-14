x3divid = int (input ("Por favor, introduce un dividendo: "))
x3divis = int (input ("Por favor, introduce un divisor: "))

if x3divis == 0:
    print ("ERROR: No se puede dividir por cero.")
else:
    print (f"El resultado de la división es: {x3divid / x3divis}")