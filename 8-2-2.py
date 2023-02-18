fcrear = open("pruebacreacion.txt","x")
fcrear.write("Time of Software\n")
fcrear.write("Fichero creado 8-2-2\n")
fcrear.close()

print("### Fichero creado ###")

flectura = open("pruebacreacion.txt","r")
texto = flectura.read()
flectura.close()
print(texto)
