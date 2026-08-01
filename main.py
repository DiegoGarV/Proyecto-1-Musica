from music import *

# from bajo import Bajo
# from guitar import Guitarra
# from piano import Piano
from sax import Saxofon
from violoncello import Violoncello
from violin import Violin


tempo = 82
cancion = "Bitter Sweet Symphony"


def crear_cancion():
    partitura = Score(cancion, tempo)

    # bajo = Bajo()
    # guitarra = Guitarra()
    # piano = Piano()
    saxofon = Saxofon()
    violoncello = Violoncello()
    violin = Violin()

    partes = [
        # bajo.crear_parte(),
        # guitarra.crear_parte(),
        # piano.crear_parte(),
        saxofon.crear_parte(),
        violoncello.crear_parte(),
        violin.crear_parte()
    ]

    partitura.addPartList(partes)
    
    return partitura


def playSong():
    partitura = crear_cancion()

    # Se llama una sola vez para reproducir todos
    # los instrumentos simultaneamente.
    Play.midi(partitura)


def main():
    playSong()



main()