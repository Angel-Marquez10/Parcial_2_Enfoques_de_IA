# Título: Ejemplo de Independencia Condicional en Python
# Este código simula un conjunto de datos para demostrar el concepto de independencia condicional
# entre dos eventos dado un tercer evento.

import random

# Introducción
print("Bienvenido a la práctica de Independencia Condicional")
print("En este ejercicio, veremos si el estado de un dispositivo y su reinicio son independientes, dado que ocurre un fallo.\n")

# Paso 1: Inicializar variables para simular los eventos
# Creamos listas para simular el estado del dispositivo, el reinicio, y el fallo del sistema
num_simulaciones = 10000  # Número de simulaciones

estado_dispositivo = []  # 1 si funciona, 0 si falla
reinicio_dispositivo = []  # 1 si se reinicia, 0 si no
fallo_sistema = []  # 1 si hay fallo en el sistema, 0 si no hay fallo

# Paso 2: Generamos datos simulados para las tres variables
for _ in range(num_simulaciones):
    # Generamos el fallo en el sistema
    fallo = random.choices([1, 0], weights=[0.3, 0.7])[0]  # 30% de probabilidad de fallo
    fallo_sistema.append(fallo)
    
    # Generamos el estado del dispositivo condicionado al fallo en el sistema
    if fallo == 1:
        estado = random.choices([1, 0], weights=[0.4, 0.6])[0]  # Más probabilidad de fallo si el sistema falla
    else:
        estado = random.choices([1, 0], weights=[0.9, 0.1])[0]  # Menos probabilidad de fallo sin fallo en el sistema
    estado_dispositivo.append(estado)
    
    # Generamos el reinicio condicionado al fallo en el sistema
    if fallo == 1:
        reinicio = random.choices([1, 0], weights=[0.7, 0.3])[0]  # Más probabilidad de reinicio si el sistema falla
    else:
        reinicio = random.choices([1, 0], weights=[0.2, 0.8])[0]  # Menos probabilidad de reinicio sin fallo en el sistema
    reinicio_dispositivo.append(reinicio)

# Paso 3: Cálculo de probabilidades
# Calculamos la probabilidad de cada evento y las probabilidades condicionales
total_fallos = sum(fallo_sistema)
prob_reinicio_dado_fallo = sum([1 for i in range(num_simulaciones) if reinicio_dispositivo[i] == 1 and fallo_sistema[i] == 1]) / total_fallos
prob_estado_dado_fallo = sum([1 for i in range(num_simulaciones) if estado_dispositivo[i] == 1 and fallo_sistema[i] == 1]) / total_fallos
prob_estado_y_reinicio_dado_fallo = sum([1 for i in range(num_simulaciones) if estado_dispositivo[i] == 1 and reinicio_dispositivo[i] == 1 and fallo_sistema[i] == 1]) / total_fallos

# Paso 4: Verificación de Independencia Condicional
# Si P(Estado y Reinicio | Fallo) ≈ P(Estado | Fallo) * P(Reinicio | Fallo), entonces Estado y Reinicio son independientes dado el fallo.
independencia_condicional = (prob_estado_y_reinicio_dado_fallo == prob_estado_dado_fallo * prob_reinicio_dado_fallo)

# Resultados
print("Probabilidades calculadas:")
print(f"P(Reinicio = 1 | Fallo = 1): {prob_reinicio_dado_fallo:.4f}")
print(f"P(Estado = 1 | Fallo = 1): {prob_estado_dado_fallo:.4f}")
print(f"P(Estado = 1 y Reinicio = 1 | Fallo = 1): {prob_estado_y_reinicio_dado_fallo:.4f}")
print(f"P(Estado = 1 | Fallo = 1) * P(Reinicio = 1 | Fallo = 1): {prob_estado_dado_fallo * prob_reinicio_dado_fallo:.4f}")

print("\nVerificación de independencia condicional:")
if independencia_condicional:
    print("Los eventos Estado y Reinicio son condicionalmente independientes dado el Fallo.")
else:
    print("Los eventos Estado y Reinicio NO son condicionalmente independientes dado el Fallo.")

# Conclusión
print("\nConclusión:")
print("Este ejercicio demuestra cómo podemos verificar la independencia condicional entre dos eventos")
print("al observar si su probabilidad conjunta dado un tercer evento es igual al producto de sus probabilidades individuales condicionadas.")
print("Este tipo de análisis es útil en modelos probabilísticos y en redes bayesianas.\n")
