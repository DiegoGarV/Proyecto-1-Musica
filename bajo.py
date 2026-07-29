from music import *


class Bajo(object):

    def __init__(self):
        self.nombre = "Bajo"
        self.instrumento = 32  # Acoustic Bass
        self.canal = 0

    def crear_frase(self):
        # 0.0 significa que empieza desde el inicio de la canción.
        frase = Phrase(0.0)

        notas = [
            # Colocar notas aquí.

        ]

        duraciones = [
            # Colocar duraciones aquí.

        ]

        if len(notas) != len(duraciones):
            raise ValueError(
                "El bajo debe tener la misma cantidad de notas y duraciones."
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