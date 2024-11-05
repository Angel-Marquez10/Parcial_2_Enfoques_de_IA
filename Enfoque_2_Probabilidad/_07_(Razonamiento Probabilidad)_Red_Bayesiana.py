# Título: Red Bayesiana
# Este código implementa una red bayesiana simple sin el uso de librerías.

# Definición de probabilidades
# Probabilidades a priori
P_gripe = 0.1  # Probabilidad de tener gripe
P_no_gripe = 1 - P_gripe  # Probabilidad de no tener gripe

# Probabilidades condicionales
# P(Fiebre | Gripe)
P_fiebre_dado_gripe = 0.8  # Probabilidad de fiebre dado que hay gripe
P_fiebre_dado_no_gripe = 0.1  # Probabilidad de fiebre dado que no hay gripe

# P(Tos | Gripe)
P_tos_dado_gripe = 0.7  # Probabilidad de tos dado que hay gripe
P_tos_dado_no_gripe = 0.2  # Probabilidad de tos dado que no hay gripe

# Función para calcular la probabilidad de tener fiebre
def probabilidad_fiebre(tiene_gripe):
    if tiene_gripe:
        return P_fiebre_dado_gripe
    else:
        return P_fiebre_dado_no_gripe

# Función para calcular la probabilidad de tener tos
def probabilidad_tos(tiene_gripe):
    if tiene_gripe:
        return P_tos_dado_gripe
    else:
        return P_tos_dado_no_gripe

# Función para calcular la probabilidad conjunta
def probabilidad_conjunta(tiene_gripe):
    prob_fiebre = probabilidad_fiebre(tiene_gripe)
    prob_tos = probabilidad_tos(tiene_gripe)
    return prob_fiebre * prob_tos

# Calculo de probabilidades
# Probabilidad de tener fiebre y tos
P_fiebre_tos_con_gripe = probabilidad_conjunta(True) * P_gripe
P_fiebre_tos_sin_gripe = probabilidad_conjunta(False) * P_no_gripe

# Probabilidad total
P_total = P_fiebre_tos_con_gripe + P_fiebre_tos_sin_gripe

# Probabilidades condicionales finales
P_fiebre_y_tos_dado_gripe = P_fiebre_tos_con_gripe / P_total
P_fiebre_y_tos_dado_no_gripe = P_fiebre_tos_sin_gripe / P_total

# Resultados
print("Probabilidades condicionales:")
print(f"P(Fiebre y Tos | Gripe): {P_fiebre_y_tos_dado_gripe:.4f}")
print(f"P(Fiebre y Tos | No Gripe): {P_fiebre_y_tos_dado_no_gripe:.4f}")

# Conclusión
print("\nConclusión:")
print("Este código ha implementado una red bayesiana simple para calcular la probabilidad de fiebre y tos en función de la presencia de gripe.")
