import random
import math

class SimulatedAnnealingNQueens:
    def __init__(self, n, initial_temp=1000, cooling_rate=0.95):
        """Inicializa la búsqueda de temple simulado para el problema de N-Reinas."""
        self.n = n  # Número de reinas y tamaño del tablero
        self.current_solution = self.generate_initial_solution()
        self.current_score = self.calculate_attacks(self.current_solution)
        self.best_solution = self.current_solution
        self.best_score = self.current_score
        self.temperature = initial_temp  # Temperatura inicial
        self.cooling_rate = cooling_rate  # Tasa de enfriamiento
        print(f"Solución inicial: {self.current_solution} con ataques: {self.current_score}")

    def generate_initial_solution(self):
        """Genera una solución inicial aleatoria."""
        return [random.randint(0, self.n - 1) for _ in range(self.n)]

    def calculate_attacks(self, solution):
        """Calcula el número de ataques en la solución actual."""
        attacks = 0
        for i in range(self.n):
            for j in range(i + 1, self.n):
                if solution[i] == solution[j] or abs(solution[i] - solution[j]) == abs(i - j):
                    attacks += 1
        return attacks

    def get_neighbor(self, solution):
        """Genera un vecino cambiando la posición de una reina."""
        neighbor = solution[:]
        col = random.randint(0, self.n - 1)
        # Mueve la reina a una nueva columna aleatoria
        neighbor[col] = random.randint(0, self.n - 1)
        return neighbor

    def acceptance_probability(self, current_score, neighbor_score, temperature):
        """Calcula la probabilidad de aceptar una solución peor."""
        if neighbor_score < current_score:
            return 1.0  # Siempre aceptamos una mejor solución
        else:
            # Calcula la probabilidad de aceptar una solución peor
            return math.exp((current_score - neighbor_score) / temperature)

    def search(self, max_iterations=1000):
        """Ejecuta el algoritmo de búsqueda de temple simulado para el problema de N-Reinas."""
        iteration = 0

        while iteration < max_iterations and self.current_score > 0:
            neighbor = self.get_neighbor(self.current_solution)
            neighbor_score = self.calculate_attacks(neighbor)

            # Decide si se acepta la nueva solución
            if self.acceptance_probability(self.current_score, neighbor_score, self.temperature) > random.random():
                self.current_solution = neighbor
                self.current_score = neighbor_score
                print(f"Iteración {iteration}: Se acepta vecino: {self.current_solution} con ataques: {self.current_score}")
                
                # Actualiza la mejor solución
                if self.current_score < self.best_score:
                    self.best_solution = self.current_solution
                    self.best_score = self.current_score
                    print(f"Mejor solución actualizada: {self.best_solution} con ataques: {self.best_score}")
            else:
                print(f"Iteración {iteration}: Se rechaza vecino: {neighbor} con ataques: {neighbor_score}")

            # Reduce la temperatura
            self.temperature *= self.cooling_rate
            iteration += 1

        return self.best_solution, self.best_score  # Retorna la mejor solución y su puntuación

# Ejemplo de uso
if __name__ == "__main__":
    n = 8  # Número de reinas
    simulated_annealing = SimulatedAnnealingNQueens(n)

    # Ejecutar la búsqueda de temple simulado
    optimal_solution, optimal_attacks = simulated_annealing.search(max_iterations=1000)
    print(f"Solución óptima alcanzada: {optimal_solution} con ataques: {optimal_attacks}")
