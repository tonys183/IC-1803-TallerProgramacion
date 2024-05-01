bM = [[1,1],[1,0],[0,1],[-1,1],[1,-1],[0,-1],[-1,0],[-1,-1]]

def newBodega(matriz):
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):

            if matriz[i][j] == "<":
                for k in range(j, -1, -1):
                    if matriz[i][k] == "X":
                        break
                    if matriz[i][k] == ".":
                        matriz[i][k] = "<"
                    if matriz[i][k] == "B":
                        return False
            
            if matriz[i][j] == ">":
                for k in range(j, len(matriz[0])):
                    if matriz[i][k] == "X":
                        break
                    if matriz[i][k] == ".":
                        matriz[i][k] = ">"
                    if matriz[i][k] == "B":
                        return False

            if matriz[i][j] == "^":
                for k in range(i, -1, -1):
                    if matriz[k][j] == "X":
                        break
                    if matriz[k][j] == ".":
                        matriz[k][j] = "^"
                    if matriz[i][k] == "B":
                        return False

            if matriz[i][j] == "v":
                for k in range(len(matriz)):
                    if matriz[k][j] == "X":
                        break
                    if matriz[k][j] == ".":
                        matriz[k][j] = "v"
                    if matriz[i][k] == "B":
                        return False
    return matriz 

def ubicarBatman(matriz):
    pos = []
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            if matriz[i][j] == "B":
                pos = [i,j]
    return pos

def esValido(i, j, matriz):
    return 0 <= i < len(matriz) and 0 <= j < len(matriz[0])


def batman(matriz):
    pila = [ubicarBatman(matriz)]
    while pila:
        i, j = pila.pop()
        if not (i + j):
            return True
        for di, dj in bM:
            if esValido(i + di, j + dj, matriz) and matriz[i + di][j + dj] == ".":
                matriz[i + di][j + dj] = "B"
                pila.append([i + di, j + dj])
    return False


def main():
    bodega = [
        [".",".",".",".",".",".","."],
        [".",".",".",".",".","B","X"],
        [".",".",".",".",".",".","."]]
    
    if not newBodega(bodega):
        print(newBodega(bodega))
    else:
        print(batman(newBodega(bodega)))

if __name__ == '__main__':
    main()