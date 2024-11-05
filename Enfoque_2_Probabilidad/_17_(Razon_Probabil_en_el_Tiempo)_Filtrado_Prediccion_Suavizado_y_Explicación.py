import random  # Importar la biblioteca random para generar ruido gaussiano

# Título: Filtro de Kalman Simplificado
# Este código simula un filtro de Kalman para estimar la posición de un objeto en movimiento.

# Parámetros del sistema
dt = 1.0  # Intervalo de tiempo entre mediciones (1 segundo)
num_steps = 20  # Número total de pasos a simular
true_position = 0.0  # Posición real inicial del objeto
velocity = 1.0  # Velocidad del objeto (1 unidad por segundo)
measurements = []  # Lista para almacenar mediciones ruidosas
estimates = []  # Lista para almacenar las estimaciones del filtro

# Inicialización del estado del filtro
estimated_position = 0.0  # Posición estimada inicial
estimated_velocity = 0.0  # Velocidad estimada inicial
process_variance = 1.0  # Varianza del proceso (incertidumbre en la dinámica)
measurement_variance = 2.0  # Varianza de la medición (incertidumbre en las mediciones)

# Simulación del movimiento del objeto y las mediciones
for step in range(num_steps):
    # Actualizar la posición real del objeto
    true_position += velocity * dt
    
    # Generar una medición ruidosa (ruido gaussiano)
    noise = random.gauss(0, measurement_variance ** 0.5)  # Ruido
    measurement = true_position + noise  # Mediciones ruidosas
    measurements.append(measurement)

    # Predicción del siguiente estado (sin control)
    predicted_position = estimated_position + estimated_velocity * dt
    predicted_velocity = estimated_velocity  # Se asume que la velocidad es constante

    # Actualización del filtro de Kalman
    # Calcular el error de predicción
    estimation_error = predicted_position - estimated_position
    
    # Calcular la ganancia de Kalman
    kalman_gain = process_variance / (process_variance + measurement_variance)
    
    # Actualizar la estimación
    estimated_position += kalman_gain * (measurement - predicted_position)
    estimated_velocity = predicted_velocity  # Actualización simple

    # Actualizar la varianza del proceso
    process_variance = (1 - kalman_gain) * process_variance

    # Almacenar la estimación
    estimates.append(estimated_position)

# Mostrar resultados finales
print("Resultados de la Simulación:")
print("Pasos de la Simulación:")
for i in range(num_steps):
    print(f"Paso {i + 1}: Mediciones = {measurements[i]:.2f}, Estimación = {estimates[i]:.2f}, Verdadera Posición = {true_position:.2f}")
