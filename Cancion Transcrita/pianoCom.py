from music import *


class Piano(object):

    def __init__(self, tempo=120, repeticion_compases=True):
        self.nombre = "Piano"
        self.instrumento = 0  # Acoustic Grand Piano
        self.canal = 2
        self.tempo = tempo
        self.repeticion_compases = repeticion_compases


    def crear_frases(self):

        frase_derecha = Phrase(0.0)
        frase_izquierda = Phrase(0.0)



        notas_derecha = []
        duraciones_derecha = []

        notas_izquierda = []
        duraciones_izquierda = []


        # compas 1 ============================================================


        # MANO DERECHA
        


        notas_derecha.append(B3)
        duraciones_derecha.append(QN)


        notas_derecha.append(D4)
        duraciones_derecha.append(QN)
        notas_derecha.append(B4)
        duraciones_derecha.append(QN)

        notas_derecha.append(FS4)
        duraciones_derecha.append(EN)

        notas_derecha.append(GS4)
        duraciones_derecha.append(QN)

        notas_derecha.append(E4)
        duraciones_derecha.append(EN)
        notas_derecha.append(E4)
        duraciones_derecha.append(EN)
        notas_derecha.append(E4)
        duraciones_derecha.append(QN)

        

        # MANO IZQUIERDA

        notas_izquierda.append(E3)
        duraciones_izquierda.append(HN)

        notas_izquierda.append(E2)
        duraciones_izquierda.append(HN)


        # compas 2 ============================================================


        # # MANO DERECHA


        notas_derecha.append(DS4)
        duraciones_derecha.append(EN)
         
        notas_derecha.append(DS4)
        duraciones_derecha.append(EN)
        
        notas_derecha.append(FS4)
        duraciones_derecha.append(EN)
        
        notas_derecha.append(CS4)
        duraciones_derecha.append(EN)
        
        notas_derecha.append(DS4)
        duraciones_derecha.append(EN)
        notas_derecha.append(CS4)
        duraciones_derecha.append(EN)
        notas_derecha.append(DS4)
        duraciones_derecha.append(EN)
        notas_derecha.append(E4)
        duraciones_derecha.append(QN)
        
        #notas_derecha.append(D4)
        #duraciones_derecha.append(EN)

        # notas_derecha.append(A4)
        # duraciones_derecha.append(QN)

        # notas_derecha.append(A3)
        # duraciones_derecha.append(EN)

        

        # notas_derecha.append(E4)
        # duraciones_derecha.append(QN)







        # # MANO IZQUIERDA

        #notas_izquierda.append(DS4)
        #duraciones_izquierda.append(EN)

        # notas_izquierda.append(A2)
        # duraciones_izquierda.append(HN)
        #notas_izquierda.append(DS4)
        notas_izquierda.append(E3)
        duraciones_izquierda.append(HN)

        notas_izquierda.append(E2)
        duraciones_izquierda.append(HN)



        # compas 3 ============================================================
         
        # # Mano derecha
        notas_derecha.append(DS4)
        duraciones_derecha.append(EN)
        notas_derecha.append(CS4)
        duraciones_derecha.append(EN)
        notas_derecha.append(DS4)
        duraciones_derecha.append(EN)
        notas_derecha.append(E4)
        duraciones_derecha.append(QN)
        
        notas_derecha.append(CS4)
        duraciones_derecha.append(EN)
        
        notas_derecha.append(FS4)
        duraciones_derecha.append(EN)
        
             
        #notas_derecha.append(DS4)
        #duraciones_derecha.append(EN)
         
        #notas_derecha.append(DS4)
        #duraciones_derecha.append(EN)
        
        notas_derecha.append(DS4)
        duraciones_derecha.append(HN)
        
        


        # # Mano izquierda

        # notas_izquierda.append(E3)
        # duraciones_izquierda.append(HN)

        # notas_izquierda.append(B2)
        # duraciones_izquierda.append(HN)
        notas_izquierda.append(E3)
        duraciones_izquierda.append(HN)

        notas_izquierda.append(E2)
        duraciones_izquierda.append(HN)


        # compas 4 ============================================================


        # # Mano derecha
        notas_derecha.append(B3)
        duraciones_derecha.append(QN)


        notas_derecha.append(D4)
        duraciones_derecha.append(QN)
        notas_derecha.append(B4)
        duraciones_derecha.append(QN)

        notas_derecha.append(FS4)
        duraciones_derecha.append(EN)

        notas_derecha.append(GS4)
        duraciones_derecha.append(QN)

        #notas_derecha.append(E4)
        #duraciones_derecha.append(EN)
        notas_derecha.append(E4)
        duraciones_derecha.append(EN)
        notas_derecha.append(E4)
        duraciones_derecha.append(HN)

       

        # # Mano izquierda

        notas_izquierda.append(E3)
        duraciones_izquierda.append(HN)

        notas_izquierda.append(E2)
        duraciones_izquierda.append(HN)



        if len(notas_derecha) != len(duraciones_derecha):
            raise ValueError(
                "La mano derecha debe tener la misma cantidad "
                "de notas y duraciones"
            )

        if len(notas_izquierda) != len(duraciones_izquierda):
            raise ValueError(
                "La mano izquierda debe tener la misma cantidad "
                "de notas y duraciones"
            )



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



piano = Piano(
    tempo=120,
    repeticion_compases=True
)

score = Score("Bitter Symphony")

score.setTempo(
    piano.tempo
)

score.addPart(
    piano.crear_parte()
)

Play.midi(score)

#Write.midi(score, "piano_bs.mid")
#print("Se creo .mid")