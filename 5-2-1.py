def SumarRestar(param1, param2):
    return Sumar(param1,param2), Restar(param1,param2)

def Sumar(sumando1, sumando2):
    return sumando1 + sumando2

def Restar(minuendo, sustraendo):
    return minuendo - sustraendo

numero1 = int(input("Introduce el primer numero: "))
numero2 = int(input("Introduce el segundo numero: "))
resultadosuma, resultadoresta = SumarRestar(numero1,numero2)
print("El resultado de la suma es: ", resultadosuma)
print("El resultado de la resta es: ", resultadoresta)
