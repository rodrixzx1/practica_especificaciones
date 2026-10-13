# PROBLEMA
# Calcular el importe a cobrar en un estacionamiento según los minutos de estancia.
# ENTRADAS
# minutos: int, minutos de estancia, mayor a 0.
# SALIDAS
# importe: float, pesos, formato con dos decimales.
# REGLAS Y SUPUESTOS
# La primera hora (hasta 60 minutos) cuesta $20 de forma fija.
# Cada hora adicional o fracción cuesta $15.
# El cobro máximo no puede superar los $150.
# Redondeo: No se permite usar módulos (como math.ceil). Toda fracción de hora se cuenta como hora completa sumando 59 antes de hacer división entera entre 60.
# ALGORITMO
# 1. Leer los minutos.
# 2. Si minutos <= 60:
#      importe = 20.0
# 3. En caso contrario:
#      horas_extra = (minutos - 60 + 59) // 60
#      importe = 20.0 + (horas_extra * 15.0)
# 4. Si importe > 150.0:
#      importe = 150.0
# 5. Mostrar el importe.
# CASOS DE PRUEBA
# 45 -> 20.00
# 60 -> 20.00
# 61 -> 35.00
# 150 -> 50.00
# 600 -> 150.00 (alcanza el tope máximo)
# RESTRICCIONES PARA EL AGENTE
# Implementa exactamente este algoritmo, en el mismo orden.
# Usa únicamente las funciones del contrato, con esas firmas.
# NO IMPORTES NINGÚN MÓDULO, NI SIQUIERA math.
# No agregues clases, funciones auxiliares ni bibliotecas.
# No agregues validaciones, mensajes ni cálculos que no estén aquí.
# No llames a las funciones en este archivo; se llaman desde menu/menu.py.

# CONTRATO DE FUNCIONES
# leerMinutos() -> int
# calcularCobro(minutos: int) -> float
# mostrarCobro(importe: float) -> None

def leerMinutos():
    minutos = int(input("Ingrese los minutos de estancia: "))
    return minutos
    
def calcularCobro(minutos: int) -> float:
    if minutos <= 60:
        importe = 20.0
    else:
        horas_extra = (minutos - 60 + 59) // 60
        importe = 20.0 + (horas_extra * 15.0)
    if importe > 150.0:
        importe = 150.0
    return importe

def mostrarCobro(importe: float) -> None:
    print(f"El importe a cobrar es: ${importe:.2f}")

