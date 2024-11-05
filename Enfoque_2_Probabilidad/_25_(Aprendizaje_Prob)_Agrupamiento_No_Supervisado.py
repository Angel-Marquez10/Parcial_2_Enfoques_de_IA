
import numpy as np
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

# Generación de datos de ejemplo
np.random.seed(0)
grupo1 = np.random.normal(5, 1, (50, 2))
grupo2 = np.random.normal(15, 1, (50, 2))
datos = np.vstack((grupo1, grupo2))

# Configuración del modelo k-means
kmeans = KMeans(n_clusters=2, random_state=0)
kmeans.fit(datos)
etiquetas = kmeans.labels_

# Visualización de los resultados
plt.scatter(datos[:, 0], datos[:, 1], c=etiquetas, cmap='viridis', marker='o', edgecolor='k')
plt.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1], s=200, c='red', label='Centroides')
plt.title("Agrupamiento No Supervisado con K-means")
plt.xlabel("Característica 1")
plt.ylabel("Característica 2")
plt.legend()
plt.show()
