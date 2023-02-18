class PuntoPublico:
    def __init__ (self, x, y):
        self.X = x
        self.Y = y
    
class PuntoPrivado:
    def __init__ (self, x, y):
        self.__X = x
        self.__Y = y
    def GetX(self):
        return self.__X
    def GetY(self):
        return self.__Y
    def SetX(self, x):
        self.__X = x
    def SetY(self, y):
        self.__Y = y

publico = PuntoPublico(4,6)
privado = PuntoPrivado(7,3)
print("Valores punto publico:", publico.X,",",publico.Y)
print("Valores punto privado:", privado.GetX(),",",privado.GetY())
publico.X = 2
privado.SetX(9)
print("Valores punto publico:", publico.X,",",publico.Y)
print("Valores punto privado:", privado.GetX(),",",privado.GetY())
