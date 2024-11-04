import heapq

class Node:
    def __init__(self, position):
        """Inicializa un nodo con su posición en la cuadrícula."""
        self.position = position  # (x, y)
        self.g = 0  # Costo desde el inicio hasta este nodo
        self.h = 0  # Heurística (estimación del costo hasta el objetivo)
        self.f = 0  # Costo total (g + h)
        self.parent = None  # Nodo padre en el camino

    def __lt__(self, other):
        """Permite comparar nodos basados en el costo total (f) para la cola de prioridad."""
        return self.f < other.f

def heuristic(a, b):
    """Calcula la distancia Manhattan entre dos puntos."""
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def a_star(grid, start, goal):
    """Ejecuta el algoritmo A* para encontrar el camino más corto en una cuadrícula."""
    open_set = []  # Cola de prioridad para nodos a explorar
    closed_set = set()  # Conjunto de nodos ya explorados

    start_node = Node(start)  # Crear nodo de inicio
    goal_node = Node(goal)     # Crear nodo objetivo

    # Inicializar el nodo de inicio
    start_node.g = 0
    start_node.h = heuristic(start_node.position, goal_node.position)
    start_node.f = start_node.g + start_node.h

    heapq.heappush(open_set, start_node)  # Agregar nodo inicial a la cola de prioridad
    print(f"Inicio en: {start} | Objetivo en: {goal}")

    while open_set:
        current_node = heapq.heappop(open_set)  # Extraer el nodo con el costo total más bajo
        print(f"\nExplorando nodo: {current_node.position} | Costo total (f): {current_node.f}")

        if current_node.position == goal_node.position:  # Si se alcanza el objetivo
            print("\n¡Objetivo alcanzado!")
            return reconstruct_path(current_node)  # Retornar el camino

        closed_set.add(current_node.position)  # Marcar el nodo actual como explorado

        # Generar vecinos (celdas adyacentes)
        neighbors = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # Derecha, Abajo, Izquierda, Arriba
        for new_position in neighbors:
            node_position = (current_node.position[0] + new_position[0], current_node.position[1] + new_position[1])

            # Verificar que la nueva posición esté dentro de los límites de la cuadrícula
            if (0 <= node_position[0] < len(grid)) and (0 <= node_position[1] < len(grid[0])):
                # Verificar que la nueva posición no sea un obstáculo
                if grid[node_position[0]][node_position[1]] == 1:  # 1 representa un obstáculo
                    print(f"  - Posición {node_position} es un obstáculo. Ignorando.")
                    continue

                # Crear un nuevo nodo vecino
                neighbor_node = Node(node_position)

                if neighbor_node.position in closed_set:  # Si el vecino ya fue explorado, ignorar
                    print(f"  - Posición {node_position} ya fue explorada. Ignorando.")
                    continue

                # Cálculo del costo
                tentative_g = current_node.g + 1  # El costo para moverse a la celda vecina es 1
                if tentative_g < neighbor_node.g or neighbor_node.g == 0:  # Si el nuevo costo es mejor
                    neighbor_node.parent = current_node  # Establecer el nodo padre
                    neighbor_node.g = tentative_g  # Actualizar el costo
                    neighbor_node.h = heuristic(neighbor_node.position, goal_node.position)  # Actualizar heurística
                    neighbor_node.f = neighbor_node.g + neighbor_node.h  # Actualizar costo total
                    print(f"  - Evaluando vecino: {neighbor_node.position} | g: {neighbor_node.g}, h: {neighbor_node.h}, f: {neighbor_node.f}")

                    if neighbor_node not in open_set:  # Agregar el vecino a la cola si no está
                        heapq.heappush(open_set, neighbor_node)
                        print(f"  - Agregando {neighbor_node.position} a la cola de exploración.")

    print("\nNo se encontró un camino hacia el objetivo.")
    return None  # No se encontró un camino

def reconstruct_path(current_node):
    """Reconstruye el camino desde el nodo objetivo hasta el inicio."""
    path = []
    while current_node:
        path.append(current_node.position)  # Agregar la posición del nodo al camino
        current_node = current_node.parent  # Retroceder al nodo padre
    return path[::-1]  # Retornar el camino en orden correcto

# Definir la cuadrícula (0 = espacio libre, 1 = obstáculo)
grid = [
    [0, 0, 0, 1, 0, 0],
    [0, 1, 0, 1, 0, 1],
    [0, 0, 0, 0, 0, 0],
    [0, 1, 1, 1, 1, 0],
    [0, 0, 0, 0, 0, 0],
    [1, 0, 1, 1, 1, 0]
]

# Definir nodo de inicio y nodo objetivo
start = (0, 0)  # Esquina superior izquierda
goal = (5, 5)   # Esquina inferior derecha

# Ejecutar algoritmo A*
print("Ejecutando el algoritmo A*...")
result_path = a_star(grid, start, goal)

# Mostrar el resultado final
if result_path:
    print("\nSe encontró un camino:")
    for step in result_path:
        print(step)
else:
    print("No se encontró un camino.")
