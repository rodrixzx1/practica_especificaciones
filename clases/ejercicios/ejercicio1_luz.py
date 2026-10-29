class ConsumoLuz(object):
    def __init__(self):
        self.consumo = 0.0
        self.importe = 0.0

    def leerConsumo(self):
        self.consumo = float(input("Ingrese el consumo en kWh: "))

    def calcularPago(self):
        if self.consumo <= 150:
            self.importe = self.consumo * 1.00
        elif self.consumo <= 280:
            self.importe = (150 * 1.00) + ((self.consumo - 150) * 1.50)
        else:
            self.importe = (150 * 1.00) + (130 * 1.50) + ((self.consumo - 280) * 3.00)

    def mostrarRecibo(self):
        print(f"El importe del recibo de luz es: ${self.importe:.2f}")

