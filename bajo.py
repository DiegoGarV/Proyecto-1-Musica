from music import *

repet=5

class Bajo(object):

    def __init__(self, tempo=120, numerador=4, denominador=4):
        self.nombre = "Bajo"
        self.instrumento = ELECTRIC_BASS
        self.canal = 0
        self.tempo = tempo                  # BPM
        self.numerador = numerador          # Ej. 4 para 4/4
        self.denominador = denominador      # Ej. 4 para 4/4

    def crear_frase(self):
        frase = Phrase(0.0)

        # Configuración de Tempo y Compás
        frase.setTempo(self.tempo)
        frase.setNumerator(self.numerador)
        frase.setDenominator(self.denominador)

        notas = [
            E2, B1, REST,                   # Compás 1
            A1, REST, A1, A1, A1, REST, A1  # Compás 2
        ]*repet

        duraciones = [
            2.0, 1.5, 0.5,                      # Compás 1
            1.0, 0.5, 0.25, 0.25, 1.0, 0.5, 0.5  # Compás 2
        ]*repet

        if len(notas) != len(duraciones):
            raise ValueError(
                "El bajo debe tener la misma cantidad de notas y duraciones."
            )

        if len(notas) > 0:
            frase.addNoteList(notas, duraciones)

        return frase

    def crear_parte(self):
        parte = Part(self.nombre, self.instrumento, self.canal)
        parte.addPhrase(self.crear_frase())
        return parte



mi_bajo = Bajo(tempo=83, numerador=4, denominador=4)
parte_bajo = mi_bajo.crear_parte()

Play.midi(parte_bajo)