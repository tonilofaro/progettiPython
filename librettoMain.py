from voto import Voto
from voto import Libretto

voto_1 = Voto("Analisi Matematica", 10, 28, False, '2022-02-10')
voto_2 = Voto("Basi di dati", 8, 30, True, '2023-05-15')

libretto = Libretto()
libretto.append(voto_1)
libretto.append(voto_2)

print(libretto.media())