# PROBLEMA
# Calcular la multa por exceso de velocidad en una avenida según la velocidad registrada del vehículo.
# ENTRADAS
# velocidad: int, km/h, mayor a 0.
# SALIDAS
# multa: float, pesos, formato con dos decimales.
# REGLAS Y SUPUESTOS
# El límite de velocidad permitido es de 60 km/h.
# Si la velocidad es menor o igual a 60, la multa es de $0.0.
# Si se excede hasta por 20 km/h (es decir, velocidad > 60 y velocidad <= 80), la multa es de $500.
# Si se excede por más de 20 km/h (velocidad > 80), la multa es de $1,000.
# ALGORITMO
# 1. Leer la velocidad.
# 2. Si velocidad <= 60:
#      multa = 0.0
# 3. En caso contrario, si velocidad <= 80:
#      multa = 500.0
# 4. En caso contrario:
#      multa = 1000.0
# 5. Mostrar la multa.
# CASOS DE PRUEBA
# 50 -> 0.00
# 60 -> 0.00
# 61 -> 500.00
# 80 -> 500.00
# 81 -> 1000.00
# RESTRICCIONES PARA EL AGENTE
# Implementa exactamente este algoritmo, en el mismo orden.
# Usa únicamente las funciones del contrato, con esas firmas.
# No agregues clases, funciones auxiliares ni bibliotecas.
# No agregues validaciones, mensajes ni cálculos que no estén aquí.
# No llames a las funciones en este archivo; se llaman desde menu/menu.py.

# CONTRATO DE FUNCIONES
# leerVelocidad() -> int
# calcularMulta(velocidad: int) -> float
# mostrarMulta(velocidad: int, multa: float) -> None

def leerVelocidad():
    velocidad = int(input("Ingrese la velocidad del vehículo (km/h): "))
    return velocidad

def calcularMulta(velocidad: int) -> float:
    if velocidad <= 60:
        multa = 0.0
    elif velocidad <= 80:
        multa = 500.0
    else:
        multa = 1000.0
    return multa

def mostrarMulta(velocidad: int, multa: float) -> None:
    print(f"La multa por exceso de velocidad para {velocidad} km/h es: ${multa:.2f}")
