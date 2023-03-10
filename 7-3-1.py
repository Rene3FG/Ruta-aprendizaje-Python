class Hotel:
    def __init__ (self):
        self.__NumeroHabitaciones = 0 
        self.__Estrellas = 0
    def SetNumeroHabitaciones(self, habs):
        self.__NumeroHabitaciones = habs
    def SetEstrellas(self, estrellas):
        self.__Estrellas = estrellas
    def MostrarHotel(self):
        print("---------")
        print("Hotel:")
        print("\tEstrellas:", self.__Estrellas)
        print("\tNumero de habitaciones:", self.__NumeroHabitaciones)
        print("---------")

class Restaurante():
    def __init__ (self):
        self.__Tenedores = 0
        self.__HoraApertura = 0
    def SetTenedores(self, tenedores):
        self.__Tenedores = tenedores
    def SetHoraApertura(self, hora):
        self.__HoraApertura = hora
    def MostrarRestaurante(self):
        print("---------")
        print("Restaurante:")
        print("\tTenedores:",self.__Tenedores)
        print("\tHora de Apertura:",self.__HoraApertura)
        print("---------")

class Negocio(Hotel, Restaurante):
    def __init__(self):
        self.__Nombre = ""
        self.__Direccion = ""
        self.__Telefono = 0
    def SetNombre(self, nombre):
        self.__Nombre = nombre
    def SetDireccion(self, direccion):
        self.__Direccion = direccion
    def SetTelefono(self, telefono):
        self.__Telefono = telefono
    def MostrarNegocio(self):
        print("#########")
        print("Negocio:")
        print("\tNombre:", self.__Nombre)
        print("\tDireccion:", self.__Direccion)
        print("\tTelefono:", self.__Telefono)
        self.MostrarHotel()
        self.MostrarRestaurante()
        print("#########")

negocio = Negocio()
negocio.SetEstrellas(4)
negocio.SetNumeroHabitaciones(255)
negocio.SetTenedores(3)
negocio.SetHoraApertura(8)
negocio.SetNombre("Time of Software")
negocio.SetDireccion("Calle Falsa 123")
negocio.SetTelefono("0034914567890")
negocio.MostrarNegocio()
