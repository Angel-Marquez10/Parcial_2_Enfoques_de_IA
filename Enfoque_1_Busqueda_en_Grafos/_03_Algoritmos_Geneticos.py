import random
import numpy as np

# Configuración del problema
NUM_CITIES = 5  # Número de ciudades en el grafo (puedes ajustar este valor)
POPULATION_SIZE = 20  # Tamaño de la población, es decir, cuántas rutas consideraremos en cada generación
GENERATIONS = 500  # Número de generaciones que el algoritmo ejecutará
MUTATION_RATE = 0.1  # Tasa de mutación, probabilidad de que una mutación ocurra en una ruta

# Generamos un grafo aleatorio en forma de matriz de distancias entre ciudades
# Cada celda de la matriz representa la "distancia" entre dos ciudades
distances = np.random.randint(10, 100, size=(NUM_CITIES, NUM_CITIES))
np.fill_diagonal(distances, 0)  # La distancia de una ciudad a sí misma es 0, así que la matriz es diagonal

# Función para crear un individuo, que representa una ruta aleatoria entre las ciudades
def create_individual():
    individual = list(range(NUM_CITIES))  # Creamos una lista de ciudades [0, 1, 2, ..., NUM_CITIES - 1]
    random.shuffle(individual)  # Mezclamos el orden de las ciudades para crear una ruta aleatoria
    return individual  # Devolvemos el individuo, que es una lista de ciudades en orden aleatorio

# Función para calcular el "fitness" o aptitud de una ruta
# En este caso, la aptitud es la distancia total de la ruta
def calculate_fitness(individual):
    total_distance = 0  # Iniciamos la distancia total en 0
    # Recorremos la ruta ciudad por ciudad, sumando las distancias
    for i in range(len(individual) - 1):
        total_distance += distances[individual[i]][individual[i + 1]]  # Sumar la distancia entre dos ciudades consecutivas
    # Añadimos la distancia para regresar a la ciudad inicial
    total_distance += distances[individual[-1]][individual[0]]
    return total_distance  # Retornamos la distancia total de la ruta

# Función de selección: se utiliza el método de torneo para elegir un individuo
# Este método selecciona un subgrupo de individuos y elige el más apto
def tournament_selection(population, k=3):
    selected = random.sample(population, k)  # Seleccionamos k individuos al azar de la población
    selected.sort(key=calculate_fitness)  # Ordenamos los individuos seleccionados por su aptitud (distancia total)
    return selected[0]  # Devolvemos el individuo con menor distancia (el más apto)

# Función de cruce entre dos padres (crossover) para crear un hijo
def crossover(parent1, parent2):
    child = [-1] * NUM_CITIES  # Iniciamos el hijo como una lista de -1 de longitud NUM_CITIES
    start, end = sorted(random.sample(range(NUM_CITIES), 2))  # Seleccionamos dos puntos al azar para el cruce
    
    # Copiamos una parte del primer padre al hijo
    child[start:end] = parent1[start:end]
    
    # Rellenamos el resto de la ruta con genes del segundo padre sin duplicar ciudades
    p2_index = 0  # Índice para recorrer el segundo padre
    for i in range(NUM_CITIES):
        if child[i] == -1:  # Si el lugar en el hijo está vacío
            # Buscamos en el segundo padre una ciudad que aún no esté en el hijo
            while parent2[p2_index] in child:
                p2_index += 1  # Avanzamos en el segundo padre
            child[i] = parent2[p2_index]  # Asignamos la ciudad al hijo
    return child  # Devolvemos el hijo resultante del cruce

# Función de mutación: realiza un intercambio aleatorio de dos ciudades en la ruta
def mutate(individual):
    if random.random() < MUTATION_RATE:  # Mutamos solo si el número aleatorio es menor que la tasa de mutación
        i, j = random.sample(range(NUM_CITIES), 2)  # Seleccionamos dos posiciones al azar
        # Intercambiamos las ciudades en esas posiciones para modificar ligeramente la ruta
        individual[i], individual[j] = individual[j], individual[i]

# Función principal del algoritmo genético para encontrar la ruta óptima
def genetic_algorithm():
    # Creamos la población inicial generando rutas aleatorias
    population = [create_individual() for _ in range(POPULATION_SIZE)]
    
    for generation in range(GENERATIONS):  # Iteramos a través de las generaciones
        # Evaluamos la aptitud de cada individuo en la población
        population.sort(key=calculate_fitness)  # Ordenamos la población por aptitud (distancia total)
        best_individual = population[0]  # Obtenemos el mejor individuo de la generación actual
        best_fitness = calculate_fitness(best_individual)  # Calculamos su aptitud

        # Imprimimos el mejor individuo y su distancia en la generación actual
        print(f"Generación {generation}: Mejor ruta: {best_individual}, Distancia: {best_fitness}")
        
        # Condición de parada si encontramos una ruta óptima (distancia 0)
        if best_fitness == 0:
            print("Ruta óptima encontrada!")
            break
        
        # Crear una nueva generación mediante selección, cruce y mutación
        new_population = []
        for _ in range(POPULATION_SIZE):
            # Seleccionamos dos padres usando selección por torneo
            parent1 = tournament_selection(population)
            parent2 = tournament_selection(population)
            # Realizamos el cruce entre los padres para generar un hijo
            child = crossover(parent1, parent2)
            # Mutamos el hijo
            mutate(child)
            # Añadimos el hijo a la nueva generación
            new_population.append(child)
        
        # Actualizamos la población con la nueva generación
        population = new_population
    
    # Resultados finales: mostramos el mejor individuo al final del algoritmo
    best_individual = min(population, key=calculate_fitness)  # Obtenemos el mejor individuo de la última generación
    print("Mejor ruta encontrada:", best_individual)
    print("Distancia mínima:", calculate_fitness(best_individual))

# Ejecutamos el algoritmo genético
genetic_algorithm()
