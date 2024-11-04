import heapq  # Importamos la biblioteca heapq para manejar la cola de prioridad

# Definimos un grafo ponderado como un diccionario
# Cada clave es un nodo y su valor es una lista de tuplas (vecino, costo)
graph = {
    'A': [('B', 1), ('C', 3)],
    'B': [('A', 1), ('D', 5), ('E', 2)],
    'C': [('A', 3), ('F', 4)],
    'D': [('B', 5), ('G', 2)],
    'E': [('B', 2), ('G', 3)],
    'F': [('C', 4), ('H', 1)],
    'G': [('D', 2), ('E', 3), ('H', 3)],
    'H': [('F', 1), ('G', 3)]
}

def uniform_cost_search(graph, start, goal):
    """
    Implementa el algoritmo de búsqueda en anchura de costo uniforme.
    Args:
    - graph: diccionario que representa el grafo con costos.
    - start: nodo inicial.
    - goal: nodo objetivo.

    Returns:
    - parent: diccionario que muestra el camino hacia atrás.
    """
    
    # Cola de prioridad que contiene tuplas (costo acumulado, nodo)
    priority_queue = [(0, start)]
    # Conjunto de nodos visitados
    visited = set()
    # Diccionario para rastrear el padre de cada nodo
    parent = {start: None}
    # Diccionario para rastrear el costo acumulado hasta cada nodo
    cost = {start: 0}

    while priority_queue:
        # Extraemos el nodo con el menor costo acumulado
        current_cost, current_node = heapq.heappop(priority_queue)

        # Verificamos si hemos alcanzado el nodo objetivo
        if current_node == goal:
            print(f"Meta alcanzada: {current_node} con costo total: {current_cost}")
            break

        # Ignoramos el nodo si ya ha sido visitado
        if current_node in visited:
            continue

        # Marcamos el nodo actual como visitado
        visited.add(current_node)
        print(f"Visitando: {current_node} con costo acumulado: {current_cost}")

        # Iteramos sobre los vecinos del nodo actual
        for neighbor, edge_cost in graph[current_node]:
            new_cost = current_cost + edge_cost  # Calculamos el nuevo costo acumulado

            # Solo consideramos el vecino si no ha sido visitado o si encontramos un costo menor
            if neighbor not in visited or new_cost < cost.get(neighbor, float('inf')):
                heapq.heappush(priority_queue, (new_cost, neighbor))  # Agregamos el vecino a la cola
                parent[neighbor] = current_node  # Establecemos el padre del vecino
                cost[neighbor] = new_cost  # Actualizamos el costo acumulado

    return parent  # Retornamos el diccionario de padres

def reconstruct_path(parent, start, goal):
    """
    Reconstruye el camino desde el nodo objetivo hasta el nodo de inicio.
    Args:
    - parent: diccionario que muestra el camino hacia atrás.
    - start: nodo inicial.
    - goal: nodo objetivo.

    Returns:
    - path: lista que contiene el camino encontrado.
    """
    path = []  # Lista para almacenar el camino
    current = goal  # Comenzamos desde el nodo objetivo

    # Reconstruimos el camino mientras tengamos un nodo padre
    while current is not None:
        path.append(current)  # Agregamos el nodo actual al camino
        current = parent[current]  # Retrocedemos al nodo padre

    path.reverse()  # Invertimos el camino para que esté desde el inicio al objetivo
    return path  # Retornamos el camino

# Definimos el nodo de inicio y el nodo objetivo
start_node = 'A'  # Nodo inicial 'A'
goal_node = 'H'   # Nodo objetivo 'H'

# Ejecutamos la búsqueda de costo uniforme
print(f"Iniciando la búsqueda de costo uniforme desde el nodo {start_node} hasta el nodo {goal_node}")
parent_map = uniform_cost_search(graph, start_node, goal_node)

# Reconstruimos y mostramos el camino encontrado
if goal_node in parent_map:
    path = reconstruct_path(parent_map, start_node, goal_node)
    print("Camino encontrado:", path)  # Mostramos el camino encontrado
else:
    print("No se encontró un camino hacia el nodo objetivo.")
