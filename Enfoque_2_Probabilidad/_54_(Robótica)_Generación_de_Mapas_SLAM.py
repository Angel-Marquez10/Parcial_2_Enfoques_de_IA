
import numpy as np
import matplotlib.pyplot as plt

# Parámetros del entorno
num_particles = 100
map_size = 10
num_steps = 30

# Inicializar partículas aleatorias
particles = np.random.rand(num_particles, 2) * map_size

# Simulación de movimiento y observaciones
for step in range(num_steps):
    # Simular movimiento aleatorio
    movement = np.random.normal(0, 0.5, (num_particles, 2))
    particles += movement
    particles = np.clip(particles, 0, map_size)  # Mantener partículas dentro del mapa

    # Simular observaciones
    # (En un caso real, aquí se incluirían las observaciones del entorno)

# Visualización de las partículas y el mapa
plt.figure(figsize=(8, 8))
plt.scatter(particles[:, 0], particles[:, 1], alpha=0.5, label='Partículas')
plt.title("Generación de Mapas: SLAM")
plt.xlim(0, map_size)
plt.ylim(0, map_size)
plt.axhline(0, color='black', lw=0.5, ls='--')
plt.axvline(0, color='black', lw=0.5, ls='--')
plt.grid()
plt.legend()
plt.show()
