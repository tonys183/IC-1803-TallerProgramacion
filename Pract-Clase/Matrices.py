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

if len(matrizMulti1[0]) == len(matrizMulti2):
    fila = 0
    while fila < len(matrizMulti2[0]):
        for i in range(len(matrizMulti1)):
           x = matrizMulti1[fila][i] * matrizMulti2[i][fila]
           print(x)
        fila +=1
    
