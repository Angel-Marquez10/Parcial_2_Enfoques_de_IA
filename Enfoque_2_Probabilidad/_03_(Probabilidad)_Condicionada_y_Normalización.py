# Título: Probabilidad Condicionada y Normalización en Python
# Este código demuestra cómo calcular probabilidades condicionadas y normalizarlas
# para obtener una distribución completa con un total de 1.

# Introducción
print("Bienvenido a la práctica de Probabilidad Condicionada y Normalización")
print("En esta práctica, exploraremos cómo calcular la probabilidad condicionada de un evento y normalizar los resultados.\n")

# Información de las zonas y probabilidades
# Distribución de pedidos por zona (probabilidad a priori)
probabilidad_zona_A = 0.4  # 40% de los pedidos son de la Zona A
probabilidad_zona_B = 0.35 # 35% de los pedidos son de la Zona B
probabilidad_zona_C = 0.25 # 25% de los pedidos son de la Zona C

# Probabilidad de que un pedido en cada zona sea recurrente
probabilidad_recurrente_dado_zona_A = 0.7  # 70% de los pedidos de la Zona A son recurrentes
probabilidad_recurrente_dado_zona_B = 0.5  # 50% de los pedidos de la Zona B son recurrentes
probabilidad_recurrente_dado_zona_C = 0.2  # 20% de los pedidos de la Zona C son recurrentes

# Paso 1: Calcular la probabilidad de que un pedido sea recurrente para cada zona
# Utilizando probabilidad condicionada: P(Recurrente y Zona) = P(Recurrente | Zona) * P(Zona)
probabilidad_recurrente_A = probabilidad_recurrente_dado_zona_A * probabilidad_zona_A
probabilidad_recurrente_B = probabilidad_recurrente_dado_zona_B * probabilidad_zona_B
probabilidad_recurrente_C = probabilidad_recurrente_dado_zona_C * probabilidad_zona_C

# Imprimimos las probabilidades antes de la normalización
print("Probabilidades antes de la normalización:")
print(f"Probabilidad de pedido recurrente en Zona A: {probabilidad_recurrente_A:.4f}")
print(f"Probabilidad de pedido recurrente en Zona B: {probabilidad_recurrente_B:.4f}")
print(f"Probabilidad de pedido recurrente en Zona C: {probabilidad_recurrente_C:.4f}")

# Paso 2: Normalizar las probabilidades
# Calculamos la suma total de las probabilidades condicionadas
total_probabilidades = probabilidad_recurrente_A + probabilidad_recurrente_B + probabilidad_recurrente_C

# Ahora, normalizamos cada probabilidad condicionada dividiéndola por la suma total
# Esto asegurará que todas las probabilidades sumen 1
probabilidad_normalizada_A = probabilidad_recurrente_A / total_probabilidades
probabilidad_normalizada_B = probabilidad_recurrente_B / total_probabilidades
probabilidad_normalizada_C = probabilidad_recurrente_C / total_probabilidades

# Imprimimos las probabilidades normalizadas
print("\nProbabilidades después de la normalización:")
print(f"Probabilidad normalizada de pedido recurrente en Zona A: {probabilidad_normalizada_A:.4f}")
print(f"Probabilidad normalizada de pedido recurrente en Zona B: {probabilidad_normalizada_B:.4f}")
print(f"Probabilidad normalizada de pedido recurrente en Zona C: {probabilidad_normalizada_C:.4f}")

# Validación: La suma de las probabilidades normalizadas debe ser 1
suma_normalizada = probabilidad_normalizada_A + probabilidad_normalizada_B + probabilidad_normalizada_C
print(f"\nSuma de las probabilidades normalizadas: {suma_normalizada:.4f}")

# Conclusión
print("\nConclusión:")
print("Este ejercicio demuestra cómo calcular la probabilidad condicionada de un evento para diferentes escenarios,")
print("y luego usar la normalización para asegurar que el total de probabilidades condicionales suma 1.")
print("Esto es importante en aplicaciones como el análisis de datos probabilísticos y la inferencia estadística.\n")
