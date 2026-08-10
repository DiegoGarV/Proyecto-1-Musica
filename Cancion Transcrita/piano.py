from music import *


class Piano(object):

    def __init__(self, tempo=120, repeticion_compases=True):
        self.nombre = "Piano"
        # Acoustic Grand Piano
        self.instrumento = 0
        self.canal = 2
        self.tempo = tempo
        self.repeticion_compases = True  


    def agregar_ciclos(
            self, 
            cantidad, 
            notas_derecha, duraciones_derecha,
            notas_izquierda, duraciones_izquierda
    ):
        """
        Agrega el patron:
        | E - Bm | D - A |
        """

        # compas 1 : E -BM 
        medida_e_bm_derecha=[
                                E4, GS4, B4,
                                B3, D4, FS4
                            ]

        medida_e_bm_duraciones = [
                                    EN, EN, QN,
                                    EN, EN, QN
                                ]

        medida_e_bm_izquierda = [E3, B2]
        
        medida_e_bm_izquierda_duraciones = [HN, HN]


        # compas 2 : D - A
        medida_d_a_derecha = [
                                D4, FS4, A4,
                                A3, CS4, E4
                            ]
        
        medida_d_a_duraciones = [
                                    EN, EN, QN,
                                    EN, EN, QN
                                ]

        medida_d_a_izquierda = [D3, A2]

        medida_d_a_izquierda_duraciones = [HN, HN]

        
        for _ in range(cantidad):
            # Agregar compas E - Bm
            notas_derecha.extend(
                medida_e_bm_derecha
            )

            duraciones_derecha.extend(
                medida_e_bm_duraciones
            )

            notas_izquierda.extend(
                medida_e_bm_izquierda
            )

            duraciones_izquierda.extend(
                medida_e_bm_izquierda_duraciones
            )

            # Agregar compas D - A
            notas_derecha.extend(
                medida_d_a_derecha
            )

            duraciones_derecha.extend(
                medida_d_a_duraciones
            )

            notas_izquierda.extend(
                medida_d_a_izquierda
            )

            duraciones_izquierda.extend(
                medida_d_a_izquierda_duraciones
            )


    def crear_frases(self):
        frase_derecha = Phrase(0.0)
        frase_izquierda = Phrase(0.0)

        notas_derecha = []
        duraciones_derecha = []

        notas_izquierda = []
        duraciones_izquierda = []


        # 4 compases = 2 ciclos de E - Bm | D - A
        self.agregar_ciclos(
            2, 
            notas_derecha, duraciones_derecha,
            notas_izquierda, duraciones_izquierda
        )

        # 56 compases = 28 ciclos de E - Bm | D - A
        self.agregar_ciclos(
            28, 
            notas_derecha, duraciones_derecha,
            notas_izquierda, duraciones_izquierda
        )


        if self.repeticion_compases:
            self.agregar_ciclos(
                28, 
                notas_derecha, duraciones_derecha,
                notas_izquierda, duraciones_izquierda
            )


        self.agregar_ciclos(
            4,
            notas_derecha, duraciones_derecha,
            notas_izquierda, duraciones_izquierda
        )

        if len(notas_derecha) != len(duraciones_derecha):
            raise ValueError("la mano derecha debe tener la misma cantidad de notas y duraciones")

        if len(notas_izquierda) != len(duraciones_izquierda):
            raise ValueError("la mano izquierda debe tener la misma cantidad de notas y duraciones")


        frase_derecha.addNoteList(
            notas_derecha,
            duraciones_derecha
        )

        frase_izquierda.addNoteList(
            notas_izquierda,
            duraciones_izquierda
        )

        return frase_derecha, frase_izquierda



    def crear_parte(self):
        parte = Part(
            self.nombre,
            self.instrumento,
            self.canal
        )

        frase_derecha, frase_izquierda = self.crear_frases()
        parte.addPhrase(frase_derecha)
        parte.addPhrase(frase_izquierda)

        return parte

# piano = Piano(
#     tempo=120,
#     repeticion_compases=True
# )

# score = Score("Bitter Sweet Symphony")
# score.setTempo(piano.tempo)
# score.addPart(piano.crear_parte())

# Play.midi(score)
# Write.midi(score, "piano_bss.mid")
# print("Se creo .mid")