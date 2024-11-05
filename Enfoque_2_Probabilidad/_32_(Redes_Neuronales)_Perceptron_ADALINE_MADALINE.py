
import numpy as np
from sklearn.linear_model import Perceptron
from sklearn.linear_model import SGDRegressor
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt

# Generación de datos de ejemplo
X, y = make_classification(n_samples=100, n_features=2, n_informative=2, n_redundant=0, random_state=0)
y = np.where(y == 0, -1, 1)  # Cambiar etiquetas a -1 y 1 para ADALINE
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=0)

# Perceptrón
modelo_perceptron = Perceptron()
modelo_perceptron.fit(X_train, y_train)
print("Precisión del Perceptrón:", modelo_perceptron.score(X_test, y_test))

# ADALINE
modelo_adaline = SGDRegressor(max_iter=1000, tol=1e-3)
modelo_adaline.fit(X_train, y_train)
print("Precisión de ADALINE:", modelo_adaline.score(X_test, y_test))

# Visualización de la clasificación con Perceptrón
plt.scatter(X[:, 0], X[:, 1], c=y, cmap='viridis')
plt.title("Clasificación con Perceptrón y ADALINE")
plt.xlabel("Característica 1")
plt.ylabel("Característica 2")
plt.show()
