
import numpy as np
import matplotlib.pyplot as plt

# Parámetros del entorno
num_particles = 100
map_size = 10
num_steps = 50
motion_noise = 0.5  # Ruido en el movimiento

# Inicializar partículas aleatorias
particles = np.random.rand(num_particles, 2) * map_size

# Simulación de movimiento con incertidumbre
for _ in range(num_steps):
    # Movimiento con ruido
    movement = np.random.normal(1, motion_noise, (num_particles, 2))  # Movimiento en x e y
    particles += movement
    particles = np.clip(particles, 0, map_size)  # Mantener partículas dentro del mapa

# Visualización de las partículas
plt.figure(figsize=(8, 8))
plt.scatter(particles[:, 0], particles[:, 1], alpha=0.5, label='Partículas con incertidumbre')
plt.title("Incertidumbre en el Movimiento del Robot")
plt.xlim(0, map_size)
plt.ylim(0, map_size)
plt.axhline(0, color='black', lw=0.5, ls='--')
plt.axvline(0, color='black', lw=0.5, ls='--')
plt.grid()
plt.legend()
plt.show()
