
import speech_recognition as sr

# Inicialización del reconocedor
reconocedor = sr.Recognizer()

# Función para captar y reconocer el habla
def reconocer_habla():
    with sr.Microphone() as source:
        print("Por favor, hable algo...")
        audio = reconocedor.listen(source)
        try:
            texto = reconocedor.recognize_google(audio, language="es-MX")
            print("Texto reconocido:", texto)
        except sr.UnknownValueError:
            print("No se pudo entender el audio.")
        except sr.RequestError:
            print("Error con el servicio de reconocimiento.")
            
# Ejemplo de uso
reconocer_habla()
