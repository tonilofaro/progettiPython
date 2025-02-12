def fai_la_pasta():
    print("metti l'acqua")
    print("fai bollire")
    print("metti la pasta")

fai_la_pasta()

def fai_la_pasta_2(tipo_pasta = "penne",metti_sugo= False):
    print("metti l'acqua")
    print("fai bollire")
    print(f"metti {tipo_pasta}")
    if metti_sugo:
        print("metti sugo")

fai_la_pasta_2("fusilli",True)
fai_la_pasta_2("spaghetti")
fai_la_pasta_2()

def funzione3(*opzioni): # parametri arbitrari
    print("metti l'acqua")
    print("fai bollire")
    print(f"metti {opzioni[0]}")
    if opzioni[1]:
        print("metti il sugo")

funzione3("gli spaghetti",False)
funzione3("i fusilli",True)

def fai_la_pasta_3(tipo_pasta,metti_sugo):
    print("metti l'acqua")
    print("fai bollire")
    print(f"metti {tipo_pasta}")
    if metti_sugo:
        print("metti sugo")

fai_la_pasta_3(tipo_pasta="fusilli",metti_sugo=True)

def somma(num1,num2):
    return num1 + num2

risultato = somma(2,3)
print(risultato)