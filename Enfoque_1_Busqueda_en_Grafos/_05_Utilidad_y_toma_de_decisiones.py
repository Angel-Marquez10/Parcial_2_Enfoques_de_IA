from itertools import permutations

# Matriz de costos de viaje entre ubicaciones
travel_costs = [
    [0, 15, 20, 10],  # Costos de viaje desde la ubicación 0
    [15, 0, 30, 25],  # Costos de viaje desde la ubicación 1
    [20, 30, 0, 35],  # Costos de viaje desde la ubicación 2
    [10, 25, 35, 0]   # Costos de viaje desde la ubicación 3
]

# Ganancias estimadas en cada ubicación (supuesto de ventas)
potential_profits = [40, 50, 60, 70]  # Ganancias al visitar cada ubicación

# Número de ubicaciones
num_locations = len(travel_costs)

# Función para calcular la utilidad neta de una ruta dada
def calculate_net_utility(route):
    total_cost = 0
    total_profit = 0
    
    # Sumamos las ganancias en cada ubicación
    for location in route:
        total_profit += potential_profits[location]
    
    # Calculamos el costo del viaje a lo largo de la ruta
    for i in range(len(route) - 1):
        total_cost += travel_costs[route[i]][route[i + 1]]
    
    # Consideramos el costo de regresar a la ubicación de origen
    total_cost += travel_costs[route[-1]][route[0]]
    
    # Calculamos la utilidad neta (ganancia - costo total)
    net_utility = total_profit - total_cost
    return net_utility

# Función principal para encontrar la ruta óptima
def find_optimal_route():
    best_route = None
    max_utility = float('-inf')
    
    # Probamos todas las permutaciones de rutas posibles
    for route in permutations(range(num_locations)):
        net_utility = calculate_net_utility(route)
        
        # Verificamos si la utilidad de la ruta actual es la mejor hasta ahora
        if net_utility > max_utility:
            max_utility = net_utility
            best_route = route
            
    return best_route, max_utility

# Ejecutamos la función para encontrar la mejor ruta y utilidad máxima
optimal_route, max_utility = find_optimal_route()

# Imprimimos la ruta óptima y la utilidad máxima
print("Ruta óptima:", optimal_route)
print("Utilidad máxima:", max_utility)
