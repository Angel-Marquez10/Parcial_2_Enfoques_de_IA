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


def forward_checking(board, row, col, domain):
    """Verifica si la asignación de una reina afecta el dominio de las variables restantes."""
    n = len(board)

    # Actualiza el dominio de las variables no asignadas
    for r in range(n):
        if is_safe(board, r, col):
            domain[col].append(r)  # Añade posición válida al dominio

    # Elimina valores inconsistente del dominio de las columnas restantes
    for c in range(col + 1, n):
        new_domain = []
        for r in domain[c]:
            if is_safe(board, r, c):
                new_domain.append(r)
        domain[c] = new_domain

    return domain


def solve_n_queens(board, col, domain):
    """Resuelve el problema de las N-Reinas utilizando comprobación hacia delante."""
    n = len(board)
    if col >= n:
        print("Solución encontrada:")
        print_board(board)
        return True

    for row in domain[col]:
        board[row][col] = 'Q'  # Coloca una reina
        print(f"Colocando reina en ({row}, {col})")

        # Realiza la comprobación hacia delante
        new_domain = forward_checking(board, row, col, domain)

        if solve_n_queens(board, col + 1, new_domain):
            return True  # Si se encontró una solución, no retroceder
        
        board[row][col] = '.'  # Retrocede (backtrack)
        print(f"Retrocediendo de ({row}, {col})")

    return False


def n_queens(n):
    """Inicializa el tablero y comienza la solución del problema de las N-Reinas."""
    board = [['.' for _ in range(n)] for _ in range(n)]  # Crea un tablero vacío
    domain = [[] for _ in range(n)]  # Inicializa el dominio de cada columna

    # Inicializa el dominio con todas las posiciones válidas
    for c in range(n):
        domain[c] = list(range(n))

    if not solve_n_queens(board, 0, domain):
        print("No se encontró solución para N =", n)


# Ejemplo de uso
if __name__ == "__main__":
    n = 4  # Cambia el valor de N para diferentes tamaños del tablero
    n_queens(n)
