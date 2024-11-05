
import cv2
import numpy as np
import matplotlib.pyplot as plt

# Cargar una imagen de ejemplo
imagen = cv2.imread('ejemplo.jpg')  # Asegúrate de que la imagen esté en el mismo directorio
imagen_gris = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)  # Convertir a escala de grises

# Detección de aristas usando el operador Canny
edges = cv2.Canny(imagen_gris, 100, 200)

# Segmentación de la imagen utilizando un umbral
_, segmentacion = cv2.threshold(imagen_gris, 128, 255, cv2.THRESH_BINARY)

# Visualización de los resultados
plt.figure(figsize=(15, 5))
plt.subplot(1, 3, 1)
plt.imshow(imagen)
plt.title('Imagen Original')
plt.axis('off')

plt.subplot(1, 3, 2)
plt.imshow(edges, cmap='gray')
plt.title('Detección de Aristas')
plt.axis('off')

plt.subplot(1, 3, 3)
plt.imshow(segmentacion, cmap='gray')
plt.title('Segmentación')
plt.axis('off')

plt.show()
