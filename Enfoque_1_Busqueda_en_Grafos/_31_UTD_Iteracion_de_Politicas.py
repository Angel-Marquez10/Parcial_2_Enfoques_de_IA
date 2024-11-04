import numpy as np

# Definimos la clase para nuestro MDP
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

    def policy_evaluation(self, policy, epsilon=0.01):
        """
        Evalúa una política dada.

        :param policy: Diccionario que asigna acciones a estados.
        :param epsilon: Umbral de convergencia.
        :return: Un diccionario con el valor de cada estado.
        """
        values = {state: 0 for state in self.states}  # Inicializamos los valores a cero

        while True:
            new_values = values.copy()  # Copia de los valores para comparar después
            delta = 0  # Para medir el cambio en los valores
            
            for state in self.states:
                action = policy[state]  # Acción tomada según la política actual
                expected_value = 0  # Valor esperado para esta acción
                
                # Calculamos el valor esperado basándonos en las probabilidades de transición
                for next_state in self.states:
                    prob = self.transition_probabilities[state][action].get(next_state, 0)
                    reward = self.rewards.get(next_state, 0)
                    expected_value += prob * (reward + self.discount_factor * values[next_state])
                
                # Actualizamos el nuevo valor del estado
                new_values[state] = expected_value

                # Medimos la diferencia para verificar la convergencia
                delta = max(delta, abs(new_values[state] - values[state]))

            values = new_values  # Actualizamos los valores
            
            # Si la diferencia es menor que el umbral, hemos convergido
            if delta < epsilon:
                break
        
        return values

    def policy_improvement(self, values):
        """
        Mejora la política basada en los valores dados.

        :param values: Valores de cada estado.
        :return: Nueva política.
        """
        policy = {state: None for state in self.states}  # Inicializamos la política

        for state in self.states:
            max_value = float('-inf')  # Valor máximo inicial
            best_action = None  # Acción que maximiza el valor

            # Probar cada acción
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

    def iterate_policy(self, initial_policy, epsilon=0.01):
        """
        Realiza la iteración de políticas para encontrar la política óptima.

        :param initial_policy: Política inicial.
        :param epsilon: Umbral de convergencia.
        :return: La política óptima y los valores correspondientes.
        """
        policy = initial_policy
        
        while True:
            # Evaluamos la política actual
            values = self.policy_evaluation(policy, epsilon)
            # Mejoramos la política
            new_policy = self.policy_improvement(values)

            # Si la política no ha cambiado, hemos convergido
            if new_policy == policy:
                break

            policy = new_policy  # Actualizamos la política

        return policy, values

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

# Definimos una política inicial (puede ser aleatoria o fija)
initial_policy = {
    's1': 'a1',
    's2': 'a2',
    's3': 'a1'
}

# Creamos una instancia del MDP
mdp = MarkovDecisionProcess(states, actions, transition_probabilities, rewards)

# Ejecutamos la iteración de políticas
optimal_policy, optimal_values = mdp.iterate_policy(initial_policy)

# Imprimimos la política óptima y los valores
print("Política óptima:")
for state, action in optimal_policy.items():
    print(f"Estado {state}: Acción óptima = {action}")

print("\nValores óptimos de cada estado:")
for state, value in optimal_values.items():
    print(f"Estado {state}: Valor óptimo = {value:.2f}")
