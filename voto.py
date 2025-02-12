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


