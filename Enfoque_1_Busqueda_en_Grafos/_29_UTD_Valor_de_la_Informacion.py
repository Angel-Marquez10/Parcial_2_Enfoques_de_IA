class DecisionNode:
    """Clase que representa un nodo de decisión."""
    def __init__(self, name):
        """Inicializa un nodo de decisión con un nombre."""
        self.name = name
        self.children = []  # Lista de nodos hijos
        self.outcomes = {}  # Diccionario para almacenar resultados y utilidades

    def add_outcome(self, outcome_name, utility):
        """Agrega un resultado con su utilidad al nodo."""
        self.outcomes[outcome_name] = utility

    def add_child(self, child_node):
        """Agrega un nodo hijo a este nodo."""
        self.children.append(child_node)

    def __str__(self):
        """Devuelve el nombre del nodo."""
        return self.name


def calculate_expected_utility(node):
    """Calcula la utilidad esperada a partir de un nodo de decisión."""
    # Verifica si el nodo no tiene hijos
    if not node.children:
        return node.outcomes  # Retorna las utilidades de los resultados

    expected_utilities = {}
    for child in node.children:
        utilities = calculate_expected_utility(child)
        for outcome, utility in utilities.items():
            if outcome not in expected_utilities:
                expected_utilities[outcome] = 0
            expected_utilities[outcome] += utility

    return expected_utilities


def build_decision_network():
    """Construye una red de decisión para ilustrar el valor de la información."""
    # Crea el nodo de decisión principal
    main_decision = DecisionNode("Decisión de Inversión")
    
    # Crea un nodo para la opción de invertir sin información
    investment_no_info = DecisionNode("Inversión Sin Información")
    investment_no_info.add_outcome("Alto Retorno", 80)  # Utilidad 80
    investment_no_info.add_outcome("Bajo Retorno", 20)   # Utilidad 20
    main_decision.add_child(investment_no_info)          # Conecta al nodo principal

    # Crea un nodo para la opción de invertir con información
    investment_with_info = DecisionNode("Inversión Con Información")
    # Resultados posibles después de obtener información
    investment_with_info.add_outcome("Alto Retorno", 100)  # Utilidad 100
    investment_with_info.add_outcome("Bajo Retorno", 40)   # Utilidad 40
    main_decision.add_child(investment_with_info)          # Conecta al nodo principal

    return main_decision


def calculate_value_of_information(main_decision):
    """Calcula el valor de la información al comparar utilidades esperadas."""
    # Utilidad esperada sin información
    utility_no_info = calculate_expected_utility(main_decision.children[0])
    
    # Utilidad esperada con información
    utility_with_info = calculate_expected_utility(main_decision.children[1])

    # Sumar las utilidades esperadas
    expected_utility_no_info = sum(utility_no_info.values())
    expected_utility_with_info = sum(utility_with_info.values())

    # Calcular el valor de la información
    value_of_information = expected_utility_with_info - expected_utility_no_info
    
    return expected_utility_no_info, expected_utility_with_info, value_of_information


def main():
    """Función principal para ejecutar el ejemplo de valor de la información."""
    decision_network = build_decision_network()  # Construye la red de decisión
    
    # Calcula el valor de la información
    utility_no_info, utility_with_info, value_of_info = calculate_value_of_information(decision_network)
    
    # Imprime los resultados
    print("Utilidad esperada sin información:", utility_no_info)
    print("Utilidad esperada con información:", utility_with_info)
    print("Valor de la información:", value_of_info)


if __name__ == "__main__":
    main()  # Llama a la función principal al ejecutar el script
