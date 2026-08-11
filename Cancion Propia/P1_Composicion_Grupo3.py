# -*- coding: utf-8 -*-
from music import *

start = 3.0

mainTempo = 85

# Esta melodía debe usar LA (A), SI (B), DO# (C#), 
# RE (D), MI (E), FA# (F#), SOL# (G#)

# ---------------------- Piano Derecha ----------------------
melody = Phrase(start) 

coro = [FS4, A4, GS4, B4, CS5, FS4, FS4, A4]

notesMelody = ([
    FS4, A4, CS5, B4,
    FS4, GS4, A4, CS5,
    E5, CS5, B4, A4,
    GS4, FS4, REST, FS4,
    FS4, A4, GS4, FS4,
    E4, FS4, A4, GS4,
    FS4, CS5, B4, A4,
    GS4, FS4, E4, FS4,
    A4, B4, CS5, A4,
    GS4, FS4, E4, CS4,
    FS4, A4, B4, CS5,
    B4, GS4, FS4, REST,
    FS4, GS4, A4, B4, A4, GS4, FS4, E4,
    FS4, A4, B4, CS5, B4, A4, GS4, FS4,
    A4, B4, CS5, E5, CS5, B4, A4, GS4,
    FS4, GS4, A4, CS5, B4, GS4, FS4, E4] + 
    coro * 4 +
    [CS5, E5, CS5, B4, A4, B4, GS4, FS4,
    A4, CS5, E5, FS5, E5, CS5, B4, A4,
    FS4, A4, CS5, E5, CS5, A4, GS4, FS4,
    E5, CS5, B4, GS4, A4, GS4, FS4, REST,
    FS4, A4, CS5, A4,
    E4, GS4, B4, GS4,
    FS4, B4, CS5, E5,
    CS5, B4, GS4, FS4] +
    coro * 4 +
    [CS5, B4,
    A4, GS4,
    FS4, E4,
    CS4, FS4
])

blancas = [HN]
negras = [QN]
corcheas = [EN]

coroDuration = corcheas * 8

durationMelody = (
    negras * 48 + 
    corcheas * 32 + 
    coroDuration * 4 + 
    corcheas * 32 + 
    negras * 16 + 
    coroDuration * 4 + 
    blancas * 8
)

melody.addNoteList(notesMelody, durationMelody)

# ---------------------- Piano Izquierda ----------------------
pianoLeft = Phrase(start)

notesPianoLeft = ([
    FS3, CS4, A3, CS4,
    D3,  A3,  FS3, A3,
    A2,  E3,  CS3, E3,
    E3,  B3,  GS3, B3,
    FS3, CS4,
    D3, A3,
    A2, E3,
    E3, B3,
    FS3, CS4,
    D3, A3,
    A2, E3,
    E3, B3,
    FS3, A3, CS4, A3,
    D3, FS3, A3, FS3,
    A2, CS3, E3, CS3,
    E3, GS3, B3, GS3,
    FS3, CS4, A3, CS4,
    D3, A3, FS3, A3,
    A2, E3, CS3, E3,
    E3, B3, GS3, B3,
    FS3, CS4, FS3, A3,
    E3, B3, E3, GS3,
    D3, A3, D3, FS3,
    E3, B3, GS3, B3,
    FS3, CS4,
    D3, A3,
    A2, E3,
    E3, B3,
    FS3, CS4, A3, CS4,
    D3, A3, FS3, A3,
    A2, E3, CS3, E3,
    E3, B3, GS3, B3,
    FS3, CS4,
    D3, A3,
    E3, B3,
    FS3, FS3
])

durationPianoLeft = (
    negras * 16 + 
    blancas * 16 + 
    negras * 48 + 
    blancas * 8 + 
    negras * 16 + 
    blancas * 8
)

pianoLeft.addNoteList(notesPianoLeft, durationPianoLeft)
pianoLeft.setDynamic(50)
# ---------------------- Bass ----------------------
# El segundo compás inicia 4 tiempos después de 'start'
bass = Phrase(start + 4.0) 

patternBass = [
    # ((E2, 2), (E2, 0.5), (C#2, 0.5), (B1, 1), (A1, 4)) - Repetición 1
    (E2, 2.0), (E2, 0.5), (CS2, 0.5), (B1, 1.0), (A1, 4.0),
    # ((E2, 2), (E2, 0.5), (C#2, 0.5), (B1, 1), (A1, 4)) - Repetición 2
    (E2, 2.0), (E2, 0.5), (CS2, 0.5), (B1, 1.0), (A1, 4.0),
    # ((E2, 2), (E2, 0.5), (D2, 0.5), (C#2, 1), (B1, 4))
    (E2, 2.0), (E2, 0.5), (D2, 0.5), (CS2, 1.0), (B1, 4.0),
    # ((E2, 2), (D2, 0.5), (C#2, 0.5), (B1, 1), (A1, 4))
    (E2, 2.0), (D2, 0.5), (CS2, 0.5), (B1, 1.0), (A1, 4.0)
]

notesBass = []
durationBass = []

target_duration = sum(durationMelody) - 4.0
current_duration = 0.0

