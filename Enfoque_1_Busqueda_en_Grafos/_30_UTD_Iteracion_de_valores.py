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

    def value_iteration(self, epsilon=0.01):
        """
        Realiza la iteración de valores para calcular el valor óptimo de cada estado.

        :param epsilon: Umbral de convergencia.
        :return: Un diccionario con el valor óptimo para cada estado.
        """
        # Inicializamos los valores de los estados a cero
        values = {state: 0 for state in self.states}
        
        while True:
            # Creamos una copia de los valores para comparar después
            new_values = values.copy()
            delta = 0  # Para medir el cambio en los valores
            
            # Iteramos sobre todos los estados
            for state in self.states:
                # Calculamos el valor máximo para cada acción posible
                max_value = float('-inf')
                
                for action in self.actions:
                    expected_value = 0  # Valor esperado para esta acción
                    
                    # Calculamos el valor esperado basándonos en las probabilidades de transición
                    for next_state in self.states:
                        # Probabilidad de ir al siguiente estado
                        prob = self.transition_probabilities[state][action].get(next_state, 0)
                        # Recompensa por llegar a ese estado
                        reward = self.rewards.get(next_state, 0)
                        expected_value += prob * (reward + self.discount_factor * values[next_state])
                    
                    # Guardamos el valor máximo encontrado
                    max_value = max(max_value, expected_value)

                # Actualizamos el nuevo valor del estado
                new_values[state] = max_value
            
            # Medimos la diferencia para verificar la convergencia
            for state in self.states:
                delta = max(delta, abs(new_values[state] - values[state]))
            
            # Actualizamos los valores
            values = new_values
            
            # Si la diferencia es menor que el umbral, hemos convergido
            if delta < epsilon:
                break
        
        return values

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

# Imprimimos los valores óptimos
print("Valores óptimos de cada estado:")
for state, value in optimal_values.items():
    print(f"Estado {state}: Valor óptimo = {value:.2f}")
