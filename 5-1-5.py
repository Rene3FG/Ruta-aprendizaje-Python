def Sumar(*valores):
    resultado = 0
    for item in valores:
        resultado = resultado + item
    return resultado

resultado = Sumar(23,56,3,89,78,455)
print("El resultado de la suma es: ", resultado)
