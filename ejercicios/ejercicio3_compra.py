# PROBLEMA
# Calcular el subtotal, descuento, IVA y total a pagar de una compra en una tienda.
# ENTRADAS
# compra_inicial: float, pesos, mayor a 0.
# SALIDAS
# subtotal: float, pesos, formato con dos decimales.
# descuento: float, pesos, formato con dos decimales.
# iva: float, pesos, formato con dos decimales.
# total: float, pesos, formato con dos decimales.
# REGLAS Y SUPUESTOS
# Si la compra es >= 5000, aplica un 20% de descuento.
# Si la compra es >= 1000 y < 5000, aplica un 10% de descuento.
# Si la compra es < 1000, el descuento es de 0%.
# El IVA es del 16% (0.16) y se calcula sobre el monto después de aplicar el descuento.
# El total es el monto (compra - descuento) más el IVA.
# ALGORITMO
# 1. Leer el monto de compra_inicial (que será el subtotal).
# 2. Si compra_inicial >= 5000:
#      descuento = compra_inicial * 0.20
# 3. En caso contrario, si compra_inicial >= 1000:
#      descuento = compra_inicial * 0.10
# 4. En caso contrario:
#      descuento = 0.0
# 5. Calcular iva = (compra_inicial - descuento) * 0.16
# 6. Calcular total = (compra_inicial - descuento) + iva
# 7. Mostrar compra_inicial (como subtotal), descuento, iva y total.
# CASOS DE PRUEBA
# 500 -> Subtotal: 500.00, Descuento: 0.00, IVA: 80.00, Total: 580.00
# 900 -> Subtotal: 900.00, Descuento: 0.00, IVA: 144.00, Total: 1044.00
# 1000 -> Subtotal: 1000.00, Descuento: 100.00, IVA: 144.00, Total: 1044.00
# 5000 -> Subtotal: 5000.00, Descuento: 1000.00, IVA: 640.00, Total: 4640.00
# RESTRICCIONES PARA EL AGENTE
# Implementa exactamente este algoritmo, en el mismo orden.
# Usa únicamente las funciones del contrato, con esas firmas.
# No agregues clases, funciones auxiliares ni bibliotecas.
# No agregues validaciones, mensajes ni cálculos que no estén aquí.
# No llames a las funciones en este archivo; se llaman desde menu/menu.py.

# CONTRATO DE FUNCIONES
# leerSubtotal() -> float
# calcularDescuento(subtotal: float) -> float
# calcularIVA(subtotal: float, descuento: float) -> float
# calcularTotal(subtotal: float, descuento: float, iva: float) -> float
# mostrarTicket(subtotal: float, descuento: float, iva: float, total: float) -> None

def leerSubtotal():
    subtotal = float(input("Ingrese el monto de la compra: "))
    return subtotal

def calcularDescuento(subtotal: float) -> float:
    if subtotal >= 5000:
        return subtotal * 0.20
    elif subtotal >= 1000:
        return subtotal * 0.10
    else:
        return 0.0

def calcularIVA(subtotal: float, descuento: float) -> float:
    return (subtotal - descuento) * 0.16

def calcularTotal(subtotal: float, descuento: float, iva: float) -> float:
    return (subtotal - descuento) + iva

def mostrarTicket(subtotal: float, descuento: float, iva: float, total: float) -> None:
    print(f"Subtotal: {subtotal:.2f}")
    print(f"Descuento: {descuento:.2f}")
    print(f"IVA: {iva:.2f}")
    print(f"Total: {total:.2f}")
