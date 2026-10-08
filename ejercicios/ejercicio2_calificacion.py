# PROBLEMA
# Calcular la calificación final de una materia a partir de tres parciales y determinar si el alumno aprobó o reprobó.
# ENTRADAS
# p1, p2, p3: float, puntos, rango de 0 a 100.
# SALIDAS
# final: float, puntos, formato con dos decimales.
# estado: string, texto ("Aprobado" o "Reprobado").
# REGLAS Y SUPUESTOS
# El primer parcial (p1) vale 30% de la calificación.
# El segundo parcial (p2) vale 30% de la calificación.
# El tercer parcial (p3) vale 40% de la calificación.
# La calificación mínima aprobatoria es 70.
# Regla estricta: Si alguno de los parciales es menor a 50, el alumno reprueba automáticamente.
# ALGORITMO
# 1. Leer las calificaciones p1, p2 y p3.
# 2. Calcular final = (p1 * 0.30) + (p2 * 0.30) + (p3 * 0.40).
# 3. Si p1 < 50 o p2 < 50 o p3 < 50:
#      estado = "Reprobado"
# 4. En caso contrario, si final >= 70:
#      estado = "Aprobado"
# 5. En caso contrario:
#      estado = "Reprobado"
# 6. Mostrar la calificación final y el estado.
# CASOS DE PRUEBA
# (80, 70, 90) -> Final: 81.00, Estado: Aprobado
# (70, 70, 70) -> Final: 70.00, Estado: Aprobado
# (100, 100, 40) -> Final: 100.00 (el cálculo directo da eso), Estado: Reprobado (por parcial menor a 50)
# (69, 70, 70) -> Final: 69.70, Estado: Reprobado
# RESTRICCIONES PARA EL AGENTE
# Implementa exactamente este algoritmo, en el mismo orden.
# Usa únicamente las funciones del contrato, con esas firmas.
# No agregues clases, funciones auxiliares ni bibliotecas.
# No agregues validaciones, mensajes ni cálculos que no estén aquí.
# No llames a las funciones en este archivo; se llaman desde menu/menu.py.

# CONTRATO DE FUNCIONES
# leerParciales() -> tuple
# calcularFinal(p1: float, p2: float, p3: float) -> float
# determinarEstado(p1: float, p2: float, p3: float, final: float) -> str
# mostrarResultado(final: float, estado: str) -> None

def leerParciales():
    p1 = float(input("Ingrese la calificación del primer parcial (0-100): "))
    p2 = float(input("Ingrese la calificación del segundo parcial (0-100): "))
    p3 = float(input("Ingrese la calificación del tercer parcial (0-100): "))
    return p1, p2, p3

def calcularFinal(p1: float, p2: float, p3: float) -> float:
    return (p1 * 0.30) + (p2 * 0.30) + (p3 * 0.40)

def determinarEstado(p1: float, p2: float, p3: float, final: float) -> str:
    if p1 < 50 or p2 < 50 or p3 < 50:
        return "Reprobado"
    elif final >= 70:
        return "Aprobado"
    else:
        return "Reprobado"

def mostrarResultado(final: float, estado: str) -> None:
    print(f"Calificación final: {final:.2f}")
    print(f"Estado: {estado}")
