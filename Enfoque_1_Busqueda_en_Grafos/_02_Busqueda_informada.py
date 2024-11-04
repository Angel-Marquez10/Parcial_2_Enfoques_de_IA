import heapq  # Biblioteca para implementar una cola de prioridad. Utiliza montículos para manejar datos en orden.

class Graph:
    def __init__(self):
        """Inicializa un grafo vacío.
        - graph: Diccionario que almacena los nodos y sus conexiones. 
        - heuristic: Diccionario que almacena los valores heurísticos de cada nodo.
        """
        
        # Diccionario para almacenar los nodos y sus conexiones. Las llaves son los nodos y los valores son listas de adyacencia.
        self.graph = {}  
        # Diccionario para almacenar la heurística de cada nodo (estimación del costo desde el nodo actual hasta el nodo objetivo).
        self.heuristic = {}  

    def add_edge(self, u, v, cost):
        """
        Agrega una arista (conexión) con un costo entre los nodos u y v.
        
        :param u: Nodo inicial.
        :param v: Nodo destino.
        :param cost: Costo asociado a la arista de u a v.
        """
        # Si el nodo u no existe en el grafo, inicializamos su lista de adyacencia.
        if u not in self.graph:
            self.graph[u] = []  # Inicializa la lista de nodos conectados a u.
        # Agrega la conexión desde u hasta v junto con su costo.
        self.graph[u].append((v, cost))

    def set_heuristic(self, node, value):
        """
        Establece la heurística para un nodo.
        
        :param node: Nodo al que se le asignará la heurística.
        :param value: Valor heurístico que se asignará.
        """
        # Guarda el valor heurístico para el nodo dado.
        self.heuristic[node] = value

    def a_star(self, start, goal):
        """
        Realiza la búsqueda A* desde el nodo inicial hasta el nodo objetivo.
        
        :param start: Nodo inicial para la búsqueda.
        :param goal: Nodo objetivo al que se desea llegar.
        :return: Lista con la ruta óptima desde el nodo inicial hasta el objetivo.
        """
        # Inicializa la cola de prioridad para almacenar nodos por explorar, comenzando con el nodo inicial.
        priority_queue = [(0, start)]  # La cola almacena tuplas (costo estimado total, nodo).
        # Diccionarios para llevar un registro del costo de la ruta y la ruta óptima encontrada.
        g_cost = {start: 0}  # Almacena el costo acumulado desde el nodo inicial.
        came_from = {start: None}  # Almacena el nodo previo en la ruta óptima.

        # Mientras la cola de prioridad no esté vacía.
        while priority_queue:
            # Extrae el nodo con el menor costo estimado.
            current_cost, current = heapq.heappop(priority_queue)
            print(f"Visitando: {current}")

            # Si el nodo actual es el objetivo, reconstruimos el camino completo.
            if current == goal:
                path = self._reconstruct_path(came_from, goal)
                print(f"¡Objetivo '{goal}' encontrado! Camino óptimo: {path}")
                return path

            # Recorre los vecinos del nodo actual.
            for neighbor, cost in self.graph.get(current, []):
                # Calcula el costo total tentativo del camino desde el nodo inicial hasta el vecino.
                tentative_g_cost = g_cost[current] + cost

                # Si encontramos un camino mejor al vecino o si aún no ha sido visitado.
                if neighbor not in g_cost or tentative_g_cost < g_cost[neighbor]:
                    # Actualiza el costo total para llegar al vecino.
                    g_cost[neighbor] = tentative_g_cost
                    # Calcula el costo estimado total (f_cost): costo acumulado + heurística.
                    f_cost = tentative_g_cost + self.heuristic.get(neighbor, float('inf'))
                    # Añade el vecino a la cola de prioridad con el nuevo costo estimado.
                    heapq.heappush(priority_queue, (f_cost, neighbor))
                    # Actualiza el diccionario que mantiene el camino óptimo.
                    came_from[neighbor] = current

        # Si el objetivo no se encuentra, se retorna None.
        print("No se encontró un camino al objetivo.")
        return None

    def _reconstruct_path(self, came_from, current):
        """
        Reconstruye el camino óptimo desde el nodo inicial hasta el nodo objetivo.
        
        :param came_from: Diccionario que contiene el nodo previo en el camino óptimo para cada nodo.
        :param current: Nodo objetivo desde el cual reconstruir la ruta.
        :return: Lista con la secuencia de nodos que forman el camino óptimo.
        """
        # Inicializa la lista que contendrá la ruta desde el nodo inicial al objetivo.
        path = []
        # Se recorre desde el nodo objetivo hasta el nodo inicial siguiendo los nodos previos.
        while current is not None:
            path.append(current)  # Agrega el nodo actual a la ruta.
            current = came_from[current]  # Mueve al nodo previo.
        path.reverse()  # Invierte la lista para que vaya del inicio al objetivo.
        return path

# Ejemplo de uso del algoritmo A*
if __name__ == "__main__":
    # Crear una nueva instancia del grafo.
    g = Graph()
    
    # Agregar aristas al grafo (nodos y conexiones con costos).
    g.add_edge('A', 'B', 1)  # Nodo A conectado a B con costo 1.
    g.add_edge('A', 'C', 4)  # Nodo A conectado a C con costo 4.
    g.add_edge('B', 'D', 2)  # Nodo B conectado a D con costo 2.
    g.add_edge('B', 'E', 5)  # Nodo B conectado a E con costo 5.
    g.add_edge('C', 'F', 3)  # Nodo C conectado a F con costo 3.
    g.add_edge('D', 'G', 1)  # Nodo D conectado a G con costo 1.
    g.add_edge('E', 'G', 2)  # Nodo E conectado a G con costo 2.
    g.add_edge('F', 'G', 6)  # Nodo F conectado a G con costo 6.

    # Definir las heurísticas de cada nodo (estimación de costo al objetivo G).
    g.set_heuristic('A', 7)
    g.set_heuristic('B', 6)
    g.set_heuristic('C', 5)
    g.set_heuristic('D', 3)
    g.set_heuristic('E', 4)
    g.set_heuristic('F', 2)
    g.set_heuristic('G', 0)  # La heurística del objetivo siempre es 0.

    # Ejecución del algoritmo A* desde A hasta G.
    print("Búsqueda A* (Heurística):")
    g.a_star('A', 'G')

