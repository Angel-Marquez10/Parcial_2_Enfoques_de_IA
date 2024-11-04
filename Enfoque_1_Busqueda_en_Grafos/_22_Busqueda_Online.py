import heapq

class Graph:
    def __init__(self):
        """Inicializa el grafo como un diccionario."""
        self.nodes = {}  # Un diccionario que almacena los nodos y sus vecinos

    def add_edge(self, from_node, to_node, cost):
        """Agrega un arco al grafo con un coste asociado."""
        if from_node not in self.nodes:
            self.nodes[from_node] = []
        self.nodes[from_node].append((to_node, cost))

    def online_search(self, start, goal):
        """Realiza una búsqueda online desde el nodo inicial hasta el nodo objetivo."""
        print(f"Iniciando búsqueda desde {start} hacia {goal}...\n")
        
        # Cola de prioridad para explorar nodos (coste acumulado, nodo actual)
        frontier = [(0, start)]
        explored = set()  # Conjunto de nodos ya explorados
        came_from = {}  # Diccionario para rastrear el camino
        
        while frontier:
            # Obtener el nodo con el menor coste acumulado
            current_cost, current_node = heapq.heappop(frontier)
            print(f"Explorando nodo: {current_node} con coste acumulado: {current_cost}")

            if current_node == goal:
                print("¡Objetivo alcanzado!")
                return self.reconstruct_path(came_from, start, goal)

            explored.add(current_node)

            # Explorar los vecinos del nodo actual
            for neighbor, cost in self.nodes.get(current_node, []):
                if neighbor not in explored:
                    new_cost = current_cost + cost
                    print(f" - Evaluando vecino: {neighbor} con coste: {cost} (nuevo coste acumulado: {new_cost})")
                    if all(neighbor != n[1] for n in frontier):  # Evitar nodos ya en la frontera
                        heapq.heappush(frontier, (new_cost, neighbor))
                        came_from[neighbor] = current_node

        print("No se encontró un camino al objetivo.")
        return None

    def reconstruct_path(self, came_from, start, goal):
        """Reconstruye el camino desde el nodo inicial hasta el nodo objetivo."""
        path = []
        current = goal
        while current != start:
            path.append(current)
            current = came_from[current]
        path.append(start)
        path.reverse()
        return path


# Ejemplo de uso
if __name__ == "__main__":
    g = Graph()
    # Definición de un grafo simple
    g.add_edge("A", "B", 1)
    g.add_edge("A", "C", 4)
    g.add_edge("B", "C", 2)
    g.add_edge("B", "D", 5)
    g.add_edge("C", "D", 1)
    g.add_edge("D", "E", 3)
    g.add_edge("C", "E", 6)

    start_node = "A"
    goal_node = "E"
    path = g.online_search(start_node, goal_node)

    if path:
        print(f"\nCamino encontrado: {' -> '.join(path)}")
    else:
        print("No se encontró un camino.")
