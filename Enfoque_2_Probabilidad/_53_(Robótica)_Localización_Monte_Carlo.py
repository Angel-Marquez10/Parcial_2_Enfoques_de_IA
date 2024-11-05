
import numpy as np
import matplotlib.pyplot as plt

# Parámetros del entorno
num_particles = 1000
num_steps = 20
map_size = 10

# Inicializar partículas aleatorias
particles = np.random.rand(num_particles, 2) * map_size

# Simulación de movimiento
for step in range(num_steps):
    # Simular movimiento aleatorio
    movement = np.random.normal(0, 0.5, (num_particles, 2))  # Ruido en el movimiento
    particles += movement
    particles = np.clip(particles, 0, map_size)  # Mantener partículas dentro del mapa

# Visualización de las partículas
plt.figure(figsize=(8, 8))
plt.scatter(particles[:, 0], particles[:, 1], alpha=0.5)
plt.title("Localización Monte Carlo: Partículas")
plt.xlim(0, map_size)
plt.ylim(0, map_size)
plt.axhline(0, color='black', lw=0.5, ls='--')
plt.axvline(0, color='black', lw=0.5, ls='--')
plt.grid()
plt.show()
