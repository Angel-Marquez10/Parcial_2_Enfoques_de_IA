from collections import defaultdict

def print_map_coloring(colors, regions):
    """Imprime el coloreo del mapa."""
    print("\nColoreo del mapa:")
    for region in regions:
        print(f"{region}: {colors.get(region, 'Sin color')}")
    print("\n")

def is_consistent(colors, region, color, adjacency):
    """Verifica si la asignación de color es consistente con las restricciones."""
    for neighbor in adjacency[region]:
        if neighbor in colors and colors[neighbor] == color:
            return False
    return True

def propagate_constraints(colors, adjacency, domain, region, color):
    """Propaga restricciones eliminando colores inconsistentes del dominio."""
    for neighbor in adjacency[region]:
        if neighbor not in colors:  # Solo afecta a regiones no coloreadas
            if color in domain[neighbor]:
                domain[neighbor].remove(color)
                print(f"Eliminando color {color} de {neighbor} debido a la restricción.")
            if len(domain[neighbor]) == 0:  # Si el dominio queda vacío
                return False
    return True

def backtrack(colors, adjacency, domain):
    """Realiza la búsqueda con propagación de restricciones."""
    if len(colors) == len(domain):
        print("Solución encontrada:")
        print_map_coloring(colors, domain.keys())
        return True

    # Selecciona una región no coloreada
    region = next(r for r in domain if r not in colors)
    for color in domain[region]:
        print(f"Intentando color {color} para {region}.")
        
        # Verifica si es consistente
        if is_consistent(colors, region, color, adjacency):
            colors[region] = color  # Asigna el color
            print(f"Coloreando {region} con {color}.")

            # Realiza la propagación de restricciones
            temp_domain = {r: domain[r][:] for r in domain}  # Copia del dominio original
            if propagate_constraints(colors, adjacency, temp_domain, region, color):
                if backtrack(colors, adjacency, temp_domain):
                    return True

            # Retrocede si no hay solución
            del colors[region]
            print(f"Retrocediendo de {region}.")
    
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

    colors = {}  # Almacena el coloreo actual

    if not backtrack(colors, adjacency, domain):
        print("No se encontró solución.")

# Ejemplo de uso
if __name__ == "__main__":
    map_coloring_problem()
