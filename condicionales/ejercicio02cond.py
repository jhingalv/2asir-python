x2pass = "Admin123"
x2passInput = input ("Por favor, introduce tu contraseña: ")

if x2passInput.upper() == x2pass.upper():
    print ("Contraseña correcta.")
else:
    print ("Contraseña incorrecta.")