while current_duration < target_duration:
    for note, dur in patternBass:
        if current_duration >= target_duration:
            break
        notesBass.append(note)
        durationBass.append(dur)
        current_duration += dur

bass.addNoteList(notesBass, durationBass)

# ---------------------- Guitar ----------------------
# La guitarra eléctrica inicia en el segundo compás (start + 4.0)
guitar = Phrase(start + 4.0)

# Construcción de la secuencia de notas según lo solicitado
notesGuitar = ([GS3, A3, GS3, B3] * 2 +  # 8 compases de 4 tiempos por nota
               [GS3, A3, GS3, B3] * 4 +  # 8 compases de 2 tiempos por nota
               [GS3, A3, GS3, B3] * 1 +  # 4 compases de 4 tiempos por nota
               [GS3, A3, GS3, B3] * 2 +  # 4 compases de 2 tiempos por nota
               [GS3, A3, GS3, B3] * 3)   # 12 compases de 4 tiempos por nota

# Construcción de las duraciones correspondientes
durationGuitar = ([4.0] * 8 +
                  [2.0] * 16 +
                  [4.0] * 4 +
                  [2.0] * 8 +
                  [4.0] * 12)

guitar.addNoteList(notesGuitar, durationGuitar)

# ---------------------------------------------------
# violin

violinPhrase = Phrase(start)

notesViolin = [

    
    A4,  CS5, B4, A4,

    A4, CS5, GS4, A4,

    CS5, B4, A4, GS4,

    A4, A4, CS5, B4,

    A4, A4, CS5, B4,

    CS5, A4, A4, B4,

    A4, GS4, FS4, GS4,

    A4, A4, CS5, B4,

    GS4, CS5, A4, A4
]

durationViolin = [WN] * 36

violinPhrase.addNoteList(
    notesViolin,
    durationViolin
)

violinPhrase.setDynamic(48)
violinPhrase.setPan(0.65)


# -------------------------------------------------------------
# saxofon

saxPhrase = Phrase(start)

saxNotes = []
saxDurations = []


# Cada elemento representa un compas.
# WN = compas entero
# HN + HN = dos notas dentro del compas

saxBars = [

    # Compases 1 - 4 -> piano solo
    [(REST, WN)],
    [(REST, WN)],
    [(REST, WN)],
    [(REST, WN)],


    [(CS4, HN), (B3, HN)],
    [(A3, HN),  (CS4, HN)],
    [(B3, HN),  (A3, HN)],
    [(GS3, HN), (REST, HN)],

    [(CS4, HN), (E4, HN)],
    [(B3, HN),  (GS3, HN)],
    [(A3, HN),  (CS4, HN)],
    [(GS3, HN), (REST, HN)],


    [(CS4, HN), (B3, HN)],
    [(A3, HN),  (FS3, HN)],
    [(E4, HN),  (CS4, HN)],
    [(B3, HN),  (GS3, HN)],

    [(CS4, WN)],
    [(A3, WN)],
    [(E4, WN)],
    [(B3, WN)],

    [(E4, HN),  (CS4, HN)],
    [(CS4, HN), (A3, HN)],
    [(A3, HN),  (FS3, HN)],
    [(B3, HN),  (GS3, HN)],

    [(CS4, HN), (A3, HN)],
    [(B3, HN),  (GS3, HN)],
    [(FS3, HN), (B3, HN)],
    [(GS3, HN), (CS4, HN)],

    [(CS4, WN)],
    [(A3, WN)],
    [(E4, WN)],
    [(B3, WN)],

    [(GS3, HN), (CS4, HN)],
    [(E4, HN),  (CS4, HN)],
    [(CS4, HN), (A3, HN)],
    [(FS3, WN)]
]


for bar in saxBars:

    for noteData in bar:

        saxNotes.append(noteData[0])
        saxDurations.append(noteData[1])


saxPhrase.addNoteList(
    saxNotes,
    saxDurations
)

saxPhrase.setDynamic(55)

# hacia la izquierda
saxPhrase.setPan(0.35)



# ---------------------- Instrumentos ----------------------
pianoPart = Part("Piano", PIANO, 0)
pianoPart.addPhrase(melody)
pianoPart.addPhrase(pianoLeft)

bassPart = Part("Bajo Electrico", ELECTRIC_BASS, 1)
bassPart.addPhrase(bass)

guitarPart = Part("Guitarra Electrica", ELECTRIC_GUITAR, 2)
guitarPart.addPhrase(guitar)

violin = Part( "Violin", VIOLIN, 3)
violin.addPhrase(violinPhrase)

sax = Part( "Saxofon", TENOR_SAX, 4 )
sax.addPhrase(saxPhrase)




# ---------------------- Partitura ----------------------
score = Score(mainTempo)
score.addPart(pianoPart)
score.addPart(bassPart)
score.addPart(guitarPart)
score.addPart(violin)
score.addPart(sax)

# Play.midi(score)

Write.midi(score, "C:\\Users\\Lenovo _ LeGion\\Documents\\Jython Music\\Trabajos\\Proyecto 1 Musica\\Cancion Propia\\P1_Composicion_Grupo3.mid")