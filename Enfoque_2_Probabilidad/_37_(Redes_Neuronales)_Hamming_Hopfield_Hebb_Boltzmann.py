
import numpy as np

# Definición de una red de Hopfield
class HopfieldNetwork:
    def __init__(self, n):
        self.n = n
        self.W = np.zeros((n, n))

    def train(self, patterns):
        for pattern in patterns:
            self.W += np.outer(pattern, pattern)
        np.fill_diagonal(self.W, 0)  # No auto-conexiones

    def run(self, initial_state, steps=5):
        state = initial_state.copy()
        for _ in range(steps):
            for i in range(self.n):
                s = np.dot(self.W[i], state)
                state[i] = 1 if s > 0 else -1
        return state

# Definición de patrones de entrenamiento
patterns = np.array([[1, 1, -1, -1],
                     [-1, -1, 1, 1],
                     [1, -1, 1, -1]])

# Entrenamiento y ejecución de la red de Hopfield
hopfield = HopfieldNetwork(n=4)
hopfield.train(patterns)
initial_state = np.array([1, -1, -1, -1])
result = hopfield.run(initial_state)

print("Estado inicial:", initial_state)
print("Estado final después de la red de Hopfield:", result)
