from dataclasses import dataclass

@dataclass
class Voto:
    esame: str
    cfu: int
    punteggio: int
    lode: bool
    data: str

    def str_punteggio(self):
        if self.punteggio == 30 and self.lode:
            return "30 e lode"
        else:
            return f"{self.punteggio}"

class Libretto:
    def __init__(self):
        self._voti = []

    def append(self,voto):
        if self.has_voto(voto) == False and self.has_conflitto(voto) == False:
            self._voti.append(voto)
        else:
            raise ValueError("Voto non valido")


    def media(self):
        if len(self._voti) == 0:
            raise ValueError("elenco voti vuoto")
        punteggi = [v.punteggio for v in self._voti]
        return sum(punteggi)/len(punteggi)

    def findByPunti(self, punteggio,lode):
        corsi = []
        for v in self._voti:
            if v.punteggio == punteggio and v.lode == lode:
                corsi.append(v)
        return corsi

    def findByEsame(self,esame):
        for v in self._voti:
            if v.esame == esame:
                return v
        return None

    def findByEsame2(self,esame):

        for v in self._voti:
            if v.esame == esame:
                return v
        raise ValueError(f"Esame '{esame}' non presente nel libretto")

    def has_voto(self,voto):
        for v in self._voti:
            if v.esame == voto.esame and v.punteggio == voto.punteggio and v.lode == voto.lode:
                return True
        return False

    def has_conflitto(self,voto):
        for v in self._voti:
            if v.esame == voto.esame and not (v.punteggio == voto.punteggio and v.lode == voto.lode):
                return True
        return False


#tipicamente si fa:
# se il programma viene eseguito direttamente
def _test_voto():
    print(__name__)  # se eseguito dentro voto assume il valore __main__ se eseguito da dove importo assume il valore voto del modulo
    v1 = Voto("nome esame", 10, 18, False, "2025-02-12")
    l1 = Libretto()
    l1.append(v1)
    print(l1.media())


if __name__ == "__main__":
    _test_voto()


