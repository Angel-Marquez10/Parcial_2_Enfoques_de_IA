
import numpy as np
from hmmlearn import hmm

# Generación de una secuencia de observaciones simulada
observaciones = np.array([[0], [1], [0], [1], [1], [0], [1], [0]]).reshape(-1, 1)

# Configuración del modelo HMM
modelo_hmm = hmm.MultinomialHMM(n_components=2, n_iter=100, random_state=0)
modelo_hmm.startprob_ = np.array([0.6, 0.4])  # Probabilidades iniciales
modelo_hmm.transmat_ = np.array([[0.7, 0.3], [0.4, 0.6]])  # Matriz de transición
modelo_hmm.emissionprob_ = np.array([[0.6, 0.4], [0.3, 0.7]])  # Matriz de emisión

# Entrenamiento y predicción de estados ocultos
modelo_hmm.fit(observaciones)
log_prob, estados_ocultos = modelo_hmm.decode(observaciones, algorithm="viterbi")

print("Secuencia de estados ocultos:", estados_ocultos)
print("Log-probabilidad de la secuencia:", log_prob)
