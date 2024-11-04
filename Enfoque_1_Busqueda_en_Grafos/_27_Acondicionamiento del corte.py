from itertools import product

def print_assignment(assignment):
    """Imprime la asignación de tareas a los empleados."""
    print("Asignación de tareas:")
    for employee, task in assignment.items():
        print(f"Empleado {employee}: Tarea {task}")
    print()

def is_valid_assignment(assignment, restrictions):
    """Verifica si la asignación es válida según las restricciones."""
    for employee, task in assignment.items():
        if task in restrictions.get(employee, []):
            return False
    return True

def conditioning_cut(assignment, tasks, restrictions):
    """Aplica el acondicionamiento del corte para reducir el espacio de búsqueda."""
    for employee, task in assignment.items():
        # Si el empleado tiene una tarea ya asignada, eliminamos esa tarea de los demás empleados
        if task is not None:
            for other_employee in tasks.keys():
                if other_employee != employee and task in tasks[other_employee]:
                    tasks[other_employee].remove(task)
    return tasks

def assign_tasks(employees, tasks, restrictions):
    """Asigna tareas a empleados utilizando acondicionamiento del corte."""
    initial_assignment = {employee: None for employee in employees}
    
    # Genera todas las combinaciones posibles de asignaciones de tareas
    all_assignments = product(*[tasks[employee] for employee in employees])
    
    for task_combination in all_assignments:
        assignment = dict(zip(employees, task_combination))
        
        # Verifica si la asignación es válida
        if is_valid_assignment(assignment, restrictions):
            print("Asignación válida encontrada:")
            print_assignment(assignment)
            return assignment
        
        # Aplica el acondicionamiento del corte
        print(f"Intentando asignación: {assignment} (no válida)")
        conditioned_tasks = conditioning_cut(assignment, tasks, restrictions)
        
        # Muestra el estado del espacio de búsqueda después del acondicionamiento
        print("Estado después del acondicionamiento:")
        for employee, available_tasks in conditioned_tasks.items():
            print(f"Empleado {employee}: Tareas disponibles {available_tasks}")
        print()
        
    print("No se encontró una asignación válida.")
    return None

def task_assignment_problem():
    """Inicializa el problema de asignación de tareas."""
    employees = ['A', 'B', 'C']
    tasks = {
        'A': ['T1', 'T2', 'T3'],
        'B': ['T1', 'T2', 'T3'],
        'C': ['T1', 'T2', 'T3']
    }
    
    # Definir restricciones: qué tareas no pueden ser asignadas a qué empleados
    restrictions = {
        'A': ['T1'],  # A no puede tener la tarea T1
        'B': ['T2'],  # B no puede tener la tarea T2
        'C': []       # C no tiene restricciones
    }

    print("Empezando el problema de asignación de tareas...\n")
    assign_tasks(employees, tasks, restrictions)

# Ejemplo de uso
if __name__ == "__main__":
    task_assignment_problem()
