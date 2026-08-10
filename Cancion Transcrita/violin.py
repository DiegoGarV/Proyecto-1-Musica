from music import *


class Violin(object):

    def __init__(self):
        self.nombre = "Violin"
        self.instrumento = VIOLIN
        self.canal = 5

    def crear_frase(self):
        frase = Phrase(0.0)

        notasCoro = [
            D5, A4,
            E5, B4
        ]

        notas = ([E5, D5] + notasCoro * 16)

        blancas = [HN]
        durationTot = (blancas * 66)

        if len(notas) != len(durationTot):
            raise ValueError(
                "El violin debe tener la misma cantidad de notas y duraciones."
            )

        if len(notas) > 0:
            frase.addNoteList(notas, durationTot)

        return frase

    def crear_parte(self):
        parte = Part(
            self.nombre,
            self.instrumento,
            self.canal
        )

        parte.addPhrase(self.crear_frase())

        return parte