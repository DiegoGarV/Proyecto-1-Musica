from music import *


class Violoncello(object):

    def __init__(self):
        self.nombre = "Violoncello"
        self.instrumento = CELLO
        self.canal = 4

    def crear_frase(self):
        frase = Phrase(0.0)

        notasCoro = [
            D3, A2,
            E3, B2
        ]

        notas = ([
            E3, D3
        ] + notasCoro * 13 + [
            D3, A2,
            REST, GS2, B2, GS2, A2, FS2, A2,
            D3, A2, D3, CS3, A2, CS3,
            REST, GS2, B2, GS2, A2, FS2, A2,
            D3, A2, D3, CS3, A2, CS3,
            REST, GS2, B2, GS2, A2, FS2, A2
        ])

        blancas = [HN]
        negras = [QN]
        corcheas = [EN]
        durationTot = (
            blancas * 56 + 
            corcheas * 6 + negras + 
            corcheas * 2 + negras + corcheas * 2 + negras + 
            corcheas * 6 + negras + 
            corcheas * 2 + negras + corcheas * 2 + negras + 
            corcheas * 6 + negras
        )

        if len(notas) != len(durationTot):
            raise ValueError(
                "El violoncello debe tener la misma cantidad de notas y duraciones."
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

# Crear la parte del instrumento
cello = Violoncello()
parte_cello = cello.crear_parte()

# Crear la partitura (Score) a 83 BPM
partitura = Score("Violoncello Song", 83.0)

# Configurar el compás en 4/4
partitura.setTimeSignature(4, 4)

# Agregar la parte a la partitura
partitura.addPart(parte_cello)

# Guardar como archivo MIDI
Write.midi(partitura, "violoncello_83bpm.mid")