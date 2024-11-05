
import numpy as np
import matplotlib.pyplot as plt

# Generación de datos de ejemplo
x = np.linspace(0, 10, 100)
y1 = np.sin(x)
y2 = np.cos(x)

# Creación del gráfico
plt.figure(figsize=(10, 5))
plt.plot(x, y1, label='Seno', color='blue')
plt.plot(x, y2, label='Coseno', color='green')

# Etiquetado de líneas
for i in range(0, len(x), 10):  # Etiquetar cada 10 puntos
    plt.text(x[i], y1[i], f'({x[i]:.1f}, {y1[i]:.2f})', fontsize=8, color='blue')
    plt.text(x[i], y2[i], f'({x[i]:.1f}, {y2[i]:.2f})', fontsize=8, color='green')

plt.title('Gráfico de Seno y Coseno con Etiquetas')
plt.xlabel('Eje X')
plt.ylabel('Eje Y')
plt.axhline(0, color='black', lw=0.5, ls='--')
plt.axvline(0, color='black', lw=0.5, ls='--')
plt.legend()
plt.grid(True)
plt.show()
