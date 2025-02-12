ok = False
while not ok:
    try:
        n = int(input("dato: "))
        ok = True
    except  ValueError:
        print("dato non valido")

print("fine programma")



