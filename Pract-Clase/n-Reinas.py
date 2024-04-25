matriz = [
    ["R", ".", ".", "."],
    [".", "R", ".", "."],
    [".", ".", ".", "."],
    [".", ".", ".", "."]
    ]

def esValido(matriz):
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            if matriz[i][j] == "R":
                #diagonales
                    
                for c in range(len(matriz[0])): #Recorrer cada columna
                    if matriz[i][c] == "R" and (i,c) != (i,j):
                        return False
                for f in range(len(matriz)): #Recorrer cada fila
                    if matriz[f][j] == "R" and (f,j) != (i,j):
                        return False
    return True

print(esValido(matriz))
"""
def esSolucion(matriz):
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            matriz[i][j] = "R"
            if not esValido(matriz):
                matriz[i][j] = "."

    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            print(matriz[i][j], end=" ")
        print(" ") 
         
esSolucion(matriz)
"""

def posiblesCombina(matriz):
    return