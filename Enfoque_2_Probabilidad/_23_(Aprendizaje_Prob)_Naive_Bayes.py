
from collections import Counter
import numpy as np

# Datos de ejemplo (Características: 'sol', 'lluvia'; Clases: 'playa', 'montaña')
datos = [
    (['sol', 'calor'], 'playa'),
    (['lluvia', 'frío'], 'montaña'),
    (['sol', 'frío'], 'montaña'),
    (['sol', 'calor'], 'playa'),
    (['lluvia', 'calor'], 'playa')
]

# Cálculo de probabilidades para cada clase y característica
def entrenamiento_naive_bayes(datos):
    clases = Counter([clase for _, clase in datos])
    total = sum(clases.values())
    prob_clases = {clase: cuenta / total for clase, cuenta in clases.items()}
    
    prob_caracteristicas_dado_clase = {clase: Counter() for clase in clases}
    for caracteristicas, clase in datos:
        prob_caracteristicas_dado_clase[clase].update(caracteristicas)
    
    for clase, caracteristicas in prob_caracteristicas_dado_clase.items():
        total_clase = sum(caracteristicas.values())
        for caracteristica in caracteristicas:
            prob_caracteristicas_dado_clase[clase][caracteristica] /= total_clase
            
    return prob_clases, prob_caracteristicas_dado_clase

# Clasificación de una nueva instancia
def clasificar_naive_bayes(instancia, prob_clases, prob_caracteristicas_dado_clase):
    puntajes = {}
    for clase, prob_clase in prob_clases.items():
        puntajes[clase] = prob_clase * np.prod([prob_caracteristicas_dado_clase[clase].get(caracteristica, 0.01) for caracteristica in instancia])
    return max(puntajes, key=puntajes.get)

# Ejemplo de uso
prob_clases, prob_caracteristicas_dado_clase = entrenamiento_naive_bayes(datos)
nueva_instancia = ['sol', 'calor']
clasificacion = clasificar_naive_bayes(nueva_instancia, prob_clases, prob_caracteristicas_dado_clase)
print(f"Clasificación de la instancia {nueva_instancia}:", clasificacion)
