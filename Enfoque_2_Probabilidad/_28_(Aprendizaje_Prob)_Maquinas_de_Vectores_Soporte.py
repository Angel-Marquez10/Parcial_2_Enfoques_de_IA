
import numpy as np
from sklearn.svm import SVC
import matplotlib.pyplot as plt
from sklearn.datasets import make_circles

# Generación de datos no linealmente separables
X, y = make_circles(n_samples=100, factor=0.5, noise=0.1, random_state=0)

# Configuración del modelo SVM con núcleo RBF
modelo_svm = SVC(kernel='rbf', C=1, gamma=0.5)
modelo_svm.fit(X, y)

# Visualización de resultados
def plot_svm_decision_boundary(model, X, y):
    x_min, x_max = X[:, 0].min() - 1, X[:, 0].max() + 1
    y_min, y_max = X[:, 1].min() - 1, X[:, 1].max() + 1
    xx, yy = np.meshgrid(np.linspace(x_min, x_max, 100), np.linspace(y_min, y_max, 100))
    Z = model.predict(np.c_[xx.ravel(), yy.ravel()])
    Z = Z.reshape(xx.shape)

    plt.contourf(xx, yy, Z, alpha=0.3)
    plt.scatter(X[:, 0], X[:, 1], c=y, edgecolor='k', marker='o')
    plt.title("Máquinas de Vectores Soporte con Núcleo RBF")
    plt.xlabel("Característica 1")
    plt.ylabel("Característica 2")
    plt.show()

plot_svm_decision_boundary(modelo_svm, X, y)
