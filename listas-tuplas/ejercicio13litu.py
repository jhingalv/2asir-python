import math

x13numeros = input("Introduce números separados por comas: ")
x13lista = [float(n) for n in x13numeros.split(",")]

x13media = sum(x13lista) / len(x13lista)
x13varianza = sum((x - x13media) ** 2 for x in x13lista) / len(x13lista)
x13desviacion = math.sqrt(x13varianza)

print("Media:", x13media)
print("Desviación típica:", x13desviacion)
