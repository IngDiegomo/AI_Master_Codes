tablero_virtual = [
    [0, 1, 2, 0],
    [1, 1, 2, 0],
    [0, 1, 2, 0],
]

tablero_visto_por_camara = [
    [0, 0, 2, 0],
    [0, 0, 2, 0],
    [0, 0, 0, 2],   
]


for i in range(0,len(tablero_virtual)):
    for j in range(0,len(tablero_virtual[0])):
       
        if ((tablero_virtual[i][j] == 0) and  (tablero_visto_por_camara[i][j] == 2)):
            tablero_virtual[i][j] = 2
        elif ((tablero_virtual[i][j] == 2) and  (tablero_visto_por_camara[i][j] == 0)):
            tablero_virtual[i][j] = 0

print(tablero_virtual)