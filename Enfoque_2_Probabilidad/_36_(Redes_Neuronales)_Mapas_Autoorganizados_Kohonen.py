
import numpy as np
import matplotlib.pyplot as plt
from minisom import MiniSom

# Generación de datos de ejemplo
X = np.random.rand(100, 3)  # 100 muestras con 3 características

# Inicialización y entrenamiento del mapa
som = MiniSom(x=10, y=10, input_len=3, sigma=1.0, learning_rate=0.5)
som.train(X, num_iteration=100)

# Visualización de los resultados
plt.figure(figsize=(8, 8))
for i, x in enumerate(X):
    w = som.winner(x)
    plt.text(w[0], w[1], 'o', color='C{}'.format(int(y[i])), ha='center', va='center')
plt.title("Mapa Autoorganizado de Kohonen")
plt.xlabel("Ejes X")
plt.ylabel("Ejes Y")
plt.grid()
plt.show()
