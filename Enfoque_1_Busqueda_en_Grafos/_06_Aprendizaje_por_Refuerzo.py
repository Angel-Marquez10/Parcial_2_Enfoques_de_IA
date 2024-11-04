import numpy as np  # Importamos la biblioteca NumPy para trabajar con matrices
import random  # Importamos la biblioteca random para generar números aleatorios

# Definimos el laberinto como una matriz
# 0: Camino, 1: Obstáculo, 2: Inicio, 3: Meta
maze = [
    [0, 1, 0, 0, 0],  # Fila 0
    [0, 1, 0, 1, 0],  # Fila 1
    [0, 0, 0, 1, 0],  # Fila 2
    [0, 1, 0, 1, 0],  # Fila 3
    [2, 0, 0, 0, 3]   # Fila 4 (Inicio en (4,0), Meta en (4,4))
]

# Parámetros del entorno y del aprendizaje por refuerzo
alpha = 0.8      # Tasa de aprendizaje (cómo de rápido aprende el agente)
gamma = 0.9      # Factor de descuento (importancia de las futuras recompensas)
epsilon = 0.9    # Probabilidad de exploración inicial (exploración vs explotación)
episodes = 1000  # Número de episodios para entrenar al agente

# Inicializamos la tabla Q con ceros
# La tabla Q tendrá dimensiones: (filas del laberinto, columnas del laberinto, 4 acciones posibles)
q_table = np.zeros((len(maze), len(maze[0]), 4))  # 4 acciones: arriba, abajo, izquierda, derecha

# Definimos las recompensas
reward_goal = 10     # Recompensa al llegar a la meta
reward_penalty = -1  # Penalización por movimiento normal (no es un obstáculo ni la meta)
reward_obstacle = -5 # Penalización por chocar con un obstáculo

# Definimos las acciones y sus respectivas coordenadas
actions = ["up", "down", "left", "right"]
action_deltas = {
    "up": (-1, 0),    # Moverse hacia arriba
    "down": (1, 0),   # Moverse hacia abajo
    "left": (0, -1),  # Moverse hacia la izquierda
    "right": (0, 1)   # Moverse hacia la derecha
}

# Función para verificar si la posición es válida en el laberinto
def is_valid_position(x, y):
    # Verificamos que la posición esté dentro de los límites del laberinto y que no sea un obstáculo
    return 0 <= x < len(maze) and 0 <= y < len(maze[0]) and maze[x][y] != 1

# Función para ejecutar el algoritmo Q-learning
def q_learning():
    global epsilon  # Declaramos que vamos a modificar la variable epsilon
    print("Iniciando el entrenamiento del agente...\n")
    
    for episode in range(episodes):  # Iteramos sobre el número de episodios
        # Inicializamos la posición del agente (Inicio)
        x, y = 4, 0  # El agente comienza en la posición (4,0)
        print(f"\nEpisodio {episode + 1}/{episodes}: Explorando desde la posición de inicio (4,0).")
        
        # Bucle hasta que el agente llega a la meta (3)
        while maze[x][y] != 3:
            # Elegimos una acción (exploración o explotación)
            if random.uniform(0, 1) < epsilon:
                action_index = random.choice(range(4))  # Exploración aleatoria
                print(f"  Exploración: el agente elige una acción aleatoria.")
            else:
                action_index = np.argmax(q_table[x][y])  # Explotación, elige la mejor opción aprendida
                print(f"  Explotación: el agente elige la mejor acción aprendida.")
            
            action = actions[action_index]  # Obtenemos la acción basada en el índice
            dx, dy = action_deltas[action]  # Obtenemos los cambios de posición correspondientes
            new_x, new_y = x + dx, y + dy  # Calculamos la nueva posición

            # Verificamos si el movimiento a la nueva posición es válido
            if is_valid_position(new_x, new_y):
                # Determinamos la recompensa
                if maze[new_x][new_y] == 3:  # Si ha alcanzado la meta
                    reward = reward_goal  # Recompensa por alcanzar la meta
                    print("  ¡Meta alcanzada! Recompensa recibida:", reward)
                else:
                    reward = reward_penalty  # Penalización por movimiento normal
                    print(f"  Movimiento hacia ({new_x},{new_y}), recompensa por moverse:", reward)
            else:
                reward = reward_obstacle  # Penalización por chocar con un obstáculo
                new_x, new_y = x, y  # El agente no se mueve
                print(f"  Choque con obstáculo en ({new_x},{new_y}), penalización:", reward)

            # Actualizamos la tabla Q usando la fórmula de Q-learning
            old_q_value = q_table[x][y][action_index]  # Valor Q anterior
            next_max_q_value = np.max(q_table[new_x][new_y])  # Máximo valor Q en la nueva posición
            # Fórmula de actualización de Q-learning
            q_table[x][y][action_index] = old_q_value + alpha * (reward + gamma * next_max_q_value - old_q_value)
            
            print(f"  Actualizando tabla Q: Estado ({x},{y}), Acción '{action}', Valor Q anterior: {old_q_value:.2f}, Nuevo Valor Q: {q_table[x][y][action_index]:.2f}")
            
            # Actualizamos la posición del agente
            x, y = new_x, new_y

        # Reducimos epsilon para que el agente explore menos en episodios futuros
        epsilon = max(0.1, epsilon * 0.99)  # Limitamos a un mínimo de 0.1 para asegurar alguna exploración

    print("\nEntrenamiento completado. El agente ha aprendido a moverse en el laberinto.")

# Función para probar la ruta óptima aprendida por el agente
def test_agent():
    print("\nEvaluando la ruta óptima aprendida por el agente...\n")
    x, y = 4, 0  # El agente comienza en la posición de inicio
    route = [(x, y)]  # Almacenamos la ruta que toma el agente
    
    # Bucle hasta que el agente llega a la meta
    while maze[x][y] != 3:
        action_index = np.argmax(q_table[x][y])  # Tomamos la mejor acción aprendida
        action = actions[action_index]  # Obtenemos la acción correspondiente
        dx, dy = action_deltas[action]  # Obtenemos los cambios de posición
        x, y = x + dx, y + dy  # Actualizamos la posición del agente
        route.append((x, y))  # Agregamos la nueva posición a la ruta
        print(f"  El agente se mueve a la posición ({x},{y}) usando la acción '{action}'")
    
    print("\nRuta óptima encontrada:", route)  # Mostramos la ruta aprendida
    return route

# Ejecutamos el aprendizaje por refuerzo
q_learning()

# Probamos el agente en el laberinto después del entrenamiento
optimal_route = test_agent()

# Imprimimos la ruta óptima
print("\nRuta óptima aprendida por el agente:", optimal_route)
