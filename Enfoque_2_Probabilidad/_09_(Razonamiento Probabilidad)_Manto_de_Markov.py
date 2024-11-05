import numpy as np

# Título: Simulación de un Manto de Markov para el Clima
# Este código simula el clima en un sistema con tres estados usando una cadena de Markov.

# Introducción
print("Bienvenido a la práctica del Manto de Markov")
print("Este ejercicio simula la evolución del clima en tres estados: Lluvia, Nublado y Soleado.\n")

# Definimos los estados
states = ["Lluvia", "Nublado", "Soleado"]

# Definimos la matriz de transición
# Cada fila representa el estado actual y cada columna representa el estado al que se puede transitar
transition_matrix = np.array([
    [0.5, 0.5, 0.0],  # Desde Lluvia
    [0.3, 0.4, 0.3],  # Desde Nublado
    [0.1, 0.2, 0.7]   # Desde Soleado
])

# Función para simular el clima
def simulate_weather(initial_state, days):
    # Establecer el estado inicial
    current_state = initial_state
    weather_sequence = [states[current_state]]  # Guardamos la secuencia de estados

    for day in range(days):
        # Elegimos el siguiente estado basado en la matriz de transición
        current_state = np.random.choice(range(len(states)), p=transition_matrix[current_state])
        weather_sequence.append(states[current_state])

    return weather_sequence

# Paso 1: Configuración inicial
initial_state = 0  # Comenzamos con Lluvia
days = 10  # Número de días a simular

# Paso 2: Simular el clima
weather_sequence = simulate_weather(initial_state, days)

# Paso 3: Mostrar los resultados
print("Secuencia del clima durante los próximos días:")
for day, weather in enumerate(weather_sequence):
    print(f"Día {day}: {weather}")

# Conclusión
print("\nConclusión:")
print("Hemos simulado un sistema de clima utilizando una cadena de Markov.")
print("La probabilidad de cada estado solo depende del estado actual, no de los anteriores.")
