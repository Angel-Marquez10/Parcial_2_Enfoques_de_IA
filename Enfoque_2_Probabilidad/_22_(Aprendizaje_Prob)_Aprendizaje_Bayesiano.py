
# Definición de las probabilidades iniciales
prob_hipotesis = 0.5             # P(H) - Probabilidad inicial de la hipótesis
prob_evidencia_dado_hipotesis = 0.7  # P(E|H) - Probabilidad de observar la evidencia si la hipótesis es cierta
prob_evidencia_dado_no_hipotesis = 0.3  # P(E|¬H) - Probabilidad de observar la evidencia si la hipótesis es falsa

# Actualización Bayesiana de la probabilidad de la hipótesis dado la evidencia observada
def actualizacion_bayesiana(prob_hipotesis, prob_evidencia_dado_hipotesis, prob_evidencia_dado_no_hipotesis):
    prob_no_hipotesis = 1 - prob_hipotesis
    prob_evidencia = prob_evidencia_dado_hipotesis * prob_hipotesis + prob_evidencia_dado_no_hipotesis * prob_no_hipotesis
    prob_hipotesis_dado_evidencia = (prob_evidencia_dado_hipotesis * prob_hipotesis) / prob_evidencia
    return prob_hipotesis_dado_evidencia

# Ejemplo de uso
probabilidad_actualizada = actualizacion_bayesiana(prob_hipotesis, prob_evidencia_dado_hipotesis, prob_evidencia_dado_no_hipotesis)
print("Probabilidad de la hipótesis dado la evidencia:", probabilidad_actualizada)
