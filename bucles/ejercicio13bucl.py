x13texto = ""

while x13texto != "salir":
    x13texto = input("Escribe algo (o 'salir' para terminar): ")
    if x13texto.lower() == "salir":
        print("Programa terminado.")
        break
    else:
        print(x13texto)
 