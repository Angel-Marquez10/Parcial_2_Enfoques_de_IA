
import pytesseract
from PIL import Image
import matplotlib.pyplot as plt

# Cargar la imagen de ejemplo
img_path = 'ejemplo_texto.jpg'  # Asegúrate de que la imagen esté en el mismo directorio
img = Image.open(img_path)

# Realizar el reconocimiento de texto
texto = pytesseract.image_to_string(img, lang='spa')

# Mostrar resultados
print("Texto reconocido:")
print(texto)

# Visualizar la imagen
plt.imshow(img)
plt.axis('off')
plt.title("Reconocimiento de Escritura")
plt.show()
