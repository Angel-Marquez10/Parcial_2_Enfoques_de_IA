# Título: Cálculo de Probabilidad usando la Regla de Bayes
# Este código implementa un ejemplo de la Regla de Bayes para calcular la probabilidad de tener una enfermedad dado un resultado positivo en una prueba de diagnóstico.

# Introducción
print("Bienvenido a la práctica de la Regla de Bayes")
print("En este ejercicio, calcularemos la probabilidad de que una persona tenga una enfermedad dado que el resultado de una prueba ha sido positivo.\n")

# Paso 1: Definir las probabilidades iniciales (prior, sensibilidad y tasa de falso positivo)
prob_enfermedad = 0.01                # P(enfermedad)
prob_positivo_given_enfermedad = 0.9   # P(positivo | enfermedad)
prob_positivo_given_no_enfermedad = 0.05  # P(positivo | no enfermedad)

# Paso 2: Calcular la probabilidad total de obtener un resultado positivo, P(positivo)
# Usamos la ley de la probabilidad total
prob_no_enfermedad = 1 - prob_enfermedad  # P(no enfermedad)
prob_positivo = (prob_positivo_given_enfermedad * prob_enfermedad) + (prob_positivo_given_no_enfermedad * prob_no_enfermedad)

# Paso 3: Aplicar la Regla de Bayes para encontrar P(enfermedad | positivo)
prob_enfermedad_given_positivo = (prob_positivo_given_enfermedad * prob_enfermedad) / prob_positivo

# Mostrar resultados
print("Probabilidades iniciales:")
print(f"P(Enfermedad): {prob_enfermedad}")
print(f"P(Positivo | Enfermedad): {prob_positivo_given_enfermedad}")
print(f"P(Positivo | No Enfermedad): {prob_positivo_given_no_enfermedad}")
print(f"P(Positivo): {prob_positivo:.4f}")

print("\nResultado:")
print(f"La probabilidad de tener la enfermedad dado un resultado positivo es: {prob_enfermedad_given_positivo:.4f}")

# Conclusión
print("\nConclusión:")
print("Este cálculo muestra cómo la Regla de Bayes nos permite actualizar nuestra creencia inicial sobre la probabilidad de una enfermedad")
print("una vez que tenemos evidencia adicional (resultado positivo en la prueba). Este tipo de análisis es útil en diagnósticos médicos y en la toma de decisiones bajo incertidumbre.")
