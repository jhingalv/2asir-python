x1nombre = input ("Por favor dime tu nombre: ")

x1numero = int(input (
    f"Perfecto {x1nombre}, ¿en cuantas lineas quieres repetir tu nombre? "
))

for i in range(x1numero):
    print (x1nombre)