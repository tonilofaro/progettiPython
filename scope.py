x = 300
y = 100
def gunzo():
    print(x)
    global y # fa riferimento alla y globale che sta fuori
    print(y)

gunzo()
print(y)
