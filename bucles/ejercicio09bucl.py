x9contrasena = "p4ssw0rd"
x9intento = ""

while x9intento != x9contrasena:
    x9intento = input("Introduce la contraseña: ")
    if x9intento == x9contrasena:
        print("¡Contraseña correcta!")
        break
    else:
        print("Contraseña incorrecta. Inténtalo de nuevo.")
