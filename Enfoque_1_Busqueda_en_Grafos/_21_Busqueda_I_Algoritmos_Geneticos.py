import random

class GeneticAlgorithm:
    def __init__(self, population_size, generations, mutation_rate, target_sum):
        """Inicializa el algoritmo genético."""
        self.population_size = population_size
        self.generations = generations
        self.mutation_rate = mutation_rate
        self.target_sum = target_sum
        self.population = self.create_initial_population()
        print(f"Generación inicial: {self.population}")

    def create_initial_population(self):
        """Crea una población inicial aleatoria."""
        return [[random.randint(-10, 10) for _ in range(5)] for _ in range(self.population_size)]

    def fitness(self, individual):
        """Calcula la 'aptitud' de un individuo en relación a la suma objetivo."""
        return abs(sum(individual) - self.target_sum)

    def select_parents(self):
        """Selecciona dos padres de la población basada en la aptitud."""
        sorted_population = sorted(self.population, key=self.fitness)
        return sorted_population[0], sorted_population[1]  # Los dos mejores

    def crossover(self, parent1, parent2):
        """Realiza el cruce entre dos padres para crear un nuevo hijo."""
        crossover_point = random.randint(1, len(parent1) - 1)
        child = parent1[:crossover_point] + parent2[crossover_point:]
        return child

    def mutate(self, individual):
        """Aplica mutación a un individuo con una probabilidad definida."""
        for i in range(len(individual)):
            if random.random() < self.mutation_rate:
                individual[i] += random.choice([-1, 1])  # Aumenta o disminuye en 1
        return individual

    def run(self):
        """Ejecuta el algoritmo genético para encontrar una solución."""
        for generation in range(self.generations):
            print(f"\n--- Generación {generation + 1} ---")
            new_population = []

            # Generar nueva población
            for _ in range(self.population_size // 2):  # Se generan pares de padres
                parent1, parent2 = self.select_parents()
                child1 = self.crossover(parent1, parent2)
                child2 = self.crossover(parent2, parent1)
                new_population.extend([self.mutate(child1), self.mutate(child2)])

            self.population = new_population
            print(f"Población nueva: {self.population}")

            # Verificar si hemos encontrado la solución
            best_individual = min(self.population, key=self.fitness)
            if self.fitness(best_individual) == 0:
                print(f"¡Solución encontrada! {best_individual} con suma: {sum(best_individual)}")
                break
        else:
            print(f"No se encontró solución exacta en {self.generations} generaciones.")
            print(f"Mejor individuo: {best_individual} con suma: {sum(best_individual)} y aptitud: {self.fitness(best_individual)}")


# Ejemplo de uso
if __name__ == "__main__":
    target_sum = 0  # La suma objetivo
    population_size = 10  # Tamaño de la población
    generations = 20  # Número de generaciones
    mutation_rate = 0.1  # Tasa de mutación

    ga = GeneticAlgorithm(population_size, generations, mutation_rate, target_sum)
    ga.run()
