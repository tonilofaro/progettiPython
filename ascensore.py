piano = int(input("A quale piano vuoi andare? "))
if piano != 13:
    if piano < 13:
        # piano basso
        piano_vero = piano
    else:
        # piano alto
        piano_vero = piano - 1
    print("Hai chiesto di andare al", piano, "piano")
    print("In realtà si tratta del piano \"vero\"", piano_vero)
else:
    print("vai viaa che ci sono i fantasmiii!!!")