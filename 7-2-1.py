class Electrodomestico:
    def __init__ (self):
        self.__Encendido = False 
        self.__Tension = 0
    def Encender(self):
        self.__Encendido = True
    def Apagar(self):
        self.__Encendido = False
    def Encendido(self):
        return self.__Encendido
    def SetTension(self, tension):
        self.__Tension = tension
    def GetTension(self):
        return self.__Tension

class Lavadora(Electrodomestico):
    def __init__ (self):
        self.__RPM = 0
        self.__Kilos = 0
    def SetRPM(self, rpm):
        self.__RPM = rpm
    def SetKilos(self, kilos):
        self.__Kilos = kilos
    def MostrarLavadora(self):
        print("#########")
        print("Lavadora:")
        print("\tRPM:",self.__RPM)
        print("\tKilos:",self.__Kilos)
        print("\tTension:",self.GetTension())
        if self.Encendido():
            print("\t¡Lavadora encendida!")
        else:
            print("\tLavadora no encendida.")
        print("#########")

lavadora = Lavadora()
lavadora.SetRPM(1200)
lavadora.SetKilos(7)
lavadora.SetTension(220)
lavadora.Encender()
lavadora.MostrarLavadora()
