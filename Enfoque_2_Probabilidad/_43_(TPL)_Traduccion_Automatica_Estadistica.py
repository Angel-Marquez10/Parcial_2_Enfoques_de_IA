
import numpy as np

class TranslationModel:
    def __init__(self):
        # Probabilidades de traducción de palabras
        self.translation_probabilities = {
            'Hola': {'Hello': 0.8, 'Hi': 0.2},
            'Adiós': {'Goodbye': 0.9, 'See you': 0.1},
            'Gracias': {'Thank you': 1.0},
            'Por favor': {'Please': 1.0}
        }

    def translate(self, word):
        if word in self.translation_probabilities:
            translations = self.translation_probabilities[word]
            return max(translations, key=translations.get)  # Devuelve la traducción más probable
        else:
            return None

# Ejemplo de uso
model = TranslationModel()
words_to_translate = ['Hola', 'Adiós', 'Gracias', 'Por favor']

for word in words_to_translate:
    translated = model.translate(word)
    if translated:
        print(f'Traducción de "{word}": "{translated}"')
    else:
        print(f'No hay traducción disponible para "{word}".')
