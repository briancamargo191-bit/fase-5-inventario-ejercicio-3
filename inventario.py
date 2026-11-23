# Fase 5 - Evaluación Final POA
# Problema 3: Reabastecimiento de inventario

# Matriz de inventario: [código, nombre, stock actual, stock mínimo]
inventario = [
    ["A001", "Cuaderno", 15, 20],
    ["A002", "Lápiz", 50, 30],
    ["A003", "Borrador", 8, 10],
    ["A004", "Regla", 25, 25],
    ["A005", "Marcador", 3, 12],
    ["A006", "Carpeta", 40, 15],
]


def calcular_pedido(stock_actual, stock_minimo):
    """Devuelve la cantidad exacta a pedir de un artículo."""
    if stock_actual < stock_minimo:
        return stock_minimo - stock_actual
    else:
        return 0


def mostrar_reporte(matriz):
    """Recorre la matriz y muestra la cantidad a pedir de cada artículo."""
    print("=== REPORTE DE REABASTECIMIENTO ===")
    for fila in matriz:
        codigo = fila[0]
        nombre = fila[1]
        stock_actual = fila[2]
        stock_minimo = fila[3]

        cantidad = calcular_pedido(stock_actual, stock_minimo)
        print(f"{nombre}: pedir {cantidad} unidades")


mostrar_reporte(inventario)