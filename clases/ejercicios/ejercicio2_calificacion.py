class EvaluacionParciales(object):
    def __init__(self):
        self.p1 = 0.0
        self.p2 = 0.0
        self.p3 = 0.0
        self.final = 0.0
        self.estado = ""

    def leerParciales(self):
        self.p1 = float(input("Ingrese la calificación del primer parcial (0-100): "))
        self.p2 = float(input("Ingrese la calificación del segundo parcial (0-100): "))
        self.p3 = float(input("Ingrese la calificación del tercer parcial (0-100): "))

    def calcularFinal(self):
        self.final = (self.p1 * 0.30) + (self.p2 * 0.30) + (self.p3 * 0.40)

    def determinarEstado(self):
        if self.p1 < 50 or self.p2 < 50 or self.p3 < 50:
            self.estado = "Reprobado"
        elif self.final >= 70:
            self.estado = "Aprobado"
        else:
            self.estado = "Reprobado"

    def mostrarResultado(self):
        print(f"Calificación final: {self.final:.2f}")
        print(f"Estado: {self.estado}")


