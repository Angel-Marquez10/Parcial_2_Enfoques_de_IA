
import random
import time

class Robot:
    def __init__(self):
        self.sensor_value = 0

    def read_sensor(self):
        # Simulación de la lectura de un sensor (valor entre 0 y 100)
        self.sensor_value = random.randint(0, 100)
        print(f"Valor del sensor: {self.sensor_value}")

    def actuate(self):
        if self.sensor_value > 50:
            print("Actuador activado: El valor es alto, actuando para bajar el nivel.")
        else:
            print("Actuador activado: El valor es bajo, actuando para subir el nivel.")

# Simulación del funcionamiento del robot
robot = Robot()
for _ in range(5):  # Realizar 5 lecturas
    robot.read_sensor()
    robot.actuate()
    time.sleep(1)  # Esperar 1 segundo entre lecturas
