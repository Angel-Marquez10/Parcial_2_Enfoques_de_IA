import random

def print_map_coloring(colors, regions):
    """Imprime el coloreo del mapa."""
    print("\nColoreo del mapa:")
    for region in regions:
        print(f"{region}: {colors.get(region, 'Sin color')}")
    print("\n")

def count_conflicts(colors, region, adjacency):
    """Cuenta los conflictos de color para una región específica."""
    conflicts = 0
    for neighbor in adjacency[region]:
        if neighbor in colors and colors[neighbor] == colors[region]:
            conflicts += 1
    return conflicts

def get_random_coloring(domain, regions):
    """Genera una coloración aleatoria del mapa."""
    return {region: random.choice(domain[region]) for region in regions}

def min_conflicts(colors, adjacency, domain, max_steps):
    """Implementa el algoritmo de Mínimos Conflictos."""
    for step in range(max_steps):
        # Verifica si hay conflictos
        conflicts = {region: count_conflicts(colors, region, adjacency) for region in adjacency}
        
        # Si no hay conflictos, se ha encontrado una solución
        if all(count == 0 for count in conflicts.values()):
            print("Solución encontrada:")
            print_map_coloring(colors, adjacency.keys())
            return True
        
        # Selecciona una región con el máximo conflicto
        max_conflict_region = max(conflicts, key=conflicts.get)
        print(f"\nRegión con conflicto: {max_conflict_region} (Conflictos: {conflicts[max_conflict_region]})")
        
        # Obtiene los colores disponibles
        available_colors = domain[max_conflict_region]
        
        # Encuentra el color que minimiza los conflictos
        best_color = None
        min_conflict_count = float('inf')
        
        for color in available_colors:
            colors[max_conflict_region] = color
            conflict_count = count_conflicts(colors, max_conflict_region, adjacency)
            if conflict_count < min_conflict_count:
                min_conflict_count = conflict_count
                best_color = color
        
        # Asigna el mejor color encontrado
        colors[max_conflict_region] = best_color
        print(f"Coloreando {max_conflict_region} con {best_color}.")
    
    print("No se encontró solución dentro del número máximo de pasos.")
    return False

def map_coloring_problem():
    """Inicializa el problema de coloreo del mapa."""
    # Define las regiones y sus adyacencias
    adjacency = {
        'A': ['B', 'C'],
        'B': ['A', 'C', 'D'],
        'C': ['A', 'B', 'D', 'E'],
        'D': ['B', 'C', 'E'],
        'E': ['C', 'D'],
    }

    # Define el dominio de colores para cada región
    domain = {
        'A': ['Rojo', 'Verde', 'Azul'],
        'B': ['Rojo', 'Verde', 'Azul'],
        'C': ['Rojo', 'Verde', 'Azul'],
        'D': ['Rojo', 'Verde', 'Azul'],
        'E': ['Rojo', 'Verde', 'Azul'],
    }

    # Genera una coloración aleatoria inicial
    regions = adjacency.keys()
    colors = get_random_coloring(domain, regions)
    print("Coloración inicial aleatoria:")
    print_map_coloring(colors, regions)

    max_steps = 100  # Número máximo de pasos para el algoritmo
    min_conflicts(colors, adjacency, domain, max_steps)

# Ejemplo de uso
if __name__ == "__main__":
    map_coloring_problem()
