
import cv2
import numpy as np
import matplotlib.pyplot as plt

# Cargar una imagen de ejemplo
imagen = cv2.imread('ejemplo.jpg')  # Asegúrate de que la imagen esté en el mismo directorio
imagen = cv2.cvtColor(imagen, cv2.COLOR_BGR2RGB)  # Convertir de BGR a RGB

# Aplicar un filtro de desenfoque
filtro_desenfoque = cv2.GaussianBlur(imagen, (15, 15), 0)

# Visualizar la imagen original y la filtrada
plt.figure(figsize=(10, 5))
plt.subplot(1, 2, 1)
plt.imshow(imagen)
plt.title('Imagen Original')
plt.axis('off')

plt.subplot(1, 2, 2)
plt.imshow(filtro_desenfoque)
plt.title('Imagen con Desenfoque')
plt.axis('off')

plt.show()
