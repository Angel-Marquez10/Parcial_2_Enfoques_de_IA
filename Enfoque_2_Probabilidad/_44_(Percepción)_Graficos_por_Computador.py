
import numpy as np
import matplotlib.pyplot as plt

# Generación de datos de ejemplo
x = np.linspace(0, 10, 100)
y = np.sin(x)

# Creación del gráfico
plt.figure(figsize=(10, 5))
plt.plot(x, y, label='Seno', color='blue')
plt.title('Gráfico de la función seno')
plt.xlabel('Eje X')
plt.ylabel('Eje Y')
plt.axhline(0, color='black', lw=0.5, ls='--')
plt.axvline(0, color='black', lw=0.5, ls='--')
plt.grid(True)
plt.legend()
plt.show()
