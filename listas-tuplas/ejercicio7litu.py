x7abecedario = list("abcdefghijklmnopqrstuvwxyz")

x7resultado = [letra for i, letra in enumerate(x7abecedario, start=1) if i % 3 != 0]

print(x7resultado)
