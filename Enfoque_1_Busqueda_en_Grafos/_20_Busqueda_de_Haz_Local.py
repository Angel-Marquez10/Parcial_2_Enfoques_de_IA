import random

class NQueens:
    def __init__(self, n, k):
        """Inicializa el problema de N-Reinas."""
        self.n = n  # Número de reinas
        self.k = k  # Tamaño del haz (número de soluciones que se mantendrán)
        self.solutions = [self.generate_initial_solution() for _ in range(k)]
        print("Soluciones iniciales generadas:")
        self.print_solutions(self.solutions)

    def generate_initial_solution(self):
        """Genera una solución inicial aleatoria."""
        return [random.randint(0, self.n - 1) for _ in range(self.n)]

    def calculate_attacks(self, solution):
        """Calcula el número de ataques en la solución actual."""
        attacks = 0
        for i in range(self.n):
            for j in range(i + 1, self.n):
                # Verifica si dos reinas están en la misma columna o en la misma diagonal
                if solution[i] == solution[j] or abs(solution[i] - solution[j]) == abs(i - j):
                    attacks += 1
        return attacks

    def get_neighbors(self, solution):
        """Genera vecinos cambiando la posición de cada reina en la solución."""
        neighbors = []
        for col in range(self.n):
            for row in range(self.n):
                if row != solution[col]:  # Cambiar solo si la reina se mueve
                    neighbor = solution[:]
                    neighbor[col] = row
                    neighbors.append(neighbor)
        return neighbors

    def search(self, max_iterations=100):
        """Ejecuta la búsqueda de haz local para el problema de N-Reinas."""
        for iteration in range(max_iterations):
            print(f"\n--- Iteración {iteration + 1} ---")
            scored_solutions = [(solution, self.calculate_attacks(solution)) for solution in self.solutions]
            scored_solutions.sort(key=lambda x: x[1])  # Ordena por ataques
            best_solutions = [solution for solution, _ in scored_solutions[:self.k]]  # Selecciona las mejores k

            print(f"Mejores soluciones en esta iteración:")
            self.print_solutions(best_solutions)

            # Generar nuevos vecinos para las mejores soluciones
            new_solutions = []
            for solution in best_solutions:
                neighbors = self.get_neighbors(solution)
                new_solutions.extend(neighbors)

            # Filtrar soluciones nuevas y evitar duplicados
            new_solutions = list(set(tuple(sol) for sol in new_solutions))
            self.solutions = best_solutions + new_solutions  # Combina las mejores soluciones con los nuevos vecinos

            # Si alguna solución tiene 0 ataques, hemos encontrado la solución
            if any(self.calculate_attacks(solution) == 0 for solution in self.solutions):
                print("¡Se encontró una solución sin ataques!")
                break

            # Mantener solo las k mejores soluciones
            scored_solutions = [(solution, self.calculate_attacks(solution)) for solution in self.solutions]
            scored_solutions.sort(key=lambda x: x[1])  # Ordena por ataques
            self.solutions = [solution for solution, _ in scored_solutions[:self.k]]  # Selecciona las mejores k

        # Retorna la mejor solución encontrada
        best_solution = min(self.solutions, key=self.calculate_attacks)
        return best_solution, self.calculate_attacks(best_solution)

    def print_solutions(self, solutions):
        """Imprime las soluciones de forma legible."""
        for sol in solutions:
            print(sol)

# Ejemplo de uso
if __name__ == "__main__":
    n = 8  # Número de reinas
    k = 5  # Tamaño del haz
    n_queens = NQueens(n, k)

    # Ejecutar la búsqueda de haz local
    optimal_solution, optimal_attacks = n_queens.search(max_iterations=100)
    print(f"\n--- Solución óptima alcanzada: {optimal_solution} con ataques: {optimal_attacks} ---")
