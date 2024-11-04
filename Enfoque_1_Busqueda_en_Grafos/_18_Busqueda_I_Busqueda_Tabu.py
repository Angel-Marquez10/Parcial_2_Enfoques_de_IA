import random
import numpy as np

class TabuSearchNQueens:
    def __init__(self, n, tabu_tenure=5):
        """Inicializa la búsqueda tabú para el problema de N-Reinas."""
        self.n = n  # Número de reinas y tamaño del tablero
        self.tabu_tenure = tabu_tenure  # Duración de la lista tabú
        self.tabu_list = []  # Lista para almacenar soluciones tabú
        self.best_solution = None  # Mejor solución encontrada
        self.best_score = float('inf')  # Mejor puntuación (menos ataques)

    def calculate_attacks(self, solution):
        """Calcula el número de ataques en la solución actual."""
        attacks = 0
        for i in range(self.n):
            for j in range(i + 1, self.n):
                # Verifica si hay un ataque en las mismas filas o diagonales
                if solution[i] == solution[j] or abs(solution[i] - solution[j]) == abs(i - j):
                    attacks += 1
        return attacks

    def get_neighbors(self, solution):
        """Genera vecinos cambiando la posición de una reina."""
        neighbors = []
        for i in range(self.n):
            for j in range(self.n):
                if solution[i] != j:  # Solo cambia si no es la misma columna
                    new_solution = solution[:]
                    new_solution[i] = j  # Mueve la reina a la nueva columna
                    neighbors.append(new_solution)
        return neighbors

    def search(self, max_iterations=1000):
        """Ejecuta el algoritmo de búsqueda tabú para el problema de N-Reinas."""
        # Generar solución inicial aleatoria
        current_solution = [random.randint(0, self.n - 1) for _ in range(self.n)]
        current_score = self.calculate_attacks(current_solution)
        print(f"Solución inicial: {current_solution} con ataques: {current_score}")

        iteration = 0

        # Bucle de búsqueda
        while iteration < max_iterations:
            neighbors = self.get_neighbors(current_solution)
            print(f"Vecinos generados: {neighbors}")

            # Filtrar vecinos no tabú
            non_tabu_neighbors = [n for n in neighbors if n not in self.tabu_list]
            if not non_tabu_neighbors:
                print("No quedan vecinos válidos. Terminando la búsqueda.")
                break

            # Encuentra el mejor vecino no tabú
            next_solution = min(non_tabu_neighbors, key=self.calculate_attacks)
            next_score = self.calculate_attacks(next_solution)
            print(f"Mejor vecino no tabú: {next_solution} con ataques: {next_score}")

            # Actualizar mejor solución
            if next_score < self.best_score:
                self.best_solution = next_solution
                self.best_score = next_score
                print(f"Nueva mejor solución encontrada: {self.best_solution} con ataques: {self.best_score}")

            # Actualizar la lista tabú
            self.tabu_list.append(current_solution)
            if len(self.tabu_list) > self.tabu_tenure:
                removed = self.tabu_list.pop(0)  # Remueve el elemento más antiguo
                print(f"Elemento tabú removido: {removed}")

            current_solution = next_solution  # Mueve al mejor vecino encontrado
            iteration += 1

        return self.best_solution, self.best_score  # Retorna la mejor solución y su puntuación

# Ejemplo de uso
if __name__ == "__main__":
    n = 8  # Número de reinas
    tabu_search = TabuSearchNQueens(n)

    # Ejecutar la búsqueda tabú
    optimal_solution, optimal_attacks = tabu_search.search(max_iterations=1000)
    print(f"Solución óptima alcanzada: {optimal_solution} con ataques: {optimal_attacks}")
