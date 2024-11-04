import numpy as np

class SimpleEnvironment:
    def __init__(self, num_states=5, terminal_state=4, reward=1):
        """
        Inicializa el entorno del agente.

        :param num_states: Número total de estados en el entorno.
        :param terminal_state: Estado terminal donde se recibe la recompensa.
        :param reward: Recompensa obtenida al llegar al estado terminal.
        """
        self.num_states = num_states
        self.terminal_state = terminal_state
        self.reward = reward
        self.state_values = np.zeros(num_states)  # Inicializa los valores de estado en cero
        self.gamma = 0.9  # Factor de descuento

    def step(self, state):
        """
        Realiza un paso en el entorno y devuelve la recompensa.

        :param state: Estado actual del agente.
        :return: Recompensa recibida y el siguiente estado.
        """
        if state == self.terminal_state:
            return self.reward, state  # Recompensa y estado terminal
        else:
            return 0, state + 1  # Avanza al siguiente estado

    def value_iteration(self, threshold=0.01):
        """
        Realiza la iteración de valores hasta que la convergencia sea alcanzada.

        :param threshold: Umbral para determinar la convergencia.
        """
        while True:
            delta = 0  # Variable para rastrear el cambio en los valores
            for state in range(self.num_states):
                old_value = self.state_values[state]  # Guarda el valor antiguo
                if state == self.terminal_state:
                    continue  # No actualiza el valor en el estado terminal

                # Calcula el nuevo valor de estado usando el valor de los siguientes estados
                new_value = 0
                reward, next_state = self.step(state)
                new_value += reward + self.gamma * self.state_values[next_state]

                self.state_values[state] = new_value  # Actualiza el valor del estado
                delta = max(delta, abs(old_value - new_value))  # Actualiza delta

            # Verifica si los cambios son menores al umbral
            if delta < threshold:
                break  # Converge y termina la iteración

    def print_values(self):
        """Imprime los valores de estado aprendidos."""
        for i, value in enumerate(self.state_values):
            print(f"Estado {i}: Valor = {value:.2f}")

# Crear un entorno simple
environment = SimpleEnvironment()

# Ejecutar la iteración de valores
environment.value_iteration()

# Imprimir los resultados
print("Valores de estado aprendidos:")
environment.print_values()
