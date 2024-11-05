import numpy as np
import matplotlib.pyplot as plt

# Título: Implementación de un Filtro de Kalman
# Este código simula un Filtro de Kalman para estimar la posición de un objeto en movimiento.

# Parámetros de simulación
dt = 1.0  # Intervalo de tiempo (segundos)
num_steps = 50  # Número de pasos de tiempo

# Inicialización de matrices para el filtro de Kalman
# Estado inicial: [posición, velocidad]
x = np.array([[0],  # Posición inicial
              [1]])  # Velocidad inicial

# Matriz de estado
F = np.array([[1, dt],  # Matriz de transición
              [0, 1]])

# Matriz de observación
H = np.array([[1, 0]])  # Solo observamos la posición

# Matriz de covarianza del proceso
Q = np.array([[1, 0],  # Ruido del proceso
              [0, 1]])

# Matriz de covarianza de la observación
R = np.array([[5]])  # Ruido de la medición

# Matriz de covarianza del estado
P = np.eye(2)  # Inicialmente, la incertidumbre es máxima

# Listas para almacenar posiciones reales y estimadas
true_positions = []
measurements = []
estimated_positions = []

# Simulación de movimiento y filtrado
for _ in range(num_steps):
    # Generar movimiento real (con ruido)
    true_position = x[0, 0] + x[1, 0] * dt + np.random.normal(0, 1)
    true_positions.append(true_position)

    # Medición (con ruido)
    measurement = true_position + np.random.normal(0, 5)
    measurements.append(measurement)

    # Predicción
    x = F @ x  # Predicción del estado
    P = F @ P @ F.T + Q  # Predicción de la covarianza

    # Actualización
    y = measurement - (H @ x)  # Residuos
    S = H @ P @ H.T + R  # Covarianza del residuo
    K = P @ H.T @ np.linalg.inv(S)  # Ganancia de Kalman

    x = x + K @ y  # Estado actualizado
    P = (np.eye(2) - K @ H) @ P  # Covarianza actualizada

    estimated_positions.append(x[0, 0])  # Guardar la posición estimada

# Visualización de resultados
plt.figure(figsize=(10, 5))
plt.plot(true_positions, label='Posición real', color='g')
plt.scatter(range(num_steps), measurements, label='Mediciones', color='r', s=10)
plt.plot(estimated_positions, label='Posición estimada', color='b')
plt.title('Filtro de Kalman: Estimación de Posición')
plt.xlabel('Pasos de tiempo')
plt.ylabel('Posición')
plt.legend()
plt.grid()
plt.show()
