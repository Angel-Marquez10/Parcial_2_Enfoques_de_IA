class Graph:
    def __init__(self):
        """Inicializa un grafo vacío."""
        self.graph = {}  # Diccionario para almacenar el grafo

    def add_edge(self, u, v):
        """Agrega una arista entre los nodos u y v."""
        if u not in self.graph:
            self.graph[u] = []
        if v not in self.graph:
            self.graph[v] = []
        self.graph[u].append(v)  # Añadir v a la lista de vecinos de u
        self.graph[v].append(u)  # Añadir u a la lista de vecinos de v (grafo no dirigido)

    def iterative_deepening_dfs(self, start, goal):
        """
        Realiza la búsqueda en profundidad iterativa para encontrar un camino
        desde el nodo inicial hasta el nodo objetivo.
        
        Args:
        - start: Nodo inicial.
        - goal: Nodo objetivo.

        Returns:
        - Una lista de nodos que representan el camino o None si no se encontró.
        """
        depth = 0  # Profundidad inicial

        while True:
            print(f"Buscando solución con profundidad máxima: {depth}")
            found_path = self.depth_limited_dfs(start, goal, depth, visited=set(), path=[])
            if found_path:  # Si se encontró un camino
                return found_path
            depth += 1  # Incrementar la profundidad

    def depth_limited_dfs(self, current, goal, depth, visited, path):
        """
        Realiza la búsqueda en profundidad limitada desde el nodo actual.
        
        Args:
        - current: Nodo actual.
        - goal: Nodo objetivo.
        - depth: Profundidad máxima permitida.
        - visited: Conjunto de nodos visitados.
        - path: Lista que almacena el camino actual.

        Returns:
        - Una lista de nodos que representan el camino o None si no se encontró.
        """
        visited.add(current)  # Marcar el nodo actual como visitado
        path.append(current)  # Añadir el nodo actual al camino

        if current == goal:  # Si se ha alcanzado el nodo objetivo
            return path  # Retornar el camino encontrado

        if depth > 0:  # Solo profundiza si no hemos alcanzado la profundidad máxima
            for neighbor in self.graph.get(current, []):  # Obtener vecinos del nodo actual
                if neighbor not in visited:  # Evitar ciclos
                    result = self.depth_limited_dfs(neighbor, goal, depth - 1, visited, path)
                    if result:  # Si encontramos un camino
                        return result

        path.pop()  # Retroceder si no se encuentra un camino
        return None  # No se encontró un camino

# Crear un grafo y agregar aristas
graph = Graph()
graph.add_edge('A', 'B')
graph.add_edge('A', 'C')
graph.add_edge('B', 'D')
graph.add_edge('C', 'E')
graph.add_edge('D', 'E')
graph.add_edge('E', 'F')
graph.add_edge('B', 'F')

# Definir nodo inicial y nodo objetivo
start_node = 'A'
goal_node = 'F'

# Ejecutar la búsqueda en profundidad iterativa
result_path = graph.iterative_deepening_dfs(start_node, goal_node)

# Mostrar el resultado final
if result_path:
    print(f"Se encontró un camino desde {start_node} hasta {goal_node}: {' -> '.join(result_path)}")
else:
    print(f"No se encontró un camino desde {start_node} hasta {goal_node}.")
