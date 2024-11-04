class CityGraph:
    def __init__(self):
        """Inicializa un grafo de ciudades vacío."""
        self.graph = {}  # Diccionario para almacenar el grafo

    def add_road(self, city1, city2):
        """Agrega una carretera entre las ciudades city1 y city2."""
        if city1 not in self.graph:
            self.graph[city1] = []
        if city2 not in self.graph:
            self.graph[city2] = []
        self.graph[city1].append(city2)  # Añadir city2 a la lista de vecinos de city1
        self.graph[city2].append(city1)  # Añadir city1 a la lista de vecinos de city2 (grafo no dirigido)

    def bidirectional_search(self, start, goal):
        """
        Realiza la búsqueda bidireccional para encontrar un camino
        desde la ciudad de inicio hasta la ciudad objetivo.
        
        Args:
        - start: Ciudad de inicio.
        - goal: Ciudad objetivo.

        Returns:
        - Una lista de ciudades que representan el camino o None si no se encontró.
        """
        if start == goal:
            return [start]  # Si la ciudad de inicio es la misma que la ciudad objetivo

        # Conjuntos para mantener las ciudades visitadas desde el inicio y desde el objetivo
        visited_start = {start}
        visited_goal = {goal}

        # Diccionarios para rastrear los caminos desde el inicio y el objetivo
        parent_start = {start: None}
        parent_goal = {goal: None}

        # Realiza la búsqueda en ambas direcciones
        while visited_start and visited_goal:
            # Expande desde la ciudad de inicio
            found_path = self.expand(visited_start, parent_start, "start")
            if found_path:  # Si se encontró un camino
                return self.construct_path(found_path, parent_start, parent_goal)

            # Expande desde la ciudad objetivo
            found_path = self.expand(visited_goal, parent_goal, "goal")
            if found_path:  # Si se encontró un camino
                return self.construct_path(found_path, parent_start, parent_goal)

        return None  # No se encontró un camino

    def expand(self, visited, parent, direction):
        """
        Expande una ciudad desde el conjunto de ciudades visitadas.

        Args:
        - visited: Conjunto de ciudades visitadas en la dirección actual.
        - parent: Diccionario de ciudades padre para rastrear caminos.
        - direction: Dirección de la búsqueda ("start" o "goal").

        Returns:
        - La ciudad que se encontró en el conjunto de ciudades opuestas o None.
        """
        current = visited.pop()  # Toma una ciudad de los visitados
        for neighbor in self.graph.get(current, []):  # Obtener vecinos
            if neighbor not in parent:  # Si el vecino no ha sido visitado en la otra dirección
                visited.add(neighbor)  # Agregar a los visitados
                parent[neighbor] = current  # Marcar el vecino como padre de la ciudad actual
            else:
                return neighbor  # Se encontró una ciudad en el conjunto opuesto
        return None

    def construct_path(self, meet_city, parent_start, parent_goal):
        """
        Construye el camino desde la ciudad de inicio hasta la ciudad objetivo.
        
        Args:
        - meet_city: La ciudad donde se encontraron ambas búsquedas.
        - parent_start: Diccionario de ciudades padre desde el inicio.
        - parent_goal: Diccionario de ciudades padre desde el objetivo.

        Returns:
        - Una lista de ciudades que representan el camino.
        """
        # Construir camino desde el inicio hasta la ciudad de encuentro
        path_start = []
        while meet_city is not None:
            path_start.append(meet_city)
            meet_city = parent_start[meet_city]
        path_start.reverse()  # Invertir el camino para tener el orden correcto

        # Construir camino desde la ciudad de encuentro hasta el objetivo
        meet_city = next(key for key in parent_goal if parent_goal[key] is None)
        path_goal = []
        while meet_city is not None:
            path_goal.append(meet_city)
            meet_city = parent_goal[meet_city]

        return path_start + path_goal[1:]  # Evitar duplicar la ciudad de encuentro

# Crear un grafo de ciudades y agregar carreteras
city_graph = CityGraph()
city_graph.add_road('Ciudad A', 'Ciudad B')
city_graph.add_road('Ciudad A', 'Ciudad C')
city_graph.add_road('Ciudad B', 'Ciudad D')
city_graph.add_road('Ciudad C', 'Ciudad E')
city_graph.add_road('Ciudad D', 'Ciudad E')
city_graph.add_road('Ciudad E', 'Ciudad F')
city_graph.add_road('Ciudad B', 'Ciudad F')

# Definir ciudad de inicio y ciudad objetivo
start_city = 'Ciudad A'
goal_city = 'Ciudad F'

# Ejecutar la búsqueda bidireccional
result_path = city_graph.bidirectional_search(start_city, goal_city)

# Mostrar el resultado final
if result_path:
    print(f"Se encontró un camino desde {start_city} hasta {goal_city}: {' -> '.join(result_path)}")
else:
    print(f"No se encontró un camino desde {start_city} hasta {goal_city}.")
