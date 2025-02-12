from dataclasses import dataclass


@dataclass
class Voto:
    esame: str
    cfu: int
    punteggio: int
    lode: bool
    data: str

class Libretto:
    def __init__(self):
        self._voti = []

    def append(self,voto):
        self._voti.append(voto)

    def media(self):
        if len(self._voti) == 0:
            raise ValueError("elenco voti vuoto")
        punteggi = [v.punteggio for v in self._voti]
        return sum(punteggi)/len(punteggi)


voto_1 = Voto("Analisi Matematica",10,28,False,'2022-02-10')
voto_2 = Voto("Basi di dati",8,30,True,'2023-05-15')

libretto = Libretto()
libretto.append(voto_1)
libretto.append(voto_2)

