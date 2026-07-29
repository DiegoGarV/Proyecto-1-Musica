from music import *


class Guitarra(object):

    def __init__(self):
        self.nombre = "Guitarra"
        self.instrumento = 24  # Acoustic Guitar Nylon
        self.canal = 1

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
                "La guitarra debe tener la misma cantidad de notas y duraciones."
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