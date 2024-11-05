import numpy as np

# Título: Eliminación de Variables
# Este código implementa la eliminación de variables para calcular la probabilidad de que un estudiante apruebe un examen dado que asistió a clases.

# Introducción
print("Bienvenido a la práctica de Eliminación de Variables")
print("Este ejercicio calcula la probabilidad de que un estudiante apruebe el examen dado que asistió a clases.\n")

# Paso 1: Definir las probabilidades
P_A_given_C = 0.7  # Probabilidad de que el estudiante estudie dado que asistió a clases (70%)
P_B_given_A_C = 0.9  # Probabilidad de que el estudiante apruebe dado que estudió y asistió a clases (90%)
P_B_given_not_A_C = 0.5  # Probabilidad de que el estudiante apruebe dado que no estudió pero asistió a clases (50%)

# Paso 2: Calcular la probabilidad de que un estudiante apruebe (P(B|C)) usando la eliminación de variables
P_B_given_C = (P_B_given_A_C * P_A_given_C) + (P_B_given_not_A_C * (1 - P_A_given_C))

# Paso 3: Mostrar el resultado
print(f"La probabilidad de que un estudiante apruebe el examen dado que asistió a clases es: {P_B_given_C:.4f}")

# Conclusión
print("\nConclusión:")
print("Hemos calculado la probabilidad de que un estudiante apruebe el examen usando la eliminación de variables.")
print("Este enfoque permite calcular probabilidades marginales considerando la relación entre las variables.")
