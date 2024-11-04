# Definimos el laberinto como una matriz donde:
# 0 representa caminos libres, y 1 representa paredes
maze = [
    [0, 1, 0, 0, 0, 0],
    [0, 1, 0, 1, 1, 0],
    [0, 0, 0, 1, 0, 0],
    [0, 1, 0, 0, 0, 1],
    [0, 0, 0, 1, 1, 0],
    [0, 1, 0, 0, 0, 0]
]

# Definimos las direcciones posibles de movimiento (arriba, abajo, izquierda, derecha)
directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # (row_change, col_change)

def is_valid_move(maze, visited, row, col):
    """
    Verifica si el movimiento es válido.
    Args:
    - maze: la matriz del laberinto.
    - visited: conjunto de posiciones visitadas.
    - row: fila del movimiento.
    - col: columna del movimiento.

    Returns:
    - True si el movimiento es válido, False de lo contrario.
    """
    return (0 <= row < len(maze) and 
            0 <= col < len(maze[0]) and 
            maze[row][col] == 0 and 
            (row, col) not in visited)

def depth_first_search_maze(maze, start, goal):
    """
    Implementa la búsqueda en profundidad para encontrar un camino en un laberinto.
    Args:
    - maze: matriz que representa el laberinto.
    - start: posición inicial (fila, columna).
    - goal: posición objetivo (fila, columna).

    Returns:
    - path: lista que contiene el camino encontrado desde start hasta goal.
    """
    stack = [start]  # Pila para los nodos a explorar
    visited = set()  # Conjunto para los nodos visitados
    parent = {start: None}  # Diccionario para rastrear el camino

    print(f"Iniciando búsqueda en profundidad desde {start} hasta {goal}")

    while stack:
        current_node = stack.pop()  # Sacamos el último nodo de la pila

        # Si encontramos el objetivo, reconstruimos el camino
        if current_node == goal:
            print(f"Meta alcanzada: {current_node}")
            break

        if current_node not in visited:  # Si el nodo no ha sido visitado
            print(f"Visitando: {current_node}")
            visited.add(current_node)  # Marcamos el nodo como visitado

            # Probar todos los movimientos posibles
            for direction in directions:
                next_row = current_node[0] + direction[0]
                next_col = current_node[1] + direction[1]
                next_node = (next_row, next_col)

                if is_valid_move(maze, visited, next_row, next_col):
                    stack.append(next_node)  # Agregamos el siguiente nodo a la pila
                    parent[next_node] = current_node  # Establecemos el padre del nodo

    # Reconstruimos el camino si se ha encontrado
    if goal in parent:
        path = reconstruct_path(parent, start, goal)
        return path  # Retornamos el camino encontrado
    else:
        return None  # No se encontró un camino

def reconstruct_path(parent, start, goal):
    """
    Reconstruye el camino desde el nodo objetivo hasta el nodo de inicio.
    Args:
    - parent: diccionario que muestra el camino hacia atrás.
    - start: posición inicial.
    - goal: posición objetivo.

    Returns:
    - path: lista que contiene el camino encontrado.
    """
    path = []
    current = goal  # Comenzamos desde el nodo objetivo

    while current is not None:
        path.append(current)  # Agregamos el nodo actual al camino
        current = parent[current]  # Retrocedemos al nodo padre

    path.reverse()  # Invertimos el camino para que esté desde el inicio al objetivo
    return path  # Retornamos el camino

# Definimos las posiciones de inicio y objetivo
start_position = (0, 0)  # Nodo inicial en la esquina superior izquierda
goal_position = (5, 5)   # Nodo objetivo en la esquina inferior derecha

# Ejecutamos la búsqueda en profundidad en el laberinto
path_found = depth_first_search_maze(maze, start_position, goal_position)

# Mostramos el camino encontrado o un mensaje si no se encontró
if path_found:
    print("Camino encontrado:", path_found)  # Mostramos el camino encontrado
else:
    print("No se encontró un camino hacia el nodo objetivo.")
