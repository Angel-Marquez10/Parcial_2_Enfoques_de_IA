# Título: Simulación de Distribución de Probabilidad con Lanzamientos de Dados
# Este código simula el lanzamiento de un dado 10,000 veces y calcula la distribución de probabilidad empírica de los resultados.

import random
import matplotlib.pyplot as plt

# Introducción
print("Bienvenido a la práctica de Distribución de Probabilidad")
print("En esta práctica, simularemos el lanzamiento de un dado para observar la distribución de probabilidad de los resultados.\n")

# Paso 1: Definimos el número de lanzamientos
num_lanzamientos = 10000  # Simularemos 10,000 lanzamientos de un dado

# Paso 2: Inicializamos un diccionario para almacenar la frecuencia de cada resultado
frecuencias = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0}

# Paso 3: Simulamos los lanzamientos y contamos la frecuencia de cada resultado
for _ in range(num_lanzamientos):
    resultado = random.randint(1, 6)  # Genera un número aleatorio entre 1 y 6
    frecuencias[resultado] += 1

# Paso 4: Calculamos la distribución de probabilidad
# La probabilidad de cada resultado es su frecuencia relativa (frecuencia / número total de lanzamientos)
distribucion_probabilidad = {k: v / num_lanzamientos for k, v in frecuencias.items()}

# Imprimimos la distribución de probabilidad resultante
print("Distribución de Probabilidad (resultado / probabilidad):")
for resultado, probabilidad in distribucion_probabilidad.items():
    print(f"Resultado {resultado}: {probabilidad:.4f}")

# Paso 5: Visualizamos la distribución de probabilidad en un gráfico de barras
# Configuramos las etiquetas y valores para la gráfica
resultados = list(distribucion_probabilidad.keys())
probabilidades = list(distribucion_probabilidad.values())

plt.bar(resultados, probabilidades, color='skyblue')
plt.xlabel('Resultado del Dado')
plt.ylabel('Probabilidad')
plt.title('Distribución de Probabilidad Empírica de un Dado')
plt.ylim(0, 1/6 + 0.02)  # Ajustamos el límite de probabilidad para verlo claramente

# Mostrar la gráfica
plt.show()

# Conclusión
print("\nConclusión:")
print("En esta simulación, observamos cómo se distribuyen los resultados de los lanzamientos de un dado justo.")
print("La probabilidad empírica de cada número debería estar cerca de 1/6 si el dado es justo, y con suficientes lanzamientos.")
print("Esta es una forma simple de ver una distribución de probabilidad uniforme con resultados equiprobables.\n")
