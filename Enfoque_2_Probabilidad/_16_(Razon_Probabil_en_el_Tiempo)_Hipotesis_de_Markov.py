# Título: Simulación de un Proceso de Markov Simple
# Este código simula un proceso de Markov con tres estados.

# Definición de estados
states = ['A', 'B', 'C']  # Tres estados del sistema

# Matriz de transición de estados
# Cada fila representa un estado actual y cada columna representa la probabilidad de transición a otro estado
transition_matrix = [
    [0.1, 0.6, 0.3],  # Probabilidades de transición desde el estado A
    [0.4, 0.1, 0.5],  # Probabilidades de transición desde el estado B
    [0.2, 0.7, 0.1],  # Probabilidades de transición desde el estado C
]

# Función para seleccionar el siguiente estado basado en la matriz de transición
def next_state(current_state):
    # Generar un número aleatorio para determinar el siguiente estado
    import random
    rand = random.random()  # Número aleatorio entre 0 y 1
    cumulative_probability = 0.0
    
    # Determinar el siguiente estado basado en la probabilidad acumulativa
    for i, prob in enumerate(transition_matrix[current_state]):
        cumulative_probability += prob
        if rand < cumulative_probability:
            return i  # Retorna el índice del nuevo estado

# Simulación del proceso de Markov
num_steps = 10  # Número de pasos a simular
current_state = 0  # Estado inicial (A)

print("Simulación del Proceso de Markov:")
print(f"Estado inicial: {states[current_state]}")

for step in range(num_steps):
    current_state = next_state(current_state)  # Obtener el siguiente estado
    print(f"Paso {step + 1}: Estado actual: {states[current_state]}")

