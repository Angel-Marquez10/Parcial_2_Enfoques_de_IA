
import numpy as np
import matplotlib.pyplot as plt

# Parámetros del entorno
num_steps = 50
map_size = 10

# Inicializar la posición del robot
robot_position = np.array([0, 0])
positions = [robot_position.copy()]

# Simulación de movimiento
for _ in range(num_steps):
    # Movimiento aleatorio
    movement = np.random.choice([-1, 0, 1], size=2)  # Movimiento en x e y
    robot_position += movement
    robot_position = np.clip(robot_position, 0, map_size)  # Mantener dentro del mapa
    positions.append(robot_position.copy())

# Convertir posiciones a un array
positions = np.array(positions)

# Visualización del movimiento en el espacio de configuración
plt.figure(figsize=(8, 8))
plt.plot(positions[:, 0], positions[:, 1], marker='o')
plt.title("Movimiento en el Espacio de Configuración")
plt.xlim(0, map_size)
plt.ylim(0, map_size)
plt.axhline(0, color='black', lw=0.5, ls='--')
plt.axvline(0, color='black', lw=0.5, ls='--')
plt.grid()
plt.show()
