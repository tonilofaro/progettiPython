import numpy as np

arr = np.array([1,2,3,4,5])
lista = [1,2,3,4,5]

print(arr) # stampa senza le virgole [1 2 3 4 5] sono più veloci
print(lista) # stampa [1, 2, 3, 4, 5]

# altra differenza qui:
print(lista * 5) # duplica gli elementi 5 volte [1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5]
print(arr * 5) # moltiplica gli ementi per 5  [ 5 10 15 20 25]

# creare gli array di diverse dimensioni
arr0 = np.array(42)  # scalar array di 0 dimensioni
print(arr0)
arr2D = np.array([[1,2,3,4,5],
                  [1,2,3,8,5]]) # array di array ( matrice)
print(arr2D)

arr3D = np.array([[[1,2,3,4,5],
                  [4,5,6,7,8]],
                 [[2,3,4,5,6],
                  [4,3,4,52,2]]])
print(arr3D)

print(arr.ndim) # mi resituisce il numero di dimensioni dell'array
print(arr0.ndim)
print(arr3D.ndim)

arr5D = np.array([1,2,3],ndmin=5) # creo un array di 5 dimensioni
print(arr5D)

arrArange = np.arange(5,50,5) # genera un array partendo da 5 arrivando a 50 facendo uno step ogni 5
print(arrArange)

arrZeros = np.zeros(5) # creo un array di zeri di dimensione che decido io in questo caso 5
print(arrZeros)

arrzeros3D = np.zeros((3,2,4)) # la prima dimensione deve contenere tre elementi, la seconda due elementi e la terza(piu interna) 4 elementi
print(arrzeros3D)

arrOnes = np.ones((3,2,1)) # array di soli 1
print(arrOnes)

print(arr[2]) # prendo il terzo alemento del mio array
print(arr2D[1,3]) # prendo il secondo array piu esterno e il quarto elemento
print(arr3D[1,1,3]) # voglio il 52 quindi prendo secondo array più esterno, secondo piu interno e 4 elemento
print(arr[-1]) # prende il 5 l'ultimo elemento fa lunghezza totale - 1 quindi prende il quarto elmento

print(arr3D[-1,-1,-2]) # prendo il 52 ma partendo dagli indici negativi




