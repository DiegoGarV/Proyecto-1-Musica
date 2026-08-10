from music import *

start = 3.0

mainTempo = 85

# Esta melodia debe usar LA (A), SI (B), DO# (C#), 
# RE (D), MI (E), FA# (F#), SOL (G#)

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
bass = Phrase(start) 

notesBass = []

durationBass = []

bass.addNoteList(notesBass, durationBass)

# ---------------------- Instrumento ----------------------
piano = Part("Piano", PIANO, 0)
piano.addPhrase(melody)
piano.addPhrase(bass)

# ---------------------- Partitura ----------------------
score = Score(mainTempo)
score.addPart(piano)

Play.midi(score)

# Write.midi(score, "C:\\Users\\Lenovo _ LeGion\\Documents\\Jython Music\\Trabajos\\Proyecto 1 Musica\\Cancion Propia\\CancionProyecto1.mid")