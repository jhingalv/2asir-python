x6nombre = input ("Por favor, introduce tu nombre: ")
x6letraNombre = x6nombre[0].upper()

x6genero = input ("Por favor, introduce tu genero (M/H): ")

if (x6genero == "M" and x6letraNombre < "M") or (x6genero == "H" and x6letraNombre > "N"):
    print ("Perteneces al grupo A")
else:
    print ("Perteneces al grupo B")
