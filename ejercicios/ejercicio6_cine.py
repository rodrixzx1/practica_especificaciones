# PROBLEMA
# Calcular el precio de un boleto de cine basado en la edad del asistente y las tarifas preferenciales.
# ENTRADAS
# edad: int, años, mayor o igual a 0.
# SALIDAS
# precio: float, pesos, formato con dos decimales.
# REGLAS Y SUPUESTOS
# El precio regular del boleto es de $80.
# Los niños de hasta 12 años (edad <= 12) pagan la mitad ($40).
# Los adultos de 60 años o más (edad >= 60) pagan la mitad ($40).
# Las edades entre 13 y 59 años pagan precio regular ($80).
# ALGORITMO
# 1. Leer la edad.
# 2. Si edad <= 12 o edad >= 60:
#      precio = 40.0
# 3. En caso contrario:
#      precio = 80.0
# 4. Mostrar el precio.
# CASOS DE PRUEBA
# 8 -> 40.00
# 12 -> 40.00
# 13 -> 80.00
# 59 -> 80.00
# 60 -> 40.00
# RESTRICCIONES PARA EL AGENTE
# Implementa exactamente este algoritmo, en el mismo orden.
# Usa únicamente las funciones del contrato, con esas firmas.
# No agregues clases, funciones auxiliares ni bibliotecas.
# No agregues validaciones, mensajes ni cálculos que no estén aquí.
# No llames a las funciones en este archivo; se llaman desde menu/menu.py.

# CONTRATO DE FUNCIONES
# leerEdad() -> int
# calcularPrecio(edad: int) -> float
# mostrarPrecio(edad: int, precio: float) -> None

def leerEdad():
    edad = int(input("Ingrese la edad del asistente: "))
    return edad

def calcularPrecio(edad: int) -> float:
    if edad <= 12 or edad >= 60:
        precio = 40.0
    else:
        precio = 80.0
    return precio

def mostrarPrecio(edad: int, precio: float) -> None:
    print(f"El precio del boleto para un asistente de {edad} años es: ${precio:.2f}")
