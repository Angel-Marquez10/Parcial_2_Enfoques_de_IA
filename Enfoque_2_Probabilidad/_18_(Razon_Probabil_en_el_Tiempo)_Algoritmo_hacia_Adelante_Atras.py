# Título: Algoritmo Hacia Delante-Atrás
# Este código implementa el algoritmo hacia adelante-hacia atrás para un modelo oculto de Markov.

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

# Secuencia de observaciones
sequence = ['X', 'Y', 'X']

# Fase Hacia Adelante
def forward_algorithm(sequence):
    alpha = []  # Almacenará las probabilidades hacia adelante
    # Inicialización
    first_obs_index = observations.index(sequence[0])
    alpha_0 = [initial_probabilities[i] * emission_probabilities[i][first_obs_index] for i in range(len(states))]
    alpha.append(alpha_0)

    # Recursión
    for t in range(1, len(sequence)):
        alpha_t = []
        obs_index = observations.index(sequence[t])
        for j in range(len(states)):
            prob = sum(alpha[t-1][i] * transition_probabilities[i][j] for i in range(len(states)))
            alpha_t.append(prob * emission_probabilities[j][obs_index])
        alpha.append(alpha_t)

    return alpha

# Fase Hacia Atrás
def backward_algorithm(sequence):
    beta = []  # Almacenará las probabilidades hacia atrás
    # Inicialización
    beta_t = [1] * len(states)  # En el último tiempo, beta es 1
    beta.insert(0, beta_t)

    # Recursión hacia atrás
    for t in range(len(sequence) - 1, 0, -1):
        beta_t = []
        obs_index = observations.index(sequence[t])
        for i in range(len(states)):
            prob = sum(transition_probabilities[i][j] * emission_probabilities[j][observations.index(sequence[t])] * beta[0][j] for j in range(len(states)))
            beta_t.append(prob)
        beta.insert(0, beta_t)

    return beta

# Algoritmo Hacia Delante-Atrás
def forward_backward(sequence):
    alpha = forward_algorithm(sequence)
    beta = backward_algorithm(sequence)
    
    # Calcular la probabilidad total de la secuencia
    total_prob = sum(alpha[-1])  # Sumar las probabilidades de los estados en el último tiempo
    print(f"Probabilidad total de la secuencia: {total_prob:.4f}")

    # Calcular la probabilidad de cada estado en cada tiempo
    for t in range(len(sequence)):
        posterior = [alpha[t][i] * beta[t][i] / total_prob for i in range(len(states))]
        print(f"Probabilidades de estado en tiempo {t + 1}: {dict(zip(states, posterior))}")

# Ejecutar el algoritmo
print("Simulación del Algoritmo Hacia Delante-Atrás:")
forward_backward(sequence)
