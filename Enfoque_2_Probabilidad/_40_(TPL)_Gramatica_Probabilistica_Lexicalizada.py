
import random

class LexicalizedGrammar:
    def __init__(self):
        self.grammar = {
            'S': [(0.5, 'NP VP'), (0.5, 'VP')],
            'NP': [(0.6, 'Det N'), (0.4, 'Name')],
            'VP': [(0.7, 'V NP'), (0.3, 'V')],
            'Det': [(1.0, 'el'), (1.0, 'la')],
            'N': [(0.5, 'perro'), (0.5, 'gato')],
            'V': [(0.5, 've'), (0.5, 'escucha')],
            'Name': [(1.0, 'Juan'), (1.0, 'Maria')],
        }

    def generate(self, symbol='S'):
        production = random.choices(
            [prod for prod in self.grammar[symbol]],
            weights=[prod[0] for prod in self.grammar[symbol]]
        )[0][1]
        return ' '.join(self.generate(sym) for sym in production.split())

# Ejemplo de uso
grammar = LexicalizedGrammar()
for _ in range(5):  # Generar 5 oraciones
    print(grammar.generate())
