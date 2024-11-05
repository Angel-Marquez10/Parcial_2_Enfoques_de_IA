
import numpy as np
import matplotlib.pyplot as plt

# Parámetros del manipulador
l1 = 5  # Longitud del primer brazo
l2 = 5  # Longitud del segundo brazo

# Función de cinemática inversa
def inverse_kinematics(x, y):
    d = np.sqrt(x**2 + y**2)  # Distancia al objetivo
    if d > l1 + l2:
        raise ValueError("El objetivo está fuera de alcance")
    
    # Calcular ángulo 2
    theta2 = np.arccos((d**2 - l1**2 - l2**2) / (2 * l1 * l2))
    
    # Calcular ángulo 1
    theta1 = np.arctan2(y, x) - np.arctan2(l2 * np.sin(theta2), l1 + l2 * np.cos(theta2))
    
    return theta1, theta2

# Objetivo
target = np.array([6, 3])  # Posición del objetivo

# Calcular los ángulos
theta1, theta2 = inverse_kinematics(target[0], target[1])
print(f"Ángulo 1: {np.degrees(theta1):.2f} grados")
print(f"Ángulo 2: {np.degrees(theta2):.2f} grados")

# Visualizar el manipulador
x1 = l1 * np.cos(theta1)
y1 = l1 * np.sin(theta1)
x2 = x1 + l2 * np.cos(theta1 + theta2)
y2 = y1 + l2 * np.sin(theta1 + theta2)

plt.figure(figsize=(8, 8))
plt.plot([0, x1], [0, y1], 'r', lw=5, label='Brazo 1')
plt.plot([x1, x2], [y1, y2], 'b', lw=5, label='Brazo 2')
plt.plot(target[0], target[1], 'go', markersize=10, label='Objetivo')
plt.xlim(-1, 11)
plt.ylim(-1, 11)
plt.axhline(0, color='black', lw=0.5, ls='--')
plt.axvline(0, color='black', lw=0.5, ls='--')
plt.title("Cinemática Inversa de un Manipulador 2D")
plt.legend()
plt.grid()
plt.show()
