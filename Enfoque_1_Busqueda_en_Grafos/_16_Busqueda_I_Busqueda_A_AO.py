import heapq

class Node:
    def __init__(self, name, parent=None, g=0, h=0):
        """Inicializa un nodo con su nombre, padre, costo g y heurística h."""
        self.name = name
        self.parent = parent  # Nodo padre para reconstruir el camino
        self.g = g  # Costo desde el nodo inicial
        self.h = h  # Heurística
        self.f = g + h  # Costo total (g + h)

    def __lt__(self, other):
        """Permite comparar nodos basados en su costo total f."""
        return self.f < other.f

def a_star_search(graph, start, goal):
    """Implementa la búsqueda A* para encontrar el camino al objetivo."""
    open_set = []  # Cola de prioridad para nodos a explorar
    closed_set = set()  # Conjunto de nodos ya explorados

    # Inicializar el nodo de inicio
    start_node = Node(start, None, 0, graph[start]['heuristic'])
    heapq.heappush(open_set, start_node)  # Añadir nodo de inicio a la cola

    print(f"Iniciando búsqueda A* desde '{start}' hacia '{goal}'.")

    while open_set:
        # Extraer el nodo con el menor costo total f
        current_node = heapq.heappop(open_set)
        print(f"\nExplorando nodo: {current_node.name} | Costo g: {current_node.g} | Heurística h: {current_node.h} | Costo total f: {current_node.f}")

        if current_node.name == goal:  # Si se alcanza el objetivo
            print("\n¡Objetivo alcanzado!")
            return reconstruct_path(current_node)  # Retornar el camino

        closed_set.add(current_node.name)  # Marcar el nodo actual como explorado

        # Explorar los vecinos del nodo actual
        for neighbor_name, cost in graph[current_node.name]['neighbors'].items():
            if neighbor_name in closed_set:
                print(f"  - El vecino '{neighbor_name}' ya fue explorado. Ignorando.")
                continue

            # Calcular el costo g para el vecino
            neighbor_g = current_node.g + cost
            neighbor_h = graph[neighbor_name]['heuristic']
            neighbor_node = Node(neighbor_name, current_node, neighbor_g, neighbor_h)

            # Agregar el vecino a la cola de abiertos
            heapq.heappush(open_set, neighbor_node)
            print(f"  - Agregando vecino '{neighbor_name}' a la cola de exploración con costo g: {neighbor_g}, heurística h: {neighbor_h}, costo total f: {neighbor_node.f}.")

    print("\nNo se encontró un camino hacia el objetivo.")
    return None  # No se encontró un camino

def reconstruct_path(node):
    """Reconstruye el camino desde el nodo objetivo hasta el nodo inicial."""
    path = []
    while node:
        path.append(node.name)
        node = node.parent
    return path[::-1]  # Retornar el camino invertido

# Definir el grafo como un diccionario que incluye heurísticas
graph = {
    'A': {'neighbors': {'B': 1, 'C': 4}, 'heuristic': 7},
    'B': {'neighbors': {'A': 1, 'D': 2, 'E': 2}, 'heuristic': 6},
    'C': {'neighbors': {'A': 4, 'F': 1}, 'heuristic': 2},
    'D': {'neighbors': {'B': 2, 'G': 3}, 'heuristic': 1},
    'E': {'neighbors': {'B': 2, 'G': 1}, 'heuristic': 0},
    'F': {'neighbors': {'C': 1, 'G': 3}, 'heuristic': 1},
    'G': {'neighbors': {'D': 3, 'E': 1, 'F': 3}, 'heuristic': 0}  # G es el objetivo
}

# Definir nodo de inicio y nodo objetivo
start = 'A'  # Nodo de inicio
goal = 'G'   # Nodo objetivo

# Ejecutar la búsqueda A*
print("Ejecutando la búsqueda A*...")
result = a_star_search(graph, start, goal)

# Mostrar el resultado final
if result:
    print(f"\nSe alcanzó el objetivo: {' -> '.join(result)}")
else:
    print("No se encontró un camino.")
