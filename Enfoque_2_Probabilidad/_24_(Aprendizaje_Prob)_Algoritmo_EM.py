
import numpy as np

# Generación de datos simulados con dos distribuciones normales
np.random.seed(0)
datos = np.hstack((np.random.normal(5, 1, 100), np.random.normal(15, 2, 100)))

# Inicialización de parámetros para las dos distribuciones
mu1, mu2 = 4, 14
sigma1, sigma2 = 1, 2
pi1, pi2 = 0.5, 0.5

# Función de densidad gaussiana
def gaussiana(x, mu, sigma):
    return (1 / (np.sqrt(2 * np.pi) * sigma)) * np.exp(-0.5 * ((x - mu) / sigma) ** 2)

# Algoritmo EM
def algoritmo_em(datos, iteraciones=10):
    global mu1, mu2, sigma1, sigma2, pi1, pi2
    for _ in range(iteraciones):
        # Paso E: calcular responsabilidades
        gamma1 = pi1 * gaussiana(datos, mu1, sigma1)
        gamma2 = pi2 * gaussiana(datos, mu2, sigma2)
        suma_gamma = gamma1 + gamma2
        gamma1 /= suma_gamma
        gamma2 /= suma_gamma
        
        # Paso M: actualizar parámetros
        mu1 = np.sum(gamma1 * datos) / np.sum(gamma1)
        mu2 = np.sum(gamma2 * datos) / np.sum(gamma2)
        sigma1 = np.sqrt(np.sum(gamma1 * (datos - mu1) ** 2) / np.sum(gamma1))
        sigma2 = np.sqrt(np.sum(gamma2 * (datos - mu2) ** 2) / np.sum(gamma2))
        pi1 = np.mean(gamma1)
        pi2 = np.mean(gamma2)

    return mu1, mu2, sigma1, sigma2, pi1, pi2

# Ejemplo de uso
parametros = algoritmo_em(datos)
print("Parámetros estimados:", parametros)
