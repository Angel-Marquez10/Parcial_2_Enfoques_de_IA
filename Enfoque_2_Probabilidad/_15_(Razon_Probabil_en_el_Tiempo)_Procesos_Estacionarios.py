import random
import matplotlib.pyplot as plt

# Título: Simulación de un Proceso Estacionario
# Este código simula un proceso de caminata aleatoria que representa un proceso estacionario.

# Parámetros de la simulación
num_steps = 1000  # Número total de pasos
num_walkers = 100  # Número de caminantes

# Inicializar la lista de posiciones de los caminantes
positions = [0] * num_walkers

# Almacenar las posiciones a lo largo del tiempo
all_positions = [[] for _ in range(num_walkers)]

# Simulación de la caminata aleatoria
for step in range(num_steps):
    for i in range(num_walkers):
        # Elegir aleatoriamente avanzar (1) o retroceder (-1)
        step_direction = random.choice([-1, 1])
        positions[i] += step_direction
        all_positions[i].append(positions[i])

# Visualización de las posiciones de los caminantes
plt.figure(figsize=(12, 6))
for i in range(num_walkers):
    plt.plot(all_positions[i], alpha=0.5)  # Graficar cada caminante

plt.title("Simulación de Caminata Aleatoria")
plt.xlabel("Número de Pasos")
plt.ylabel("Posición")
plt.axhline(0, color='black', lw=0.5, ls='--')  # Línea en y=0
plt.grid()
plt.show()

# Análisis de la distribución final de las posiciones
final_positions = [positions[i] for i in range(num_walkers)]
mean_position = sum(final_positions) / num_walkers
print(f"Posición Media de los Caminantes: {mean_position:.2f}")
