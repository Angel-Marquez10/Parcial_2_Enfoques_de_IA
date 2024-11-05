import numpy as np
import matplotlib.pyplot as plt

# Título: Monte Carlo para Cadenas de Markov
# Este código simula una cadena de Markov y estima la distribución de estados usando el método de Monte Carlo.

# Introducción
print("Bienvenido a la práctica de Monte Carlo para Cadenas de Markov")
print("Este ejercicio simula una cadena de Markov y estima la distribución de estados.\n")

# Definición de la matriz de transición
# Las filas representan el estado actual y las columnas representan el estado siguiente.
transition_matrix = np.array([[0.1, 0.6, 0.3],  # Probabilidades de transición desde A
                              [0.4, 0.5, 0.1],  # Probabilidades de transición desde B
                              [0.3, 0.3, 0.4]]) # Probabilidades de transición desde C

# Definición de los estados
states = ['A', 'B', 'C']

# Parámetros de simulación
num_steps = 10000  # Número de pasos de la simulación
initial_state = 0  # Comenzamos en el estado A (índice 0)

# Inicialización de conteo de estados
state_count = np.zeros(len(states))

# Simulación de la cadena de Markov
current_state = initial_state
for _ in range(num_steps):
    state_count[current_state] += 1  # Contar el estado actual
    current_state = np.random.choice(range(len(states)), p=transition_matrix[current_state])

# Cálculo de la distribución de estados
state_distribution = state_count / num_steps

# Resultados
print("Distribución estimada de estados después de la simulación:")
for state, distribution in zip(states, state_distribution):
    print(f"Estado {state}: {distribution:.4f}")

# Visualización
plt.bar(states, state_distribution, color=['blue', 'orange', 'green'])
plt.title('Distribución de Estados en la Cadena de Markov')
plt.ylabel('Probabilidad')
plt.ylim(0, 1)
plt.grid(axis='y')
plt.show()

# Conclusión
print("\nConclusión:")
print("Hemos simulado una cadena de Markov utilizando el método de Monte Carlo.")
print("La distribución de estados estimada muestra la probabilidad de encontrar el sistema en cada estado después de múltiples transiciones.")
