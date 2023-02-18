class Punto:
    def __init__ (self, x, y):
        self.X = x
        self.Y = y
    def MostrarPunto(self):
        print("El punto es (",self.X,",",self.Y,")")

class Triangulo:
    def __init__ (self, v1,v2,v3):
        self.V1 = v1
        self.V2 = v2
        self.V3 = v3
    def MostrarVertices(self):
        self.V1.MostrarPunto()
        self.V2.MostrarPunto()
        self.V3.MostrarPunto()

v1 = Punto(3,4)
v2 = Punto(6,8)
v3 = Punto(9,2)
triangulo = Triangulo(v1,v2,v3)
triangulo.MostrarVertices()
