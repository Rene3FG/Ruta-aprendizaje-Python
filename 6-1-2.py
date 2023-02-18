class Punto:
    def __init__ (self, x, y):
        self.X = x
        self.Y = y
    def MostrarPunto(self):
        print("El punto es (",self.X,",",self.Y,")")

p1 = Punto(4,6)
p2 = Punto(-5,9)
p3 = Punto(3,-7)
p4 = Punto(0,4)
p1.MostrarPunto()
p2.MostrarPunto()
p3.MostrarPunto()
p4.MostrarPunto()
