# -*- coding: utf-8 -*-
from music import *

repet=4

class Guitarra(object):

    def __init__(self, tempo=120, numerador=4, denominador=4):
        self.nombre = "Guitarra"
        self.instrumento = ELECTRIC_GUITAR  # Acoustic Guitar Nylon
        self.canal = 1
        self.tempo = tempo                  # BPM
        self.numerador = numerador          # Ej. 4 para 4/4
        self.denominador = denominador      # Ej. 4 para 4/4


    def crear_frase(self):
        frase = Phrase(0.0)

        notas = [REST, E2, GS2, REST, FS2, A2, # Compás 1
                 REST, A2, D3, REST, A2, CS3 # Compás 2
        ]*repet

        duraciones = [0.5, 0.5, 1, 0.5, 0.5, 1, # Compás 1
                      0.5, 0.5, 1, 0.5, 0.5, 1 # Compás 2
        ]*repet

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
      
mi_guitarra = Guitarra(tempo=83, numerador=4, denominador=4)
parte_guitarra = mi_guitarra.crear_parte()

# Play.midi(parte_guitarra)
Write.midi(parte_guitarra, "guitarra.mid")