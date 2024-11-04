class DecisionNode:
    """Clase que representa un nodo de decisión en la red."""
    def __init__(self, name):
        """Inicializa el nodo de decisión con un nombre y listas para hijos y resultados."""
        self.name = name  # Nombre del nodo
        self.children = []  # Lista de nodos hijos
        self.outcomes = {}  # Diccionario para almacenar los resultados y sus utilidades
    
    def add_outcome(self, outcome_name, utility):
        """Agrega un resultado con su utilidad al nodo de decisión."""
        self.outcomes[outcome_name] = utility  # Almacena el resultado con su utilidad
    
    def add_child(self, child_node):
        """Agrega un nodo hijo a este nodo de decisión."""
        self.children.append(child_node)  # Agrega el nodo hijo a la lista

    def __str__(self):
        """Devuelve el nombre del nodo para facilitar su impresión."""
        return self.name

def calculate_expected_utility(node):
    """Calcula la utilidad esperada a partir de un nodo de decisión."""
    # Verifica si el nodo no tiene hijos (es un resultado final)
    if not node.children:  
        return node.outcomes  # Retorna los resultados y utilidades de este nodo

    expected_utilities = {}  # Diccionario para almacenar las utilidades esperadas
    # Recorre todos los nodos hijos
    for child in node.children:
        # Calcula las utilidades de los nodos hijos recursivamente
        utilities = calculate_expected_utility(child)  
        for outcome, utility in utilities.items():
            if outcome not in expected_utilities:
                expected_utilities[outcome] = 0  # Inicializa la utilidad si no existe
            expected_utilities[outcome] += utility  # Suma la utilidad al total

    return expected_utilities  # Retorna las utilidades esperadas acumuladas

def build_decision_network():
    """Construye la red de decisión para el problema de inversión."""
    # Crea el nodo de decisión principal
    investment_decision = DecisionNode("Decisión de Inversión")
    # Crea nodos para las opciones de inversión
    investment_a = DecisionNode("Inversión A")
    investment_b = DecisionNode("Inversión B")

    # Agrega resultados y sus utilidades para la Inversión A
    investment_a.add_outcome("Alto Retorno", 100)  # Resultado: Alto Retorno con utilidad 100
    investment_a.add_outcome("Bajo Retorno", 20)   # Resultado: Bajo Retorno con utilidad 20
    investment_decision.add_child(investment_a)    # Conecta la opción A al nodo principal

    # Agrega resultados y sus utilidades para la Inversión B
    investment_b.add_outcome("Alto Retorno", 80)    # Resultado: Alto Retorno con utilidad 80
    investment_b.add_outcome("Bajo Retorno", 10)     # Resultado: Bajo Retorno con utilidad 10
    investment_decision.add_child(investment_b)      # Conecta la opción B al nodo principal

    return investment_decision  # Retorna la red de decisión construida

def main():
    """Función principal para ejecutar el ejemplo de red de decisión."""
    decision_network = build_decision_network()  # Construye la red de decisión
    
    # Calcula la utilidad esperada de la red de decisión
    expected_utilities = calculate_expected_utility(decision_network)
    
    # Imprime las utilidades esperadas para cada resultado
    print("Utilidades esperadas para cada resultado:")
    for outcome, utility in expected_utilities.items():
        print(f"{outcome}: {utility}")

if __name__ == "__main__":
    main()  # Llama a la función principal al ejecutar el script
