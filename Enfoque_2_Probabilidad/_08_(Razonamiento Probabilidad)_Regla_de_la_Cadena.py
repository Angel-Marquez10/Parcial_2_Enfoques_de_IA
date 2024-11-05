# Título: Cálculo de Probabilidades usando la Regla de la Cadena
# Este código implementa la regla de la cadena para calcular la probabilidad conjunta de eventos relacionados con un viaje en avión.

# Introducción
print("Bienvenido a la práctica de la Regla de la Cadena")
print("Este ejercicio calcula la probabilidad conjunta de que un avión y un pasajero lleguen a tiempo.\n")

# Paso 1: Definir las probabilidades
# Definimos las probabilidades de los eventos
P_A = 0.9  # Probabilidad de que el avión salga a tiempo (90%)
P_B_given_A = 0.95  # Probabilidad de que el avión llegue a tiempo dado que salió a tiempo (95%)
P_C_given_B = 0.85  # Probabilidad de que el pasajero llegue a la puerta a tiempo dado que el avión llegó a tiempo (85%)

# Paso 2: Calcular la probabilidad conjunta usando la Regla de la Cadena
P_A_and_B_and_C = P_A * P_B_given_A * P_C_given_B

# Paso 3: Mostrar el resultado
print(f"La probabilidad conjunta de que el avión salga a tiempo, llegue a tiempo y que el pasajero llegue a la puerta a tiempo es: {P_A_and_B_and_C:.4f}")

# Conclusión
print("\nConclusión:")
print("Hemos utilizado la regla de la cadena para calcular la probabilidad conjunta de múltiples eventos.")
print("Este enfoque es útil en situaciones donde los eventos son dependientes entre sí.")
