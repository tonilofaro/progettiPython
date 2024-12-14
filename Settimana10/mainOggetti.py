class Persona:
    # costruttore
    def __init__(self, nome, cognome):
        self.nome = nome
        self.cognome = cognome

    def saluta(self):
        print("ciao sono: "+self.nome+" "+self.cognome)

class Insegnante(Persona):  # ereditarietà

    def __init__(self,nome,cognome,ruolo):   # il costruttore viene sovrascritto
        super().__init__(nome,cognome)  # richiama il costruttore della sovraclasse
        self.ruolo = ruolo

    def saluta(self):
        print("ciao sono " + self.nome + " " + self.cognome + " e sono insegnante di "+self.ruolo)







def main():
    # istanza dell'oggetto
    persona1 = Persona("Mario", "rossi")
    print(persona1.nome)
    print(persona1.cognome)
    persona2 = Persona("ugo", "Bianchi")
    persona2.nome
    persona2.cognome

    persona1.saluta()
    persona2.saluta()
    # per la modifica
    persona2.nome = "Gesù"
    print(persona2.saluta())
    # eliminare oggetto o attributo
    del persona1.nome
    insegnate1 = Insegnante("Andrea", "Villano","Matematica")  # insegnante eredità da Persona
    print(insegnate1.nome)
    insegnate1.saluta()

main()
