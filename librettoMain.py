from voto import Voto
from voto import Libretto

voto_1 = Voto("Analisi Matematica", 10, 25, False, '2022-02-10')
voto_2 = Voto("Basi di dati", 8, 30, False, '2023-05-15')

libretto = Libretto()
libretto.append(voto_1)
libretto.append(voto_2)
libretto.append(Voto("Fisica 1",10,21,False,'2023-03-16'))
libretto.append(Voto('Fisica 2', 8, 30, True, '2023-07-08'))
libretto.append(Voto("Fisica 3",10,30,True,'2023-06-18'))

libretto.findByPunti(25,False)

print(libretto.media())

voti30 = libretto.findByPunti(30,True)

voti25 = libretto.findByPunti(25,False)

voti24 = libretto.findByPunti(24,False)

# poi posso stampare le varie liste

for v in voti30:
    print(v.esame)

voto_fisica2 = libretto.findByEsame("Fisica 2")
if voto_fisica2 is not None:
    print(f"Hai preso {voto_fisica2.str_punteggio()}")
else:
    print("nessun voto trovato")


nuovoVoto = Voto("Basi di dati", 8, 30, False, '2023-05-16')

print(libretto.has_voto(nuovoVoto))

try:
    voto_2 = libretto.findByEsame2("Fisica 4")
    print(f"Hai preso {voto_2.str_punteggio()}")
except ValueError:
    print("nessun voto trovato")
