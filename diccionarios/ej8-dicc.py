entrada = input("Introduce las palabras en formato palabra:traducción separadas por comas:\n")

diccionario = {}
pares = entrada.split(",")

for par in pares:
    esp, eng = par.split(":")
    diccionario[esp.strip()] = eng.strip()

frase = input("Introduce una frase en español:\n")
palabras = frase.split()

traduccion = []
for palabra in palabras:
    traduccion.append(diccionario.get(palabra, palabra))

print("Traducción:")
print(" ".join(traduccion))
