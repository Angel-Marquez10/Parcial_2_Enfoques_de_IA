class Graph:
    def __init__(self):
        """Inicializa un grafo vacío."""
        self.graph = {}  # Diccionario que almacenará el grafo

    def add_edge(self, u, v):
        """Agrega una arista entre los nodos u y v al grafo."""
        # Si el nodo u no existe en el grafo, lo creamos con una lista vacía
        if u not in self.graph:
            self.graph[u] = []  # Inicializa la lista de adyacencia de u
        # Agrega v a la lista de adyacencia de u (u -> v)
        self.graph[u].append(v)

    def dfs(self, start, goal):
        """Realiza una búsqueda en profundidad (DFS) desde el nodo inicial (start) hasta el objetivo (goal)."""
        visited = set()  # Conjunto para llevar un registro de los nodos visitados
        # Inicia la búsqueda recursiva
        return self._dfs_recursive(start, goal, visited)

    def _dfs_recursive(self, current, goal, visited):
        """Función recursiva que realiza la búsqueda en profundidad (DFS)."""
        # Marca el nodo actual como visitado
        visited.add(current)  
        print(f"Visitando: {current}")  # Imprime el nodo actual que está siendo visitado

        # Si el nodo actual es el objetivo, retorna True
        if current == goal:
            print(f"¡Objetivo '{goal}' encontrado!")  # Mensaje si se encuentra el objetivo
            return True

        # Recorre los nodos vecinos del nodo actual
        for neighbor in self.graph.get(current, []):  # Obtiene los vecinos de current
            if neighbor not in visited:  # Si el vecino no ha sido visitado
                # Llama recursivamente a la función para continuar la búsqueda
                if self._dfs_recursive(neighbor, goal, visited):
                    return True  # Si se encontró el objetivo en la recursión
        return False  # Si no se encontró el objetivo en esta ruta

    def bfs(self, start, goal):
        """Realiza una búsqueda en amplitud (BFS) desde el nodo inicial (start) hasta el objetivo (goal)."""
        visited = set()  # Conjunto para llevar un registro de los nodos visitados
        cola = [start]  # Cola para almacenar los nodos a explorar (inicialmente solo el nodo start)

        # Mientras haya nodos en la cola
        while cola:
            current = cola.pop(0)  # Extrae el primer nodo de la cola
            print(f"Visitando: {current}")  # Imprime el nodo actual que está siendo visitado

            # Si el nodo actual es el objetivo, retorna True
            if current == goal:
                print(f"¡Objetivo '{goal}' encontrado!")  # Mensaje si se encuentra el objetivo
                return True  # Se encontró el objetivo

            # Marca el nodo actual como visitado
            visited.add(current)

            # Recorre los nodos vecinos del nodo actual
            for neighbor in self.graph.get(current, []):  # Obtiene los vecinos de current
                # Si el vecino no ha sido visitado y no está ya en la cola
                if neighbor not in visited and neighbor not in cola:
                    cola.append(neighbor)  # Agrega el vecino a la cola para su posterior exploración
        return False  # Si no se encontró el objetivo en toda la búsqueda

# Ejemplo de uso
if __name__ == "__main__":
    g = Graph()  # Crear una nueva instancia del grafo
    # Agregar aristas al grafo (conexiones entre nodos)
    g.add_edge('A', 'B')  # A está conectado a B
    g.add_edge('A', 'C')  # A está conectado a C
    g.add_edge('B', 'D')  # B está conectado a D
    g.add_edge('B', 'E')  # B está conectado a E
    g.add_edge('C', 'F')  # C está conectado a F
    g.add_edge('E', 'G')  # E está conectado a G

    # Ejecución de la búsqueda en profundidad (DFS)
    print("Búsqueda en Profundidad (DFS):")
    g.dfs('A', 'G')  # Ejecutar DFS desde A hasta G

    # Ejecución de la búsqueda en amplitud (BFS)
    print("\nBúsqueda en Amplitud (BFS):")
    g.bfs('A', 'G')  # Ejecutar BFS desde A hasta G
