
import cv2
import numpy as np
import tensorflow as tf
from tensorflow.keras.applications import MobileNetV2
from tensorflow.keras.applications.mobilenet_v2 import preprocess_input, decode_predictions
from tensorflow.keras.preprocessing import image
import matplotlib.pyplot as plt

# Cargar el modelo preentrenado de MobileNetV2
model = MobileNetV2(weights='imagenet')

# Cargar una imagen de ejemplo
img_path = 'ejemplo.jpg'  # Asegúrate de que la imagen esté en el mismo directorio
img = image.load_img(img_path, target_size=(224, 224))
img_array = image.img_to_array(img)
img_array = np.expand_dims(img_array, axis=0)
img_array = preprocess_input(img_array)

# Realizar la predicción
predicciones = model.predict(img_array)
decoded_predictions = decode_predictions(predicciones, top=5)[0]

# Mostrar resultados
print("Predicciones:")
for i, (imagenet_id, label, score) in enumerate(decoded_predictions):
    print(f"{i + 1}: {label} ({score:.2f})")

# Visualizar la imagen
plt.imshow(img)
plt.axis('off')
plt.title("Reconocimiento de Objetos")
plt.show()
