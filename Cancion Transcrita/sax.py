from music import *

# C, F y G son Sharp

class Saxofon(object):

    def __init__(self):
        self.nombre = "Saxofon"
        self.instrumento = ALTO_SAX
        self.canal = 3

    def crear_frase(self):
        frase = Phrase(0.0)

        notasCoro = [
            REST, ES4, GS4, ES4, REST, DS4, FS4, DS4,
            REST, FS4, B4, FS4, REST, FS4, AS4, FS4
        ]

        notas = ([
            ES4, FS4,
            FS4, FS4,
            ES4, FS4,
            FS4, FS4, AS4, CS5, ES5,
            GS5,
            GS5,
            GS5,
            GS5,
            ES4, FS4,
            FS4, FS4,
            ES4, FS4,
            FS4, FS4,
            REST, ES5, GS5, ES5, FS5, DS5, FS5,
            B5, FS5, B5, AS5, FS5, AS5,
            ES5, GS5, ES5, FS5, DS5, FS5,
            B5, FS5, B5, AS5, FS5, AS5,
            REST, ES5, GS5, ES5, FS5, DS5, FS5,
            B5, FS5, B5, AS5, FS5, AS5,
            ES5, GS5, ES5, FS5, DS5, FS5,
            B5, FS5, B5, AS5, FS5, AS5
        ] + notasCoro * 4 + [
            CS5, GS4,
            A4, FS4,
            CS5, GS4,
            A4, FS4,
            CS5, GS4
        ])

        blancas = [HN]
        negras = [QN]
        corcheas = [EN]
        redondas = [WN]
        durationTot = (
            blancas * 7 + corcheas * 4 + redondas * 4 + blancas * 8 + 
            corcheas * 6 + negras + corcheas * 2 + negras + corcheas * 2 + negras + 
            corcheas * 5 + negras + corcheas * 2 + negras + corcheas * 2 + negras + 
            corcheas * 6 + negras + corcheas * 2 + negras + corcheas * 2 + negras + 
            corcheas * 5 + negras + corcheas * 2 + negras + corcheas * 2 + negras + 
            corcheas * 64 + blancas * 10 
        )

        if len(notas) != len(durationTot):
            raise ValueError(
                "El saxofon debe tener la misma cantidad de notas y duraciones."
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
sax = Saxofon()
parte_sax = sax.crear_parte()

# Crear la partitura (Score) especificando el tempo a 83 BPM
partitura = Score("Saxofon Song", 83.0)

# Establecer el compás en 4/4
partitura.setTimeSignature(4, 4)

# Agregar la parte a la partitura
partitura.addPart(parte_sax)

# Guardar como archivo MIDI
Write.midi(partitura, "saxofon_83bpm.mid")