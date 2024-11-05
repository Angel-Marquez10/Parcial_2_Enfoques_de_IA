
import numpy as np
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from sklearn.datasets import make_blobs
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt

# Generación de datos simulados
X, y = make_blobs(n_samples=500, centers=2, random_state=0)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=0)

# Escalado de datos
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# Construcción de la red neuronal simple
modelo = Sequential([
    Dense(10, input_shape=(2,), activation='relu'),  # Capa oculta con función de activación ReLU
    Dense(1, activation='sigmoid')                    # Capa de salida con función de activación Sigmoide
])

modelo.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

# Entrenamiento del modelo
historial = modelo.fit(X_train, y_train, epochs=50, batch_size=10, validation_data=(X_test, y_test))

# Visualización de los resultados de entrenamiento
plt.plot(historial.history['accuracy'], label='Entrenamiento')
plt.plot(historial.history['val_accuracy'], label='Validación')
plt.title("Precisión durante el entrenamiento")
plt.xlabel("Épocas")
plt.ylabel("Precisión")
plt.legend()
plt.show()
