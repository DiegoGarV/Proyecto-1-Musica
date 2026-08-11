from music import *

start = 3.0

mainTempo = 85

# Esta melodía debe usar LA (A), SI (B), DO# (C#), 
# RE (D), MI (E), FA# (F#), SOL# (G#)

# ---------------------- Melody ----------------------
melody = Phrase(start) 

coro = [FS4, A4, GS4, B4, CS5, FS4, FS4, A4]

notesMelody = ([FS4, A4, CS5, B4,
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
                CS4, FS4])

blancas = [HN]
negras = [QN]
corcheas = [EN]

coroDuration = corcheas * 8

durationMelody = (negras * 48 + corcheas * 32 + coroDuration * 4 + corcheas * 32 + negras * 16 + coroDuration * 4 + blancas * 8)

melody.addNoteList(notesMelody, durationMelody)

# ---------------------- Bass ----------------------
# El segundo compás inicia 4 tiempos después de 'start'
bass = Phrase(start + 4.0) 

# Definición de la secuencia de bajo
pattern = [
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

# Duración requerida para el bajo (duración total menos el primer compás)
target_duration = sum(durationMelody) - 4.0
current_duration = 0.0

# Se repite el patrón hasta cubrir toda la canción
while current_duration < target_duration:
    for note, dur in pattern:
        if current_duration >= target_duration:
            break
        notesBass.append(note)
        durationBass.append(dur)
        current_duration += dur

bass.addNoteList(notesBass, durationBass)

# ---------------------- Instrumentos ----------------------
# Piano para la melodía (Canal 0)
pianoPart = Part("Piano", PIANO, 0)
pianoPart.addPhrase(melody)

# Bajo Eléctrico para el bajo (Canal 1)
bassPart = Part("Bajo Electrico", ELECTRIC_BASS, 1)
bassPart.addPhrase(bass)

# ---------------------- Partitura ----------------------
score = Score(mainTempo)
score.addPart(pianoPart)
score.addPart(bassPart)

Play.midi(score)

# Write.midi(score, "C:\\Users\\Lenovo _ LeGion\\Documents\\Jython Music\\Trabajos\\Proyecto 1 Musica\\Cancion Propia\\CancionProyecto1.mid")