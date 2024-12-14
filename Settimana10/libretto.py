"""
Scrivere un programma python che permetta di gestire un libretto universitario
Il programma dovrà definire una classe Voto  che rappresenta il singolo esame superato ed una classe libretto
che contiene l'elenco dei voti di uno studente
"""


class Voto:
    def __init__(self, esame, cfu, punteggio, data, lode):
        self.esame = esame
        self.punteggio = punteggio
        self.cfu = cfu
        self.data = data
        self.lode = lode

        if self.lode and self.punteggio != 30:
            raise ValueError("la lode non è applicabile ad un voto inferiore di 30")

    def __str__(self):  # tipo il tostring metodi DUNDER
        return f"Esame: {self.esame}, superato con: {self.punteggio}"

    def __repr__(self): # tipo il tostring metodi DUNDER ma per il programmatore
        return f"Voto('{self.esame}',{self.cfu},{self.punteggio},'{self.data}','{self.lode}'"


class Libretto:
    def __init__(self):
        self._voti = []  # non ho nessun voto all'inizio, mettendo _ prima del nome dell'attributo sto dicendo per convenzione di un accederci direttamente

    def append(self,voto):
        self._voti.append(voto)

    def media_voti(self):
        if len(self._voti)  == 0:
            raise ValueError("Elenco voti vuoto")
        punteggi = [v.punteggio for v in self._voti]
        return sum(punteggi)/len(punteggi)





mio_libretto = Libretto()



voto_1 = Voto("Analisi Matematica 1", 10, 28, '2022-02-10', False)
voto_2 = Voto("Analisi Matematica 2", 12, 30, '2022-02-10', True)

mio_libretto.append(voto_1)
mio_libretto.append(voto_2)

print(f'La media dei voti è: {mio_libretto.media_voti()}')

#print(voto_1,voto_2)

#miei_voti = [voto_1,voto_2]
#print(miei_voti)



