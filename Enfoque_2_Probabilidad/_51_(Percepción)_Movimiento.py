
import numpy as np
import matplotlib.pyplot as plt

# Parámetros de simulación
num_pasos = 100
x = np.zeros(num_pasos)
y = np.zeros(num_pasos)

# Simular movimiento aleatorio
for i in range(1, num_pasos):
    direccion = np.random.choice(['arriba', 'abajo', 'izquierda', 'derecha'])
    if direccion == 'arriba':
        y[i] = y[i - 1] + 1
        x[i] = x[i - 1]
    elif direccion == 'abajo':
        y[i] = y[i - 1] - 1
        x[i] = x[i - 1]
    elif direccion == 'izquierda':
        x[i] = x[i - 1] - 1
        y[i] = y[i - 1]
    else:  # 'derecha'
        x[i] = x[i - 1] + 1
        y[i] = y[i - 1]

# Visualización del movimiento
plt.figure(figsize=(8, 8))
plt.plot(x, y, marker='o')
plt.title("Movimiento Aleatorio en 2D")
plt.xlabel("Posición en X")
plt.ylabel("Posición en Y")
plt.axhline(0, color='black', lw=0.5, ls='--')
plt.axvline(0, color='black', lw=0.5, ls='--')
plt.grid()
plt.xlim(-20, 20)
plt.ylim(-20, 20)
plt.show()
