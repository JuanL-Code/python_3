"""
Permite modelar jerarquias de clases
Permite compartir un comportamiento comun en la jerarquia
Super clase es padre y subclase es hijo
"""

class Rectangulo:

    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def area(self):
        return self.base * self.altura

#Cuadrado extends rectangulo
class Cuadrado(Rectangulo):

    def __init__(self, lado):
        #obtener referencia y llamar a su constructor
        super().__init__(lado,lado)


if __name__ == "__main__":

    rectangulo = Rectangulo(base = 3, altura = 4)
    print(rectangulo.area())

    cuadrado = Cuadrado(lado=5)
    print(cuadrado.area())