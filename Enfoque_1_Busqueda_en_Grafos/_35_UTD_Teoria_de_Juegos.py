import numpy as np

class PrisonersDilemma:
    def __init__(self):
        """
        Inicializa los valores de la matriz de pagos para el dilema del prisionero.
        La matriz de pagos se define como:
        |               | Cooperar (C) | No Cooperar (D) |
        |---------------|---------------|-----------------|
        | Cooperar (C)  |  -1, -1      |   -3, 0         |
        | No Cooperar (D)|   0, -3      |   -2, -2        |
        """
        self.payoffs = {
            ('C', 'C'): (-1, -1),  # Ambos cooperan
            ('C', 'D'): (-3, 0),   # Jugador 1 coopera, Jugador 2 no
            ('D', 'C'): (0, -3),   # Jugador 1 no coopera, Jugador 2 coopera
            ('D', 'D'): (-2, -2)    # Ambos no cooperan
        }

    def get_payoff(self, action1, action2):
        """
        Devuelve la recompensa para cada jugador dado sus acciones.

        :param action1: Acción del Jugador 1 (C o D).
        :param action2: Acción del Jugador 2 (C o D).
        :return: Tupla de pagos (Jugador 1, Jugador 2).
        """
        return self.payoffs[(action1, action2)]

    def find_nash_equilibrium(self):
        """
        Encuentra el equilibrio de Nash en el juego de dilema del prisionero.

        :return: Lista de estrategias que representan el equilibrio de Nash.
        """
        strategies = [('C', 'C'), ('C', 'D'), ('D', 'C'), ('D', 'D')]
        equilibria = []
        
        for strategy in strategies:
            action1, action2 = strategy
            payoff1, payoff2 = self.get_payoff(action1, action2)
            # Verifica si las acciones son un equilibrio de Nash
            if (payoff1 >= self.get_payoff('C', action2)[0] and 
                payoff1 >= self.get_payoff('D', action2)[0] and 
                payoff2 >= self.get_payoff(action1, 'C')[1] and 
                payoff2 >= self.get_payoff(action1, 'D')[1]):
                equilibria.append(strategy)
        
        return equilibria

# Crear una instancia del juego
prisoners_dilemma = PrisonersDilemma()

# Obtener el equilibrio de Nash
nash_equilibria = prisoners_dilemma.find_nash_equilibrium()

# Imprimir los resultados
print("Equilibrios de Nash encontrados:")
for equilibrium in nash_equilibria:
    action1, action2 = equilibrium
    payoff1, payoff2 = prisoners_dilemma.get_payoff(action1, action2)
    print(f"Jugador 1: {action1}, Jugador 2: {action2} -> Pagos: {payoff1}, {payoff2}")
