"""""
el problema de los 8 reyes. Este problema consiste en colocar 8 reyes en un tablero de ajedrez 
de manera que no se amenacen entre sí. La búsqueda en profundidad limitada se puede utilizar para 
explorar las diferentes configuraciones del tablero.
"""
# Definimos el tamaño del tablero y el número de reyes
N = 8  # Tamaño del tablero (8x8)
K = 8  # Número de reyes a colocar

def is_safe(board, row, col):
    """
    Verifica si se puede colocar un rey en la posición (row, col).
    Args:
    - board: el tablero de ajedrez.
    - row: fila donde se quiere colocar el rey.
    - col: columna donde se quiere colocar el rey.

    Returns:
    - True si es seguro colocar el rey, False de lo contrario.
    """
    # Verificar fila
    for j in range(N):
        if board[row][j] == 1:
            return False

    # Verificar columna
    for i in range(N):
        if board[i][col] == 1:
            return False

    # Verificar las dos diagonales
    for i in range(N):
        for j in range(N):
            if abs(row - i) == abs(col - j) and board[i][j] == 1:
                return False

    return True  # Es seguro colocar el rey

def depth_first_search_limited(board, row, col, count, limit):
    """
    Implementa la búsqueda en profundidad limitada para colocar los reyes en el tablero.
    Args:
    - board: el tablero de ajedrez.
    - row: fila actual en la que se intentan colocar reyes.
    - col: columna actual en la que se intentan colocar reyes.
    - count: cantidad de reyes colocados hasta ahora.
    - limit: número máximo de reyes a colocar.

    Returns:
    - True si se coloca todos los reyes, False de lo contrario.
    """
    # Si hemos colocado todos los reyes, terminamos la búsqueda
    if count == limit:
        return True

    # Intentamos colocar un rey en cada posición del tablero
    for i in range(row, N):
        for j in range(col if i == row else 0, N):
            if is_safe(board, i, j):  # Verificamos si es seguro colocar el rey
                board[i][j] = 1  # Colocamos el rey
                print(f"Colocando rey en: ({i}, {j}), Reinas colocadas: {count + 1}")  # Mensaje informativo

                # Realizamos la búsqueda en profundidad para el siguiente rey
                if depth_first_search_limited(board, i, j + 1, count + 1, limit):
                    return True  # Si se coloca el rey, retornamos True

                # Si no se puede colocar, retiramos el rey
                board[i][j] = 0  # Retiramos el rey
                print(f"Retirando rey de: ({i}, {j}), Volviendo atrás")  # Mensaje informativo

    return False  # No se pudo colocar el rey

# Inicializamos el tablero vacío
board = [[0 for _ in range(N)] for _ in range(N)]

# Ejecutamos la búsqueda en profundidad limitada para colocar los reyes
if depth_first_search_limited(board, 0, 0, 0, K):
    print("Se logró colocar los reyes en el tablero:")
    for row in board:
        print(row)  # Mostramos el tablero final
else:
    print("No se pudo colocar a los reyes en el tablero.")
