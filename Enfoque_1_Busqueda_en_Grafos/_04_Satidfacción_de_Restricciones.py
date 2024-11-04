# Configuración del problema de las N-Reinas
N = 8  # Tamaño del tablero, es decir, queremos encontrar una solución para 8 reinas en un tablero 8x8

# Función para verificar si la posición actual es segura para colocar una reina
# Las restricciones incluyen que no haya otras reinas en la misma columna ni en las diagonales
def is_safe(board, row, col):
    # Verificar que no haya otra reina en la misma columna
    for i in range(row):
        if board[i] == col:
            return False
    
    # Verificar que no haya otra reina en la diagonal superior izquierda
    for i, j in zip(range(row - 1, -1, -1), range(col - 1, -1, -1)):
        if board[i] == j:
            return False

    # Verificar que no haya otra reina en la diagonal superior derecha
    for i, j in zip(range(row - 1, -1, -1), range(col + 1, N)):
        if board[i] == j:
            return False

    return True

# Función principal de búsqueda en profundidad con retroceso para resolver el problema
def solve_n_queens(board, row):
    # Caso base: si colocamos reinas en todas las filas, se encontró una solución
    if row == N:
        # Imprimir el tablero con la solución encontrada
        print_board(board)
        return True
    
    # Intentamos colocar una reina en cada columna de la fila actual
    for col in range(N):
        if is_safe(board, row, col):  # Verificamos si la posición es segura
            board[row] = col  # Colocamos la reina en la columna actual
            # Continuamos con la siguiente fila
            if solve_n_queens(board, row + 1):  # Llamada recursiva
                return True  # Si encontramos una solución, terminamos
            board[row] = -1  # Si no es solución, quitamos la reina (backtracking)

    return False  # Si no encontramos solución en ninguna columna, retrocedemos

# Función para imprimir el tablero en una solución encontrada
def print_board(board):
    print("Solución encontrada para el problema de las N-Reinas:")
    for i in range(N):
        row = ["." for _ in range(N)]  # Creamos una fila vacía
        if board[i] != -1:  # Si hay una reina en la posición
            row[board[i]] = "Q"  # Colocamos la reina en la columna correspondiente
        print(" ".join(row))  # Mostramos la fila del tablero
    print("\n")  # Nueva línea entre soluciones

# Crear un tablero vacío representado por una lista de tamaño N, inicializado en -1
# -1 indica que aún no se ha colocado ninguna reina en esa fila
board = [-1] * N

# Ejecutamos la solución
solve_n_queens(board, 0)
