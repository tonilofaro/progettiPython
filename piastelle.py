# dati in ingresso:
# lunghezza del muro [LUN]
# lunghezza lato della piastrella (LATO)
# informazioni sui vincoli di posizionamento

# dati in uscita:
# numero di [N] (num_nere)
# numero di [B] (num_bianche)
# lunghezza dello spazio 's' ai margini  (spazio)

# strategia di risoluzione

# LUN / LATO
# spazio = (LUN - LATO * (num_bianche * num_nere)) / 2
# metto una piastrella nera e poi mi chiedo quante coppie bianco e nera ci stanno nella rimanente lunghezza?

# num_coppie = int((LUN - LATO) / (2 * LATO) )
# num_bianche = num_coppie
# num_nere = num_coppie + 1
LUN = 380  # cm
LATO = 25  # cm
num_coppie = int((LUN - LATO) / (2 * LATO))
num_bianche = num_coppie
num_nere = num_coppie + 1
spazio = (LUN - LATO * (num_bianche + num_nere)) / 2
print("posare", num_nere, "piastrelle nere e", num_bianche, "piastrelle bianche e lasciando uno spazio di", spazio,
      "cm")

# verificare che la lunghezza del muro sia >= lato


