class Punto:
    def __init__ (self, x, y):
        self.X = x
        self.Y = y
    def MostrarPunto(self):
        print("El punto es (",self.X,",",self.Y,")")

p1 = Punto(4,6)
p1.MostrarPunto()
p1.X = 7
p1.MostrarPunto()
