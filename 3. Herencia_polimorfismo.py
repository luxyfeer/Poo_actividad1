# Taller para herencia y polimorfismo

from abc import ABC, abstractmethod
import math

class Figura(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimetro(self):
        pass

class Circulo(Figura):
    def __init__(self, radio):
        self.radio = radio

    def area(self):
        resultado = math.pi * self.radio**2
        return resultado

    def perimetro(self):
        resultado = 2 * math.pi * self.radio
        return resultado

class Rectangulo(Figura):
    def __init__(self, alto, ancho):
        self.alto = alto
        self.ancho = ancho

    def area(self):
        resultado = self.alto * self.ancho
        return resultado

    def perimetro(self):
        resultado = (self.alto + self.ancho) * 2
        return resultado

class Triangulo(Figura):
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def area(self):
        resultado = self.base * self.altura / 2
        return resultado

    def perimetro(self):
        resultado = self.base * 3
        return resultado

class Rombo(Figura):
    def __init__(self, lado, altura):
        self.lado = lado
        self.altura = altura

    def area(self):
        resultado = self.lado * self.altura
        return resultado

    def perimetro(self):
        resultado = self.lado * self.lado * math.sin(180)
        return resultado

c = Circulo(int(input("escriba el radio del círculo aquí: ")))
print("Área del círculo:", int(c.area()))
print("Perímetro del círculo ", int(c.perimetro()))

r = Rectangulo(int(input("escriba el alto: ")),int(input("escriba el ancho: ")))
print("Área del rectángulo: %.2f" % int(r.area()))
print("Perímetro del rectángulo %.2f" % int(r.perimetro()))

t = Triangulo(int(input("escriba la base: ")),int(input("escriba la altura: ")))
print("Área del triángulo: %.2f" % int(t.area()))
print("Perímetro del triángulo %.2f" % int(t.perimetro()))

b = Rombo(int(input("escriba el lado: ")),int(input("escriba la altura: ")))
print("Área del rombo: %.2f" % int(b.area()))
print("Perímetro del rombo %.2f" % int(b.perimetro()))
