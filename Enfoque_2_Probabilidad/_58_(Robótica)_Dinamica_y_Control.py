
import numpy as np
import matplotlib.pyplot as plt

# Parámetros del sistema
time_steps = 100
dt = 0.1  # Intervalo de tiempo
target_position = 10.0  # Posición objetivo

# Inicializar variables
position = 0.0
velocity = 0.0
positions = []

# Simulación del control proporcional
for _ in range(time_steps):
    error = target_position - position  # Cálculo del error
    control_signal = error * 0.5  # Control proporcional (Kp = 0.5)

    # Actualizar la posición y velocidad
    velocity += control_signal * dt
    position += velocity * dt
    positions.append(position)

# Visualización de la posición a lo largo del tiempo
plt.figure(figsize=(10, 5))
plt.plot(positions, label='Posición del sistema', color='blue')
plt.axhline(target_position, color='red', linestyle='--', label='Posición objetivo')
plt.title('Dinámica y Control: Posición del Sistema')
plt.xlabel('Tiempo (s)')
plt.ylabel('Posición')
plt.legend()
plt.grid()
plt.show()
