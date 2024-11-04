class Node:
    def __init__(self, name, heuristic=0):
        """Inicializa un nodo con su nombre y su valor heurístico."""
        self.name = name
        self.heuristic = heuristic

    def __lt__(self, other):
        """Permite comparar nodos basados en su valor heurístico."""
        return self.heuristic < other.heuristic

def greedy_best_first_search(graph, start, goal):
    """Implementa la búsqueda voraz primero el mejor para encontrar el camino al objetivo."""
    open_set = []  # Cola de prioridad para nodos a explorar
    closed_set = set()  # Conjunto de nodos ya explorados

    # Inicializar el nodo de inicio
    start_node = Node(start, graph[start]['heuristic'])
    open_set.append(start_node)

    print(f"Iniciando búsqueda desde '{start}' hacia '{goal}'.")

    while open_set:
        # Extraer el nodo con la mejor heurística
        current_node = min(open_set, key=lambda node: node.heuristic)
        open_set.remove(current_node)
        print(f"\nExplorando nodo: {current_node.name} | Heurística: {current_node.heuristic}")

        if current_node.name == goal:  # Si se alcanza el objetivo
            print("\n¡Objetivo alcanzado!")
            return current_node.name  # Retornar el objetivo

        closed_set.add(current_node.name)  # Marcar el nodo actual como explorado

        # Explorar los vecinos del nodo actual
        for neighbor in graph[current_node.name]['neighbors']:
            if neighbor in closed_set:
                print(f"  - El vecino '{neighbor}' ya fue explorado. Ignorando.")
                continue

            # Crear un nuevo nodo para el vecino
            neighbor_node = Node(neighbor, graph[neighbor]['heuristic'])
            open_set.append(neighbor_node)
            print(f"  - Agregando vecino '{neighbor}' a la cola de exploración con heurística {neighbor_node.heuristic}.")

    print("\nNo se encontró un camino hacia el objetivo.")
    return None  # No se encontró un camino

# Definir el grafo como un diccionario que incluye heurísticas
graph = {
    'A': {'neighbors': ['B', 'C'], 'heuristic': 7},
    'B': {'neighbors': ['A', 'D', 'E'], 'heuristic': 6},
    'C': {'neighbors': ['A', 'F'], 'heuristic': 2},
    'D': {'neighbors': ['B', 'G'], 'heuristic': 1},
    'E': {'neighbors': ['B', 'G'], 'heuristic': 0},
    'F': {'neighbors': ['C', 'G'], 'heuristic': 1},
    'G': {'neighbors': ['D', 'E', 'F'], 'heuristic': 0}  # G es el objetivo
}

# Definir nodo de inicio y nodo objetivo
start = 'A'  # Nodo de inicio
goal = 'G'   # Nodo objetivo

# Ejecutar la búsqueda voraz primero el mejor
print("Ejecutando la búsqueda voraz primero el mejor...")
result = greedy_best_first_search(graph, start, goal)

# Mostrar el resultado final
if result:
    print(f"\nSe alcanzó el objetivo: {result}")
else:
    print("No se encontró un camino.")
