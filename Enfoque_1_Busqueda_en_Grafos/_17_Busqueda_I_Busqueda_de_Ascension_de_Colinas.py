import random

def hill_climbing(start, objective_func, get_neighbors):
    """Implementa el algoritmo de búsqueda de ascenso de colinas."""
    current = start  # Comienza en el punto inicial
    print(f"Iniciando la búsqueda de ascenso de colinas desde {current}.")

    while True:
        # Obtiene los vecinos del nodo actual
        neighbors = get_neighbors(current)
        if not neighbors:
            print("No se encontraron vecinos. Terminado.")
            return current

        # Encuentra el mejor vecino
        next_node = max(neighbors, key=objective_func)
        print(f"Vecinos: {neighbors}, Mejor vecino: {next_node}, Valor: {objective_func(next_node)}")

        # Si el mejor vecino es mejor que el nodo actual, ascender
        if objective_func(next_node) > objective_func(current):
            print(f"Ascendiendo de {current} a {next_node}.")
            current = next_node
        else:
            print("No se puede mejorar, se ha alcanzado un óptimo local.")
            break

    return current  # Retorna el nodo actual que es el óptimo local

def objective_function(x):
    """Función objetivo para maximizar (ejemplo de función cuadrática)."""
    return -(x - 3) ** 2 + 10  # Un máximo en x=3

def get_neighbors(x):
    """Genera vecinos en un rango de -1 a 1 del nodo actual."""
    return [x + random.uniform(-1, 1) for _ in range(5)]

# Ejecución de la búsqueda de ascenso de colinas
start_point = random.uniform(-10, 10)  # Punto de inicio aleatorio
print(f"Punto de inicio: {start_point}")

optimal_point = hill_climbing(start_point, objective_function, get_neighbors)
print(f"Óptimo local alcanzado en: {optimal_point} con valor: {objective_function(optimal_point)}")
