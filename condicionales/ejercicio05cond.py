x6edad = int (input ("Por favor, introduce tu edad: "))
x6ingresos = int (input ("Por favor, introduce tus ingresos mensuales: "))

if x6edad < 16 or x6ingresos < 1000:
    print ("No tienes que pagar impuestos.")
else:
    print ("Tienes que pagar impuestos.")