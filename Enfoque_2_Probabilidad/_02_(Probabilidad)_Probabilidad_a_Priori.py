# Título: Introducción a la Probabilidad a Priori en Python
# En esta práctica, exploraremos el concepto de probabilidad a priori mediante un ejemplo de diagnóstico médico.

# Introducción
print("Bienvenido a la práctica de Probabilidad a Priori")
print("Esta práctica muestra cómo la probabilidad a priori puede ayudarnos a entender la probabilidad de eventos basados en información previa.\n")

# Explicación: Probabilidad a Priori
# La probabilidad a priori representa nuestro conocimiento previo sobre un evento antes de observar datos adicionales.
# Este conocimiento se usa como base para calcular la probabilidad de otros eventos que dependen del evento original.

# Ejemplo: Probabilidad a Priori en Diagnóstico Médico
# Supongamos que tenemos una prueba para detectar una enfermedad. Sabemos lo siguiente:
# 1. La probabilidad a priori (probabilidad inicial) de que una persona tenga la enfermedad es del 1%.
# 2. La prueba tiene una tasa de verdaderos positivos (sensibilidad) del 99%: detecta la enfermedad en el 99% de los casos cuando está presente.
# 3. La prueba tiene una tasa de falsos positivos del 5%: da positivo en el 5% de los casos cuando la enfermedad no está presente.

# Definimos estas probabilidades
probabilidad_enfermedad = 0.01           # Probabilidad a priori de tener la enfermedad (1%)
sensibilidad = 0.99                      # Probabilidad de que la prueba detecte la enfermedad si la persona está enferma
falso_positivo = 0.05                    # Probabilidad de que la prueba dé positivo si la persona NO está enferma

# Función para calcular la probabilidad de tener la enfermedad si la prueba da positivo
# Utilizaremos el Teorema de Bayes para calcular esto
def probabilidad_posterior():
    # Probabilidad de obtener un resultado positivo de la prueba
    # P(Prueba Positiva) = P(Prueba Positiva | Enfermedad) * P(Enfermedad) + P(Prueba Positiva | No Enfermedad) * P(No Enfermedad)
    prob_positivo = (sensibilidad * probabilidad_enfermedad) + (falso_positivo * (1 - probabilidad_enfermedad))

    # Probabilidad de tener la enfermedad si la prueba es positiva (Usando el Teorema de Bayes)
    # P(Enfermedad | Prueba Positiva) = [P(Prueba Positiva | Enfermedad) * P(Enfermedad)] / P(Prueba Positiva)
    probabilidad_enfermedad_dado_positivo = (sensibilidad * probabilidad_enfermedad) / prob_positivo

    return probabilidad_enfermedad_dado_positivo

# Cálculo y salida de la probabilidad posterior
prob_enfermedad_dado_positivo = probabilidad_posterior()
print("Ejemplo: Diagnóstico médico con probabilidad a priori")
print(f"Probabilidad de tener la enfermedad dado un resultado positivo en la prueba: {prob_enfermedad_dado_positivo:.4f}")

# Observación:
# Aunque la prueba es muy sensible, la probabilidad de realmente tener la enfermedad, dado que el resultado es positivo, es menor a 1.
# Esto se debe a la probabilidad a priori de la enfermedad y a los falsos positivos.

# Conclusión
print("\nConclusión:")
print("La probabilidad a priori nos ayuda a calcular la probabilidad de un evento teniendo en cuenta el conocimiento previo.")
print("En este ejemplo, utilizamos la probabilidad a priori de que una persona tenga una enfermedad para calcular la probabilidad posterior de tener la enfermedad, dado un resultado positivo en la prueba.")
print("Este enfoque es muy útil en situaciones donde la información previa afecta nuestras expectativas sobre los resultados.\n")
