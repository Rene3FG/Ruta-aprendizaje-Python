def EsMayorQueCero(param):
    if param > 0:
        print(param, "es mayor que cero")
    else:
        print(param, "no es mayor que cero")

numero = int(input("Introduce un numero:"))
EsMayorQueCero(numero)
