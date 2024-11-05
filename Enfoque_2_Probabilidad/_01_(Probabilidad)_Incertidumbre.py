# Título: Introducción a la Probabilidad e Incertidumbre en Python
# Esta práctica está diseñada para comprender el concepto de incertidumbre en eventos probabilísticos básicos.
# Utilizaremos ejemplos de probabilidad simple y eventos inciertos.

import random

# Introducción
print("Bienvenido a la práctica de Probabilidad e Incertidumbre")
print("Esta práctica demostrará cómo la probabilidad puede ayudarnos a entender la incertidumbre en situaciones cotidianas.\n")

# Explicación: Incertidumbre y eventos probables
# Cuando hablamos de incertidumbre en probabilidad, nos referimos a la falta de certeza sobre el resultado de un evento.
# Un evento es incierto cuando no podemos predecir con seguridad qué sucederá, aunque podamos estimar la probabilidad de varios resultados.

# Ejemplo 1: Lanzamiento de una moneda
# Una moneda tiene dos lados: cara y cruz.
# La probabilidad de obtener cualquiera de los dos lados en un lanzamiento es de 50%, pero el resultado de cada lanzamiento es incierto.

def lanzar_moneda():
    resultado = random.choice(["cara", "cruz"])
    return resultado

print("Ejemplo 1: Lanzamiento de una moneda")
for i in range(5):
    print(f"Lanzamiento {i+1}: Resultado - {lanzar_moneda()}")

# Observación: Aunque sabemos que hay un 50% de probabilidad para cada lado,
# el resultado es incierto y puede variar en cada lanzamiento.

# Ejemplo 2: Lanzamiento de un dado
# Un dado tiene 6 caras, con una probabilidad de 1/6 (o aproximadamente 16.67%) para cada cara.
# Sin embargo, cada lanzamiento tiene un resultado incierto.

def lanzar_dado():
    resultado = random.randint(1, 6)
    return resultado

print("\nEjemplo 2: Lanzamiento de un dado")
for i in range(5):
    print(f"Lanzamiento {i+1}: Resultado - {lanzar_dado()}")

# Observación: Aunque conocemos la probabilidad de obtener cada número en el dado,
# no podemos predecir con certeza qué número aparecerá en cada lanzamiento.

# Ejemplo 3: Probabilidad de un evento
# Ahora exploraremos cómo podemos calcular la probabilidad de un evento basado en un conjunto de resultados.
# Lanzaremos una moneda varias veces y calcularemos la probabilidad de obtener cara.

def calcular_probabilidad_caras(lanzamientos):
    # Contador de ocurrencias de 'cara'
    caras = 0
    for _ in range(lanzamientos):
        if lanzar_moneda() == "cara":
            caras += 1
    # Cálculo de la probabilidad
    probabilidad = caras / lanzamientos
    return probabilidad

# Realizamos 100 lanzamientos para obtener una estimación de la probabilidad
lanzamientos = 100
probabilidad_estimada = calcular_probabilidad_caras(lanzamientos)
print(f"\nEjemplo 3: Probabilidad estimada de obtener cara en {lanzamientos} lanzamientos: {probabilidad_estimada:.2f}")

# Observación final: Aunque esperamos que la probabilidad esté cerca de 0.5,
# el resultado de cada lanzamiento es incierto y varía cada vez que realizamos los lanzamientos.

# Conclusión
print("\nConclusión:")
print("La incertidumbre en probabilidad se refiere a la falta de certeza en el resultado de eventos individuales.")
print("Aunque conocemos las probabilidades, el resultado de cada intento o evento sigue siendo incierto.\n")
print("Esta práctica muestra cómo podemos usar simulaciones en Python para explorar conceptos de probabilidad e incertidumbre.")
