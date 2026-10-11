matriz = [[1,7,8],[3,5,2],[4,2,3]]


#Matriz
print("Matriz:")
for i in range(len(matriz)):
    for j in range(len(matriz[i])):
        print(matriz[i][j], end=" ")
    print(" ")  


#Diagonal
def diagonal(matriz):
    if len(matriz) != len(matriz[0]):
        print("No tiene diagonal") 
    else:
        for i in range(len(matriz)):
            print(matriz[i][i], end=" ")
            print("")
print("Matriz Diagonal:")
diagonal(matriz)


#Matriz traspuesta
print("Matriz traspuesta:")
colum = 0
while colum < len(matriz[0]):
    for i in range(len(matriz)):
        print(matriz[i][colum], end=" ")
    print("")
    colum += 1


print("Multiplicacion de matrices")
matrizMulti1 = [[4,7],[4,0]]
matrizMulti2 = [[0,1],[8,1]]

def fila_nula(n):
    return [0] * n

#Matriz nula
def matrizNula(filas, columnas):
    matriz = []
    for i in range(filas):
        matriz.append(fila_nula(columnas))
    return matriz

def multiplicacion_mat(matrizMulti1, matrizMulti2):
    f_m1 = len(matrizMulti1)
    c_m1 = len(matrizMulti1[0])
    f_m2 = len(matrizMulti2)
    c_m2 = len(matrizMulti2[0])
    res = matrizNula(c_m1, f_m2)
    for i in range(f_m1):
        for j in range(c_m2):
            for k in range(f_m2):
                res[i][j] += matrizMulti1[i][k] * matrizMulti2[k][j]
    return res

print(multiplicacion_mat(matrizMulti1, matrizMulti2))
