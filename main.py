from music import *

from bajo import Bajo
from guitar import Guitarra
from piano import Piano
from sax import Saxofon
from violoncello import Violoncello


tempo = 82
cancion = "Bitter Sweet Symphony "


def crear_cancion():
    cancion = Score(cancion, tempo)

    bajo = Bajo()
    guitarra = Guitarra()
    piano = Piano()
    saxofon = Saxofon()
    violoncello = Violoncello()

    partes = [
        bajo.crear_parte(),
        guitarra.crear_parte(),
        piano.crear_parte(),
        saxofon.crear_parte(),
        violoncello.crear_parte()
    ]

    cancion.addPartList(partes)

    return cancion


def playSong():
    cancion = crear_cancion()

    # Se llama una sola vez para reproducir todos
    # los instrumentos simultaneamente.
    Play.midi(cancion)


def main():
    playSong()



main()