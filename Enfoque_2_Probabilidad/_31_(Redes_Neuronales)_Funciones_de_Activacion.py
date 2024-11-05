
import numpy as np
import matplotlib.pyplot as plt

# Definición de funciones de activación
def sigmoid(x):
    return 1 / (1 + np.exp(-x))

def relu(x):
    return np.maximum(0, x)

def tanh(x):
    return np.tanh(x)

# Rango de valores de entrada
x = np.linspace(-10, 10, 100)

# Cálculo de las salidas para cada función de activación
y_sigmoid = sigmoid(x)
y_relu = relu(x)
y_tanh = tanh(x)

# Visualización de las funciones de activación
plt.figure(figsize=(10, 6))
plt.plot(x, y_sigmoid, label='Sigmoid', color='blue')
plt.plot(x, y_relu, label='ReLU', color='green')
plt.plot(x, y_tanh, label='Tanh', color='red')
plt.title("Funciones de Activación")
plt.xlabel("Entrada")
plt.ylabel("Salida")
plt.legend()
plt.grid(True)
plt.show()
