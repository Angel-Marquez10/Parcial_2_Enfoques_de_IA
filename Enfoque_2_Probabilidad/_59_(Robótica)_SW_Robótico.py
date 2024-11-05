
import numpy as np
import matplotlib.pyplot as plt

class Robot:
    def __init__(self, x=0, y=0):
        self.position = np.array([x, y])
    
    def move(self, direction):
        if direction == 'up':
            self.position[1] += 1
        elif direction == 'down':
            self.position[1] -= 1
        elif direction == 'left':
            self.position[0] -= 1
        elif direction == 'right':
            self.position[0] += 1
    
    def get_position(self):
        return self.position

# Inicializar el robot
robot = Robot()

# Simulación de movimientos
movements = ['up', 'up', 'right', 'down', 'left', 'left', 'up']
positions = []

for move in movements:
    robot.move(move)
    positions.append(robot.get_position().copy())

# Convertir posiciones a un array para visualización
positions = np.array(positions)

# Visualización del movimiento del robot
plt.figure(figsize=(8, 8))
plt.plot(positions[:, 0], positions[:, 1], marker='o', color='blue', label='Trayectoria del robot')
plt.title('Movimiento del Robot en un Entorno 2D')
plt.xlim(-3, 5)
plt.ylim(-3, 5)
plt.axhline(0, color='black', lw=0.5, ls='--')
plt.axvline(0, color='black', lw=0.5, ls='--')
plt.grid()
plt.legend()
plt.show()
