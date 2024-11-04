def print_board(board):
    """Imprime el tablero de ajedrez de las reinas."""
    for row in board:
        print(" ".join(row))
    print("\n")


def is_safe(board, row, col):
    """Verifica si es seguro colocar una reina en board[row][col]."""
    n = len(board)

    # Verifica la columna
    for i in range(n):
        if board[i][col] == 'Q':
            return False

    # Verifica la diagonal superior izquierda
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 'Q':
            return False

    # Verifica la diagonal inferior izquierda
    for i, j in zip(range(row, n), range(col, -1, -1)):
        if board[i][j] == 'Q':
            return False

    return True


def solve_n_queens(board, col):
    """Resuelve el problema de las N-Reinas utilizando búsqueda de vuelta atrás."""
    n = len(board)
    if col >= n:
        print("Solución encontrada:")
        print_board(board)
        return True

    for i in range(n):
        if is_safe(board, i, col):
            board[i][col] = 'Q'  # Coloca una reina
            print(f"Colocando reina en ({i}, {col})")
            if solve_n_queens(board, col + 1):
                return True  # Si se encontró una solución, no retroceder
            board[i][col] = '.'  # Retrocede (backtrack)
            print(f"Retrocediendo de ({i}, {col})")

    return False


def n_queens(n):
    """Inicializa el tablero y comienza la solución del problema de las N-Reinas."""
    board = [['.' for _ in range(n)] for _ in range(n)]  # Crea un tablero vacío
    if not solve_n_queens(board, 0):
        print("No se encontró solución para N =", n)


# Ejemplo de uso
if __name__ == "__main__":
    n = 4  # Cambia el valor de N para diferentes tamaños del tablero
    n_queens(n)
