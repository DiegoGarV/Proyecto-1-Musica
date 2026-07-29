from music import *


class Violoncello(object):

    def __init__(self):
        self.nombre = "Violoncello"
        self.instrumento = 42  # Cello
        self.canal = 4

    def crear_frase(self):
        frase = Phrase(0.0)

        notas = [
            # Colocar notas aquí.
        ]

        duraciones = [
            # Colocar duraciones aquí.
        ]

        if len(notas) != len(duraciones):
            raise ValueError(
                "El violoncello debe tener la misma cantidad de notas y duraciones."
            )

        if len(notas) > 0:
            frase.addNoteList(notas, duraciones)

        return frase

    def crear_parte(self):
        parte = Part(
            self.nombre,
            self.instrumento,
            self.canal
        )

        parte.addPhrase(self.crear_frase())

        return parte