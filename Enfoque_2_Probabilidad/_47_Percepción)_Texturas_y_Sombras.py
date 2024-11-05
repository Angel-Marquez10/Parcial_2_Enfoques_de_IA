
import cv2
import numpy as np
import matplotlib.pyplot as plt

# Cargar una imagen de ejemplo
imagen = cv2.imread('ejemplo.jpg')  # Asegúrate de que la imagen esté en el mismo directorio
imagen_gris = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)  # Convertir a escala de grises

# Aplicar un filtro de Gabor para detectar texturas
def gabor_filter(img, kernel_size=31, sigma=4.0, theta=1.0, lambd=10.0, gamma=0.5):
    kernel = cv2.getGaborKernel((kernel_size, kernel_size), sigma, theta, lambd, gamma, 0, ktype=cv2.CV_32F)
    return cv2.filter2D(img, cv2.CV_8UC3, kernel)

# Aplicar el filtro Gabor
textura = gabor_filter(imagen_gris)

# Visualización de los resultados
plt.figure(figsize=(10, 5))
plt.subplot(1, 2, 1)
plt.imshow(imagen_gris, cmap='gray')
plt.title('Imagen Original en Escala de Grises')
plt.axis('off')

plt.subplot(1, 2, 2)
plt.imshow(textura, cmap='gray')
plt.title('Detección de Texturas con Filtro de Gabor')
plt.axis('off')

plt.show()
