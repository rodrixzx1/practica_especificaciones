from clases.ejemplo.calculadora import Calculadora
from clases.ejercicios.ejercicio1_luz import ConsumoLuz
from clases.ejercicios.ejercicio2_calificacion import EvaluacionParciales 

class Menu(object):

    def __init__(self):
        self.opcion = 0

    def mostrarMenu(self):
        print()
        print("Ejemplo programacion orientada a objetos")
        print("1. Calculadora")
        print("2. Consumo de Luz")
        print("3. Calificaciones Parciales")  
        print("0. Salir")

    def menu(self):
        self.opcion = ""
        while self.opcion != "0":
            self.mostrarMenu()
            self.opcion = input("Seleccione una opción: ")

            if self.opcion == "1":
                casio = Calculadora()
                casio.leerNumeros()
                casio.calcularSuma()
                casio.mostrarSuma()

            elif self.opcion == "2":  
                luz = ConsumoLuz()
                luz.leerConsumo()
                luz.calcularPago()
                luz.mostrarRecibo()

            elif self.opcion == "3":  
                evaluacion = EvaluacionParciales()
                evaluacion.leerParciales()
                evaluacion.calcularFinal()
                evaluacion.determinarEstado()
                evaluacion.mostrarResultado()

            elif self.opcion == "0":
                print("Saliendo del sistema...")

            else:
                print("Opción no válida. Intente de nuevo.")
