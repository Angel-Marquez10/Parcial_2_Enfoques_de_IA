import random

# Título: Implementación de un Modelo Oculto de Markov (HMM)
# Este código simula un Modelo Oculto de Markov y genera una secuencia de observaciones a partir de los estados ocultos.

# Definición de parámetros del modelo
states = ['A', 'B']  # Estados ocultos
observations = ['X', 'Y']  # Observaciones
initial_probabilities = [0.6, 0.4]  # Probabilidades iniciales de cada estado
transition_probabilities = [  # Matriz de transición de estados
    [0.7, 0.3],  # De A a [A, B]
    [0.4, 0.6]   # De B a [A, B]
]
emission_probabilities = [  # Probabilidades de emisión
    [0.9, 0.1],  # De A a [X, Y]
    [0.2, 0.8]   # De B a [X, Y]
]

# Función para elegir un estado basado en probabilidades
def choose_state(probabilities):
    return random.choices(states, weights=probabilities)[0]

# Función para generar una secuencia de observaciones
def generate_sequence(length):
    sequence = []
    current_state = choose_state(initial_probabilities)  # Estado inicial
    for _ in range(length):
        # Elegir la observación basada en el estado actual
        if current_state == 'A':
            observation = choose_state(emission_probabilities[0])
        else:
            observation = choose_state(emission_probabilities[1])
        
        sequence.append((current_state, observation))  # Guardar el estado y la observación
        
        # Transición al siguiente estado
        current_state = choose_state(transition_probabilities[states.index(current_state)])

    return sequence

# Simulación de la generación de una secuencia
length_of_sequence = 10  # Longitud de la secuencia deseada
generated_sequence = generate_sequence(length_of_sequence)

# Imprimir la secuencia generada
print("Secuencia generada (Estado, Observación):")
for state, observation in generated_sequence:
    print(f"Estado: {state}, Observación: {observation}")
