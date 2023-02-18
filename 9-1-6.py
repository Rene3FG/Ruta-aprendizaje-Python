print("¡Iniciando programa!")
try:
    print(3/0)
except:
    print("ERROR: Division erronea")
else:
    print("¡No se han producido errores!")
finally:
    print("¡Programa acabado!")
