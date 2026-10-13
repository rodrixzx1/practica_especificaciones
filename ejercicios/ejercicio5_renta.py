# PROBLEMA
# Calcular el importe a pagar por la renta de bicicletas en un parque según las horas de uso y un descuento por volumen.
# ENTRADAS
# horas: int, horas de renta, mayor a 0.
# SALIDAS
# importe: float, pesos, formato con dos decimales.
# REGLAS Y SUPUESTOS
# La tarifa base es de $30 por hora.
# Si se rentan 3 horas o más (horas >= 3), se aplica un 15% de descuento sobre el total.
# Si se rentan menos de 3 horas, no hay descuento.
# ALGORITMO
# 1. Leer las horas.
# 2. Si horas >= 3:
#      importe = (horas * 30.0) * 0.85
# 3. En caso contrario:
#      importe = horas * 30.0
# 4. Mostrar el importe.
# CASOS DE PRUEBA
# 1 -> 30.00
# 2 -> 60.00
# 3 -> 76.50
# 4 -> 102.00
# RESTRICCIONES PARA EL AGENTE
# Implementa exactamente este algoritmo, en el mismo orden.
# Usa únicamente las funciones del contrato, con esas firmas.
# No agregues clases, funciones auxiliares ni bibliotecas.
# No agregues validaciones, mensajes ni cálculos que no estén aquí.
# No llames a las funciones en este archivo; se llaman desde menu/menu.py.

# CONTRATO DE FUNCIONES
# leerHoras() -> int
# calcularRenta(horas: int) -> float
# mostrarRenta(horas: int, importe: float) -> None

def leerHoras():
    horas = int(input("Ingrese el número de horas de renta: "))
    return horas

def calcularRenta(horas: int) -> float:
    if horas >= 3:
        importe = (horas * 30.0) * 0.85
    else:
        importe = horas * 30.0
    return importe

def mostrarRenta(horas: int, importe: float) -> None:
    print(f"El importe a pagar por {horas} horas de renta es: ${importe:.2f}")

