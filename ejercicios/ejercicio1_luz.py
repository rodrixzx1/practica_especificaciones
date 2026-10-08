# PROBLEMA
# Calcular el importe del recibo de luz mensual de un cliente basado en su consumo con un esquema escalonado.
# ENTRADAS
# consumo: float, kWh, mayor o igual a 0.
# SALIDAS
# importe: float, pesos, formato con dos decimales.
# REGLAS Y SUPUESTOS
# Tarifa 1: $1.00 por kWh por los primeros 150 kWh.
# Tarifa 2: $1.50 por kWh por el consumo entre 151 y 280 kWh.
# Tarifa 3: $3.00 por kWh por el consumo superior a 280 kWh.
# El cálculo es acumulativo/escalonado según los rangos.
# ALGORITMO
# 1. Leer el consumo.
# 2. Si consumo <= 150:
#      importe = consumo * 1.00
# 3. Si consumo > 150 y consumo <= 280:
#      importe = (150 * 1.00) + ((consumo - 150) * 1.50)
# 4. En caso contrario (consumo > 280):
#      importe = (150 * 1.00) + (130 * 1.50) + ((consumo - 280) * 3.00)
# 5. Mostrar el importe.
# CASOS DE PRUEBA
# 100 -> $100.00
# 150 -> $150.00
# 200 -> $225.00
# 280 -> $345.00
# 300 -> $405.00
# RESTRICCIONES PARA EL AGENTE
# Implementa exactamente este algoritmo, en el mismo orden.
# Usa únicamente las funciones del contrato, con esas firmas.
# No agregues clases, funciones auxiliares ni bibliotecas.
# No agregues validaciones, mensajes ni cálculos que no estén aquí.
# No llames a las funciones en este archivo; se llaman desde menu/menu.py.

# CONTRATO DE FUNCIONES
# leerConsumo() -> float
# calcularPago(consumo: float) -> float
# mostrarRecibo(importe: float) -> None

def leerConsumo():
    consumo = float(input("Ingrese el consumo en kWh: "))
    return consumo

def calcularPago(consumo: float) -> float:
    if consumo <= 150:
        return consumo * 1.00
    elif consumo <= 280:
        return (150 * 1.00) + ((consumo - 150) * 1.50)
    else:
        return (150 * 1.00) + (130 * 1.50) + ((consumo - 280) * 3.00)

def mostrarRecibo(importe: float) -> None:
    print(f"El importe del recibo de luz es: ${importe:.2f}")
