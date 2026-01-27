texto = """nif;nombre;email;teléfono;descuento\n01234567L;Luis González;luisgonzalez@mail.com;656343576;12.5\n71476342J;Macarena Ramírez;macarena@mail.com;692839321;8\n63823376M;Juan José Martínez;juanjo@mail.com;664888233;5.2\n98376547F;Carmen Sánchez;carmen@mail.com;667677855;15.7"""

lineas = texto.split("\n")
campos = lineas[0].split(";")

clientes = {}

for linea in lineas[1:]:
    datos = linea.split(";")
    nif = datos[0]
    clientes[nif] = {
        campos[1]: datos[1],
        campos[2]: datos[2],
        campos[3]: datos[3],
        campos[4]: float(datos[4])
    }

print(clientes)
