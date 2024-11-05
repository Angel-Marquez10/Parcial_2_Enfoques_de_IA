
import sqlite3

# Crear una conexión a la base de datos
conexion = sqlite3.connect('ejemplo.db')

# Crear un cursor
cursor = conexion.cursor()

# Crear una tabla
cursor.execute('''
CREATE TABLE IF NOT EXISTS usuarios (
    id INTEGER PRIMARY KEY,
    nombre TEXT NOT NULL,
    edad INTEGER NOT NULL
)
''')

# Insertar algunos datos
cursor.execute("INSERT INTO usuarios (nombre, edad) VALUES ('Juan', 28)")
cursor.execute("INSERT INTO usuarios (nombre, edad) VALUES ('Maria', 22)")
conexion.commit()

# Recuperar datos
cursor.execute("SELECT * FROM usuarios")
usuarios = cursor.fetchall()

# Mostrar los resultados
for usuario in usuarios:
    print(f'ID: {usuario[0]}, Nombre: {usuario[1]}, Edad: {usuario[2]}')

# Cerrar la conexión
conexion.close()
