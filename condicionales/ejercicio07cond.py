x5renta = float(input("Introduce tu renta anual en euros: "))

if x5renta < 10000:
    x5tipo = 5
elif x5renta < 20000:
    x5tipo = 15
elif x5renta < 35000:
    x5tipo = 20
elif x5renta < 60000:
    x5tipo = 30
else:
    x5tipo = 45

print(f"El tipo impositivo que te corresponde es del {x5tipo}%")
