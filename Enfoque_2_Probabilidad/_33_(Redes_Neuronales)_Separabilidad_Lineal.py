
import numpy as np
from sklearn.linear_model import Perceptron
from sklearn.datasets import make_blobs
import matplotlib.pyplot as plt

# Generación de datos linealmente separables
X, y = make_blobs(n_samples=100, centers=2, random_state=0, cluster_std=0.60)
y = np.where(y == 0, -1, 1)  # Cambiar etiquetas a -1 y 1 para Perceptrón

# Configuración del modelo de Perceptrón
modelo_perceptron = Perceptron()
modelo_perceptron.fit(X, y)

# Visualización de datos y frontera de decisión
plt.scatter(X[:, 0], X[:, 1], c=y, cmap='viridis', marker='o', edgecolor='k')
x_min, x_max = plt.xlim()
y_min, y_max = (-modelo_perceptron.coef_[0][0] * x_min - modelo_perceptron.intercept_[0]) / modelo_perceptron.coef_[0][1], (-modelo_perceptron.coef_[0][0] * x_max - modelo_perceptron.intercept_[0]) / modelo_perceptron.coef_[0][1]
plt.plot([x_min, x_max], [y_min, y_max], color='red', linestyle='--', label="Frontera de decisión")
plt.title("Separabilidad Lineal con Perceptrón")
plt.xlabel("Característica 1")
plt.ylabel("Característica 2")
plt.legend()
plt.show()
