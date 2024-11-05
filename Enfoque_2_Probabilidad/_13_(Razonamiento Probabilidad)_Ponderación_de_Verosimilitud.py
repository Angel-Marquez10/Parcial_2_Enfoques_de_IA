import numpy as np
import matplotlib.pyplot as plt

# Título: Ponderación de Verosimilitud
# Este código calcula la verosimilitud de dos modelos diferentes dados algunos datos observados.

# Introducción
print("Bienvenido a la práctica de Ponderación de Verosimilitud")
print("Este ejercicio calcula la verosimilitud de dos modelos y los compara.\n")

# Datos observados (puedes cambiar estos datos)
observed_data = np.array([2, 3, 3, 4, 4, 5, 5, 5])  # Resultados observados

# Definición de dos modelos (distribuciones de probabilidad)
def model_1(x):
    # Modelo 1: Media 4, Desviación estándar 1
    mean = 4
    std_dev = 1
    return (1 / (std_dev * np.sqrt(2 * np.pi))) * np.exp(-0.5 * ((x - mean) / std_dev) ** 2)

def model_2(x):
    # Modelo 2: Media 3, Desviación estándar 1.5
    mean = 3
    std_dev = 1.5
    return (1 / (std_dev * np.sqrt(2 * np.pi))) * np.exp(-0.5 * ((x - mean) / std_dev) ** 2)

# Cálculo de la verosimilitud para cada modelo
def calculate_likelihood(model, data):
    likelihood = np.prod(model(data))  # Producto de las verosimilitudes
    return likelihood

# Calcular la verosimilitud para ambos modelos
likelihood_model_1 = calculate_likelihood(model_1, observed_data)
likelihood_model_2 = calculate_likelihood(model_2, observed_data)

# Ponderación de verosimilitud
total_likelihood = likelihood_model_1 + likelihood_model_2
weight_model_1 = likelihood_model_1 / total_likelihood
weight_model_2 = likelihood_model_2 / total_likelihood

# Resultados
print(f"Verosimilitud del Modelo 1: {likelihood_model_1:.4f}")
print(f"Verosimilitud del Modelo 2: {likelihood_model_2:.4f}")
print(f"Ponderación del Modelo 1: {weight_model_1:.4f}")
print(f"Ponderación del Modelo 2: {weight_model_2:.4f}")

# Visualización
models = ['Modelo 1', 'Modelo 2']
weights = [weight_model_1, weight_model_2]

plt.bar(models, weights, color=['blue', 'orange'])
plt.title('Ponderación de Verosimilitud')
plt.ylabel('Ponderación')
plt.ylim(0, 1)
plt.grid(axis='y')
plt.show()

# Conclusión
print("\nConclusión:")
print("Hemos calculado la verosimilitud de dos modelos dados los datos observados.")
print("La ponderación de verosimilitud nos permite comparar la plausibilidad de cada modelo.")

