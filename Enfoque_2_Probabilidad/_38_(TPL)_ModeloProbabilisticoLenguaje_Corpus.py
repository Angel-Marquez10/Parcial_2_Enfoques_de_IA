
import numpy as np
from collections import defaultdict

class NGramLanguageModel:
    def __init__(self, n):
        self.n = n
        self.ngrams = defaultdict(lambda: defaultdict(int))

    def train(self, corpus):
        for sentence in corpus:
            words = sentence.split()
            for i in range(len(words) - self.n + 1):
                ngram = tuple(words[i:i + self.n])
                self.ngrams[ngram[:-1]][ngram[-1]] += 1

    def probability(self, prefix, word):
        if prefix in self.ngrams:
            total_count = float(sum(self.ngrams[prefix].values()))
            return self.ngrams[prefix][word] / total_count
        else:
            return 0.0

# Ejemplo de uso
corpus = [
    "la casa es bonita",
    "la casa es grande",
    "el perro es bonito",
    "la casa y el perro",
]

# Creación y entrenamiento del modelo de lenguaje
model = NGramLanguageModel(n=2)
model.train(corpus)

# Cálculo de probabilidades
print("Probabilidad de 'bonita' dado 'la casa':", model.probability(('la', 'casa'), 'bonita'))
print("Probabilidad de 'grande' dado 'la casa':", model.probability(('la', 'casa'), 'grande'))
