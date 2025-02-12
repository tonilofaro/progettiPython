def leggi(messaggio, valore_min=1, valore_max=10):
    """
    leggi un valore intero nell'intervallo specificato. Se il valore non ricade nell'intervallo
    viene richiesto ripetutamente il rienserimento

    :param messaggio: messaggio da stampare con invito al rienserimento
    :param valore_min: valore minimo accettabile intero
    :param valore_max: valore massimo accettabile intero
    :return: valore inserito dall'utente che è garantito essere nell'intervallo richiesto
    """
    riga = input(messaggio).strip()

    while riga == '' or int(riga) < valore_min or int(riga) > valore_max:
        print(f"valore errato deve essere compreso tra {valore_min} e {valore_max} ")
        riga = input(messaggio).strip()
    return int(riga)

giorno = leggi('Giorno: ', 0, 10)
print(giorno)
voto = leggi("voti: ", 18, 30)
print(voto)
