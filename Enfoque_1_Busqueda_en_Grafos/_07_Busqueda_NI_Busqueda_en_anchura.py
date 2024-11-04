from collections import deque  # Importamos deque para implementar una cola de forma eficiente

# Definimos el grafo como un diccionario
# Cada clave es un nodo y su valor es una lista de nodos vecinos
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

# Función para realizar la búsqueda en anchura (BFS) desde un nodo de inicio hasta un nodo objetivo
def bfs(graph, start, goal):
    queue = deque([start])  # Inicializamos la cola con el nodo de inicio
    visited = set()  # Conjunto para rastrear los nodos visitados
    visited.add(start)  # Marcamos el nodo de inicio como visitado
    parent = {start: None}  # Diccionario para rastrear el camino hacia atrás

    while queue:
        current = queue.popleft()  # Sacamos el nodo actual de la cola
        print(f"Visitando: {current}")  # Mostramos el nodo actual

        # Verificamos si hemos alcanzado el nodo objetivo
        if current == goal:
            print("Meta alcanzada:", current)
            break  # Salimos del bucle si se alcanzó la meta

        # Iteramos sobre los vecinos del nodo actual
        for neighbor in graph[current]:
            # Verificamos si el vecino no ha sido visitado
            if neighbor not in visited:
                queue.append(neighbor)  # Añadimos el vecino a la cola
                visited.add(neighbor)  # Marcamos el vecino como visitado
                parent[neighbor] = current  # Registramos el padre del vecino

    return parent  # Retornamos el diccionario de padres

# Función para reconstruir el camino desde el nodo objetivo hasta el nodo de inicio
def reconstruct_path(parent, start, goal):
    path = []  # Lista para almacenar el camino
    current = goal  # Comenzamos desde el nodo objetivo

    while current is not None:  # Mientras tengamos un padre
        path.append(current)  # Añadimos la posición actual al camino
        current = parent[current]  # Retrocedemos al padre

    path.reverse()  # Invertimos el camino para que esté desde el inicio al objetivo
    return path  # Retornamos el camino

# Definimos el nodo de inicio y el nodo objetivo
start_node = 'A'  # Nodo inicial 'A'
goal_node = 'F'   # Nodo objetivo 'F'

# Ejecutamos la búsqueda en anchura
print(f"Iniciando la búsqueda en anchura desde el nodo {start_node} hasta el nodo {goal_node}")
parent_map = bfs(graph, start_node, goal_node)

# Reconstruimos el camino
if goal_node in parent_map:
    path = reconstruct_path(parent_map, start_node, goal_node)
    print("Camino encontrado:", path)  # Mostramos el camino encontrado
else:
    print("No se encontró un camino hacia el nodo objetivo.")
