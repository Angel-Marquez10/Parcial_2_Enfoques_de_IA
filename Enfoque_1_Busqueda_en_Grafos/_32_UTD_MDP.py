import numpy as np

class MarkovDecisionProcess:
    def __init__(self, states, actions, transition_probabilities, rewards, discount_factor=0.9):
        """
        Inicializa el MDP.

        :param states: Lista de estados.
        :param actions: Lista de acciones.
        :param transition_probabilities: Diccionario de probabilidades de transición.
        :param rewards: Diccionario de recompensas.
        :param discount_factor: Factor de descuento para futuros beneficios.
        """
        self.states = states  # Estados del MDP
        self.actions = actions  # Acciones disponibles
        self.transition_probabilities = transition_probabilities  # Probabilidades de transición
        self.rewards = rewards  # Recompensas por estado
        self.discount_factor = discount_factor  # Factor de descuento

    def value_iteration(self, epsilon=0.01):
        """
        Realiza la iteración de valores para calcular el valor óptimo de cada estado.

        :param epsilon: Umbral de convergencia.
        :return: Un diccionario con el valor de cada estado.
        """
        values = {state: 0 for state in self.states}  # Inicializamos los valores a cero

        while True:
            new_values = values.copy()  # Copia de los valores para comparar después
            delta = 0  # Para medir el cambio en los valores
            
            for state in self.states:
                max_value = float('-inf')  # Valor máximo inicial para la acción
                
                # Probar cada acción
                for action in self.actions:
                    expected_value = 0  # Valor esperado para esta acción
                    
                    # Calculamos el valor esperado basado en las probabilidades de transición
                    for next_state in self.states:
                        prob = self.transition_probabilities[state][action].get(next_state, 0)
                        reward = self.rewards.get(next_state, 0)
                        expected_value += prob * (reward + self.discount_factor * values[next_state])
                    
                    # Actualizamos el valor máximo si encontramos uno mayor
                    max_value = max(max_value, expected_value)
                
                # Actualizamos el nuevo valor del estado
                new_values[state] = max_value

                # Medimos la diferencia para verificar la convergencia
                delta = max(delta, abs(new_values[state] - values[state]))

            values = new_values  # Actualizamos los valores
            
            # Si la diferencia es menor que el umbral, hemos convergido
            if delta < epsilon:
                break
        
        return values

    def get_optimal_policy(self, values):
        """
        Obtiene la política óptima basada en los valores calculados.

        :param values: Valores de cada estado.
        :return: Una política que asigna acciones a estados.
        """
        policy = {state: None for state in self.states}  # Inicializamos la política

        for state in self.states:
            max_value = float('-inf')  # Valor máximo inicial
            best_action = None  # Acción que maximiza el valor

            # Probar cada acción para encontrar la mejor
            for action in self.actions:
                expected_value = 0  # Valor esperado para esta acción

                # Calcular el valor esperado
                for next_state in self.states:
                    prob = self.transition_probabilities[state][action].get(next_state, 0)
                    reward = self.rewards.get(next_state, 0)
                    expected_value += prob * (reward + self.discount_factor * values[next_state])
                
                # Si encontramos un valor mayor, actualizamos la acción
                if expected_value > max_value:
                    max_value = expected_value
                    best_action = action
            
            policy[state] = best_action  # Asignamos la mejor acción a la política

        return policy

# Definimos los estados y acciones
states = ['s1', 's2', 's3']
actions = ['a1', 'a2']

# Definimos las probabilidades de transición
transition_probabilities = {
    's1': {
        'a1': {'s1': 0.8, 's2': 0.2, 's3': 0.0},
        'a2': {'s1': 0.4, 's2': 0.6, 's3': 0.0}
    },
    's2': {
        'a1': {'s1': 0.1, 's2': 0.9, 's3': 0.0},
        'a2': {'s1': 0.0, 's2': 0.7, 's3': 0.3}
    },
    's3': {
        'a1': {'s1': 0.0, 's2': 0.0, 's3': 1.0},
        'a2': {'s1': 0.0, 's2': 0.0, 's3': 1.0}
    }
}

# Definimos las recompensas para los estados
rewards = {
    's1': 5,
    's2': 10,
    's3': 0
}

# Creamos una instancia del MDP
mdp = MarkovDecisionProcess(states, actions, transition_probabilities, rewards)

# Ejecutamos la iteración de valores
optimal_values = mdp.value_iteration()

# Imprimimos los valores óptimos de cada estado
print("Valores óptimos de cada estado:")
for state, value in optimal_values.items():
    print(f"Estado {state}: Valor óptimo = {value:.2f}")

# Obtenemos la política óptima
optimal_policy = mdp.get_optimal_policy(optimal_values)

# Imprimimos la política óptima
print("\nPolítica óptima:")
for state, action in optimal_policy.items():
    print(f"Estado {state}: Acción óptima = {action}")
