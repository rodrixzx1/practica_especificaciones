class Calculadora(object):
    def __init__(self):
        self.numero1 = 0
        self.numero2 = 0
        self.suma = 0

    def leerNumeros(self):
        self.numero1 = float(input("Número 1: "))
        self.numero2 = float(input("Número 2: "))

    def calcularSuma(self):
        self.suma = self.numero1 + self.numero2

    def mostrarSuma(self):
        print(f"La suma es: {self.suma}")