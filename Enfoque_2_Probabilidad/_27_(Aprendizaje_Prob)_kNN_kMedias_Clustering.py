
import numpy as np
from sklearn.cluster import KMeans
from sklearn.neighbors import KNeighborsClassifier
import matplotlib.pyplot as plt

# Generación de datos de ejemplo para clustering y clasificación
np.random.seed(0)
grupo1 = np.random.normal(5, 1, (50, 2))
grupo2 = np.random.normal(15, 1, (50, 2))
grupo3 = np.random.normal(10, 1, (50, 2))
datos_clustering = np.vstack((grupo1, grupo2, grupo3))

# k-means clustering
kmeans = KMeans(n_clusters=3, random_state=0)
kmeans.fit(datos_clustering)
etiquetas_kmeans = kmeans.labels_

# Generación de datos etiquetados para k-NN
datos_knn = np.vstack((grupo1, grupo2))
etiquetas_knn = np.array([0]*50 + [1]*50)

# Modelo k-NN y predicción de una nueva instancia
knn = KNeighborsClassifier(n_neighbors=3)
knn.fit(datos_knn, etiquetas_knn)
nueva_instancia = np.array([[12, 12]])
prediccion = knn.predict(nueva_instancia)

# Visualización de k-means clustering y k-NN
plt.scatter(datos_clustering[:, 0], datos_clustering[:, 1], c=etiquetas_kmeans, cmap='viridis', marker='o', edgecolor='k', label="k-means")
plt.scatter(nueva_instancia[:, 0], nueva_instancia[:, 1], color='red', marker='x', s=100, label="Nueva instancia (k-NN)")
plt.title("k-means Clustering y Clasificación k-NN")
plt.xlabel("Característica 1")
plt.ylabel("Característica 2")
plt.legend()
plt.show()

print(f"Clasificación de la nueva instancia con k-NN: {prediccion[0]}")
