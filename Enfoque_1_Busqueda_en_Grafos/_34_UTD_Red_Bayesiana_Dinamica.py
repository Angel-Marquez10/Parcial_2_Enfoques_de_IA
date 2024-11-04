import numpy as np

class DynamicBayesianNetwork:
    def __init__(self, states, evidence, transition_probabilities, emission_probabilities):
        """
        Inicializa la Red Bayesiana Dinámica.

        :param states: Lista de estados posibles.
        :param evidence: Lista de variables de evidencia.
        :param transition_probabilities: Probabilidades de transición entre estados.
        :param emission_probabilities: Probabilidades de emisión de las observaciones.
        """
        self.states = states  # Estados de la red
        self.evidence = evidence  # Variables de evidencia
        self.transition_probabilities = transition_probabilities  # Probabilidades de transición
        self.emission_probabilities = emission_probabilities  # Probabilidades de emisión

    def get_transition_probability(self, current_state, next_state):
        """
        Obtiene la probabilidad de transición de un estado a otro.

        :param current_state: Estado actual.
        :param next_state: Estado siguiente.
        :return: Probabilidad de transición.
        """
        return self.transition_probabilities[current_state][next_state]

    def get_emission_probability(self, state, observation):
        """
        Obtiene la probabilidad de emisión de una observación dada un estado.

        :param state: Estado.
        :param observation: Observación.
        :return: Probabilidad de emisión.
        """
        return self.emission_probabilities[state][observation]

    def predict_next_state(self, current_state):
        """
        Predice el siguiente estado dado el estado actual utilizando probabilidades de transición.

        :param current_state: Estado actual.
        :return: Estado siguiente predicho y su probabilidad.
        """
        next_state_probabilities = {}
        for next_state in self.states:
            prob = self.get_transition_probability(current_state, next_state)
            next_state_probabilities[next_state] = prob
        return next_state_probabilities

    def generate_observation(self, current_state):
        """
        Genera una observación basada en el estado actual utilizando probabilidades de emisión.

        :param current_state: Estado actual.
        :return: Observación generada.
        """
        observation_probabilities = self.emission_probabilities[current_state]
        observations = list(observation_probabilities.keys())
        probabilities = list(observation_probabilities.values())
        return np.random.choice(observations, p=probabilities)

# Definición de los estados y las evidencias
states = ['Sunny', 'Rainy']
evidence = ['Sensor']

# Definición de las probabilidades de transición entre estados
transition_probabilities = {
    'Sunny': {'Sunny': 0.8, 'Rainy': 0.2},
    'Rainy': {'Sunny': 0.4, 'Rainy': 0.6}
}

# Definición de las probabilidades de emisión
emission_probabilities = {
    'Sunny': {'High': 0.9, 'Low': 0.1},
    'Rainy': {'High': 0.3, 'Low': 0.7}
}

# Creación de una instancia de la Red Bayesiana Dinámica
dbn = DynamicBayesianNetwork(states, evidence, transition_probabilities, emission_probabilities)

# Predicción del siguiente estado dado un estado actual
current_state = 'Sunny'
predicted_states = dbn.predict_next_state(current_state)
print("Probabilidades del siguiente estado dado el estado actual (Sunny):")
for state, prob in predicted_states.items():
    print(f"Estado: {state}, Probabilidad: {prob:.2f}")

# Generación de una observación basada en el estado actual
observation = dbn.generate_observation(current_state)
print(f"Observación generada dado el estado actual ({current_state}): {observation}")
