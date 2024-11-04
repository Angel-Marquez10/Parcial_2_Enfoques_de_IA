import numpy as np

class POMDP:
    def __init__(self, states, actions, observations, transition_probabilities, observation_probabilities, rewards, discount_factor=0.9):
        """
        Inicializa el POMDP.

        :param states: Lista de estados posibles.
        :param actions: Lista de acciones posibles.
        :param observations: Lista de observaciones posibles.
        :param transition_probabilities: Diccionario de probabilidades de transición.
        :param observation_probabilities: Diccionario de probabilidades de observación.
        :param rewards: Diccionario de recompensas.
        :param discount_factor: Factor de descuento para futuros beneficios.
        """
        self.states = states  # Estados del POMDP
        self.actions = actions  # Acciones disponibles
        self.observations = observations  # Observaciones posibles
        self.transition_probabilities = transition_probabilities  # Probabilidades de transición
        self.observation_probabilities = observation_probabilities  # Probabilidades de observación
        self.rewards = rewards  # Recompensas por estado
        self.discount_factor = discount_factor  # Factor de descuento

    def belief_update(self, belief, action, observation):
        """
        Actualiza la creencia sobre el estado actual dado un acción y una observación.

        :param belief: Distribución de creencias sobre los estados.
        :param action: Acción tomada.
        :param observation: Observación recibida.
        :return: Nueva distribución de creencias actualizada.
        """
        # Actualizar creencias con la acción y la observación
        new_belief = {state: 0 for state in self.states}  # Nueva creencia inicializada a cero
        
        # Calcular la nueva creencia
        for next_state in self.states:
            # Obtener la probabilidad de transición al siguiente estado
            transition_prob = self.transition_probabilities[next_state][action]
            # Obtener la probabilidad de observar la observación dada el siguiente estado
            observation_prob = self.observation_probabilities[next_state][observation]
            
            # Sumar las contribuciones a la nueva creencia
            for prev_state in self.states:
                new_belief[next_state] += belief[prev_state] * transition_prob * observation_prob
        
        # Normalizar la nueva creencia
        total = sum(new_belief.values())
        for state in self.states:
            new_belief[state] /= total if total > 0 else 1  # Evitar división por cero
            
        return new_belief

    def value_iteration(self, belief, epsilon=0.01):
        """
        Realiza la iteración de valores para calcular el valor óptimo dado una creencia.

        :param belief: Distribución de creencias sobre los estados.
        :param epsilon: Umbral de convergencia.
        :return: Un diccionario con el valor de cada acción.
        """
        values = {action: 0 for action in self.actions}  # Inicializamos los valores de las acciones a cero

        while True:
            new_values = values.copy()  # Copia de los valores para comparar después
            delta = 0  # Para medir el cambio en los valores
            
            for action in self.actions:
                expected_value = 0  # Valor esperado para esta acción
                
                # Calcular el valor esperado para esta acción
                for next_state in self.states:
                    reward = self.rewards.get(next_state, 0)  # Obtener recompensa para el estado
                    prob = self.transition_probabilities[next_state][action]  # Obtener probabilidad de transición
                    
                    expected_value += belief[next_state] * (reward + self.discount_factor * prob)

                # Actualizar el nuevo valor de la acción
                new_values[action] = expected_value

                # Medimos la diferencia para verificar la convergencia
                delta = max(delta, abs(new_values[action] - values[action]))

            values = new_values  # Actualizamos los valores
            
            # Si la diferencia es menor que el umbral, hemos convergido
            if delta < epsilon:
                break
        
        return values

# Definimos los estados, acciones y observaciones
states = ['s1', 's2', 's3']
actions = ['a1', 'a2']
observations = ['o1', 'o2']

# Definimos las probabilidades de transición
transition_probabilities = {
    's1': {'a1': 0.7, 'a2': 0.3},
    's2': {'a1': 0.4, 'a2': 0.6},
    's3': {'a1': 0.1, 'a2': 0.9}
}

# Definimos las probabilidades de observación
observation_probabilities = {
    's1': {'o1': 0.9, 'o2': 0.1},
    's2': {'o1': 0.5, 'o2': 0.5},
    's3': {'o1': 0.2, 'o2': 0.8}
}

# Definimos las recompensas para los estados
rewards = {
    's1': 10,
    's2': 5,
    's3': 0
}

# Creamos una instancia del POMDP
pomdp = POMDP(states, actions, observations, transition_probabilities, observation_probabilities, rewards)

# Inicializamos una creencia uniforme sobre los estados
initial_belief = {state: 1/len(states) for state in states}

# Actualizamos la creencia con una acción y una observación
action_taken = 'a1'
observation_received = 'o1'
updated_belief = pomdp.belief_update(initial_belief, action_taken, observation_received)

# Ejecutamos la iteración de valores con la creencia actualizada
optimal_values = pomdp.value_iteration(updated_belief)

# Imprimimos los valores óptimos de cada acción
print("Valores óptimos de cada acción:")
for action, value in optimal_values.items():
    print(f"Acción {action}: Valor óptimo = {value:.2f}")
