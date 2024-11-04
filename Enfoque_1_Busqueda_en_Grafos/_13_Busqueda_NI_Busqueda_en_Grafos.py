class Graph:
    def __init__(self):
        """Inicializa un grafo vacío."""
        self.graph = {}  # Diccionario para almacenar el grafo

    def add_edge(self, node1, node2):
        """Agrega una arista entre node1 y node2."""
        if node1 not in self.graph:
            self.graph[node1] = []
        if node2 not in self.graph:
            self.graph[node2] = []
        self.graph[node1].append(node2)  # Añadir node2 a la lista de vecinos de node1
        self.graph[node2].append(node1)  # Añadir node1 a la lista de vecinos de node2 (grafo no dirigido)

    def depth_first_search(self, start, goal):
        """
        Realiza la búsqueda en profundidad desde el nodo de inicio hasta el nodo objetivo.
        
        Args:
        - start: Nodo de inicio.
        - goal: Nodo objetivo.

        Returns:
        - Una lista de nodos que representa el camino o None si no se encontró.
        """
        visited = set()  # Conjunto para almacenar nodos visitados
        path = []  # Lista para almacenar el camino encontrado

        def dfs(current):
            """Función auxiliar para realizar DFS recursivo."""
            visited.add(current)  # Marcar el nodo actual como visitado
            path.append(current)  # Agregar el nodo actual al camino

            if current == goal:
                return True  # Si se alcanza el nodo objetivo, se encontró el camino

            for neighbor in self.graph.get(current, []):  # Obtener vecinos
                if neighbor not in visited:  # Si el vecino no ha sido visitado
                    if dfs(neighbor):  # Realiza DFS en el vecino
                        return True  # Si se encontró el camino en la recursión

            path.pop()  # Si no se encontró el camino, eliminar el nodo actual del camino
            return False  # No se encontró el camino en esta ruta

        dfs(start)  # Comenzar la búsqueda en profundidad
        return path if goal in visited else None  # Retornar el camino si se encontró el objetivo

# Crear un grafo y agregar aristas
graph = Graph()
graph.add_edge('A', 'B')
graph.add_edge('A', 'C')
graph.add_edge('B', 'D')
graph.add_edge('B', 'E')
graph.add_edge('C', 'F')
graph.add_edge('D', 'G')
graph.add_edge('E', 'H')
graph.add_edge('F', 'I')

# Definir nodo de inicio y nodo objetivo
start_node = 'A'
goal_node = 'H'

# Ejecutar búsqueda en profundidad
result_path = graph.depth_first_search(start_node, goal_node)

# Mostrar el resultado final
if result_path:
    print(f"Se encontró un camino desde {start_node} hasta {goal_node}: {' -> '.join(result_path)}")
else:
    print(f"No se encontró un camino desde {start_node} hasta {goal_node}.")
