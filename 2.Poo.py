# Ejercicio 2: Clases, Objetos, Mensajes, this

import math

class Carro:
    def atrib(modelo, marca, color, puertas, llanta):
        modelo = " "
        marca = " "
        color = " "
        puertas = " "
        llanta = " "

class Llanta(Carro):

    def __init__(self):
        self.radio = int(input("Ingrese el radio de la llanta: "))
        self.perimetro = 2 * math.pi * self.radio # perímetro de la llanta
        self.area = math.pi * self.radio ** 2 # área de la llanta
        self.diametro = self.radio * 2
        print ("La circunferencia de la llanta es:", int(self.perimetro))
        print ("El área de la llanta es:", int(self.area))
        print ("El diámetro de la llanta es:", int(self.diametro))

llanta = Llanta()

