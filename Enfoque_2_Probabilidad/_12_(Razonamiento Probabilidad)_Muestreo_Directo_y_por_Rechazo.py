import numpy as np
import random
import matplotlib.pyplot as plt

# Título: Muestreo Directo y Por Rechazo
# Este código implementa muestreo directo y por rechazo utilizando una distribución de probabilidad.

# Introducción
print("Bienvenido a la práctica de Muestreo Directo y Por Rechazo")
print("Este ejercicio simula el lanzamiento de un dado de seis caras utilizando ambos métodos de muestreo.\n")

# Definir la función de densidad de probabilidad para un dado de seis caras
def probability_distribution():
    return np.array([1/6] * 6)  # Cada cara tiene una probabilidad de 1/6

# Muestreo Directo
def direct_sampling(num_samples):
    outcomes = np.arange(1, 7)  # Resultados posibles: 1, 2, 3, 4, 5, 6
    probabilities = probability_distribution()  # Probabilidades
    samples = np.random.choice(outcomes, size=num_samples, p=probabilities)  # Muestreo directo
    return samples

# Muestreo por Rechazo
def rejection_sampling(num_samples):
    outcomes = np.arange(1, 7)  # Resultados posibles: 1, 2, 3, 4, 5, 6
    probabilities = probability_distribution()  # Probabilidades
    max_prob = max(probabilities)  # Máxima probabilidad para escalado
    samples = []

    while len(samples) < num_samples:
        x = random.choice(outcomes)  # Elegir un resultado aleatorio
        u = random.uniform(0, max_prob)  # Elegir un valor de uniformemente aleatorio
        if u < probabilities[x - 1]:  # Rechazo basado en la probabilidad
            samples.append(x)

    return samples

# Número de muestras a generar
num_samples = 1000

# Generar muestras
direct_samples = direct_sampling(num_samples)
rejection_samples = rejection_sampling(num_samples)

# Visualizar resultados
plt.figure(figsize=(12, 5))

# Histograma de muestreo directo
plt.subplot(1, 2, 1)
plt.hist(direct_samples, bins=np.arange(1, 8), density=True, alpha=0.7, color='blue', edgecolor='black')
plt.title('Muestreo Directo')
plt.xlabel('Resultado')
plt.ylabel('Frecuencia relativa')
plt.xticks(np.arange(1, 7))

# Histograma de muestreo por rechazo
plt.subplot(1, 2, 2)
plt.hist(rejection_samples, bins=np.arange(1, 8), density=True, alpha=0.7, color='orange', edgecolor='black')
plt.title('Muestreo por Rechazo')
plt.xlabel('Resultado')
plt.ylabel('Frecuencia relativa')
plt.xticks(np.arange(1, 7))

plt.tight_layout()
plt.show()

# Conclusión
print("\nConclusión:")
print("Hemos simulado el lanzamiento de un dado utilizando muestreo directo y muestreo por rechazo.")
print("Ambos métodos permiten obtener muestras de una distribución de probabilidad, pero difieren en su enfoque.")
