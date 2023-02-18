class OperarValores:
    def __init__ (self, v1, v2):
        self.__V1 = v1
        self.__V2 = v2
    def __Sumar(self):
        return self.__V1 + self.__V2
    def __Restar(self):
        return self.__V1 - self.__V2
    def Operar(self):
        print("El resultado de la suma es: ",self.__Sumar())
        print("El resultado de la resta es: ",self.__Restar())

operarvalores = OperarValores(7,3)
operarvalores.Operar()
