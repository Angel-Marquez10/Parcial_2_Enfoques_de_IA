# Título: Inferencia por Enumeración
# Este código implementa la inferencia por enumeración para calcular la probabilidad de que un estudiante apruebe el examen.

# Introducción
print("Bienvenido a la práctica de Inferencia por Enumeración")
print("Este ejercicio calcula la probabilidad de que un estudiante apruebe un examen basado en si estudió o no.\n")

# Paso 1: Definir las probabilidades
P_A = 0.6  # Probabilidad de que el estudiante estudie (60%)
P_B_given_A = 0.8  # Probabilidad de que el estudiante apruebe dado que estudió (80%)
P_B_given_not_A = 0.4  # Probabilidad de que el estudiante apruebe dado que no estudió (40%)

# Paso 2: Calcular la probabilidad de que un estudiante apruebe (P(B)) usando la regla de la probabilidad total
P_not_A = 1 - P_A  # Probabilidad de que el estudiante no estudie
P_B = (P_B_given_A * P_A) + (P_B_given_not_A * P_not_A)  # Probabilidad total de aprobar

# Paso 3: Mostrar el resultado
print(f"La probabilidad de que un estudiante apruebe el examen es: {P_B:.4f}")

# Conclusión
print("\nConclusión:")
print("Hemos calculado la probabilidad de que un estudiante apruebe el examen utilizando la inferencia por enumeración.")
print("Este enfoque es útil cuando se pueden enumerar todas las combinaciones posibles de eventos.")
