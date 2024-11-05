
import re

# Texto de ejemplo
texto = """
Juan tiene 28 años y vive en la ciudad de México.
María tiene 22 años y vive en Guadalajara.
El perro de Juan se llama Max y el gato de María se llama Miau.
"""

# Expresión regular para encontrar nombres y edades
patron = r'(\b\w+\b) tiene (\d+) años'
resultados = re.findall(patron, texto)

# Mostrar resultados
for nombre, edad in resultados:
    print(f'Nombre: {nombre}, Edad: {edad}')
