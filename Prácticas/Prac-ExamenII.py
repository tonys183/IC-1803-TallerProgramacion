#Ejercicio 1
def criba(n):
    primos = [0] + [1] * (n+1)
    p = 2
    while (p * p <= n):
        if (primos[p] == 1):
            for i in range(p * p, n+1, p):
                primos[i] = 0
        p += 1
    return primos

def esPrimo(n):
    tablero = criba(n)
    if tablero[n] == 1:
        return True
    return False

print(esPrimo(4))

def diff(a,b):
    return a == b and esPrimo(a)

def relacion(A, B, func):
    matriz=[]
    for i in A:
        for j in B:
            if func(i,j):
                matriz.append((i,j))
    return matriz

print(relacion([1,3,5,7,92,88], [1,2,7,42], diff))







#Ejercicio 2
# def ordenar(nombres, edad):
#     for i in range(len(nombres)):
#         for j in range(i+1, len(nombres)):
#             if edad[i] > edad[j]:
#                 edad[i], edad[j] = edad[j], edad[i]
#                 nombres[i], nombres[j] = nombres[j], nombres[i]
            
#             elif edad[i] == edad[j]:
#                 if str(nombres[i]) < str(nombres[j]):
#                     nombres[i], nombres[j] = nombres[j], nombres[i]
#     return nombres
    
# print(ordenar(["A", "B", "C", "D", "E"], [21,37,17,21,21]))

def comprimir(a,b):
    newLista = []
    for i in range(len(a)):
        newLista.append((a[i], b[i]))
    return newLista

def descomprimir(lista):
    res = []
    for i in lista:
        res.append(i[0])
    return res

def orden(a,b):
    if a[1] == b[1]:
        return a[0] > b[0]
    return a[1] < b[1]

def qs(lista):
    if len(lista) == 0:
        return []
    pivot = lista[0]
    menores = []
    mayores = []
    for i in range(1, len(lista)):
        if orden(lista[i], pivot):
            menores.append(lista[i])
        else:
            mayores.append(lista[i])
    return qs(menores) + [pivot] + qs(mayores)

def miOrden(a,b):
    listaCompress = comprimir(a,b)
    ordenado = qs(listaCompress)
    return descomprimir(ordenado)


print(miOrden(["A", "T", "Z"], [23,99,99]))







#Ejercicio 3
def filaNula(largo):
    return [0] * largo

def matrizNula(filas, columnas):
    matriz = []
    for i in range(filas):
        matriz.append(filaNula(columnas))
    return matriz

def identidad(n):
    matrizIden = matrizNula(n,n)
    for i in range(n):
        matrizIden[i][i] = 1
    return matrizIden


#Estudiar ---------
def multiplicar(matriz1, matriz2):
    filas1 = len(matriz1)
    columnas1 = len(matriz1[0])
    columnas2 = len(matriz2[0])
    result = matrizNula(filas1, columnas2)
    for i in range(filas1):
        for j in range(columnas2):
            for k in range(columnas1):
                result[i][j] += matriz1[i][k] * matriz2[k][j] 
    return result

def expoLogMatri(matriz, n):
    if n == 0:
        return identidad(len(matriz))
    matExpo = expoLogMatri(matriz, n // 2)
    res = multiplicar(matExpo, matExpo)
    if n % 2 == 1:
        return multiplicar(res, matriz)
    return res
    
def func(n):
    matriz = [
        [0,1,0,0,0],
        [0,0,1,0,0],
        [0,0,0,1,0],
        [0,0,0,0,1],
        [-2,0,5,0,7]
        ]
    casos = [[0],[1],[10],[15],[20]]
    matrizExpo = expoLogMatri(matriz, n)
    res = multiplicar(matrizExpo, casos) 
    return res[0][0]

print(func(1))
print(func(2))
print(func(3))
print(func(4))
print(func(5))





#Ejercicio 4
def matAcumulada(matriz):
    n, m =  len(matriz), len(matriz[0])
    acum = matrizNula(n+1,m+1)
    for i in range(1, n+1):
        for j in range(1, m+1):
            acum[i][j] = matriz[i-1][j-1] + acum[i-1][j] + acum[i][j-1] - acum[i-1][j-1]
    return acum

def rangeQuery(matriz, fila1, col1, fila2, col2):
    return matriz[fila2 + 1][col2 + 1] - matriz[fila1][col2 + 1] - matriz[fila2 + 1][col1] + matriz[fila1][col1]

def maxi(valor1, valor2):
    if valor1 > valor2:
        return valor1
    return valor2

def maxpar(matriz):
    acum = matAcumulada(matriz)
    n, m = len(matriz), len(matriz[0])
    res = -1
    for i in range(n-1):
        for j in range(m-1):
            acumLocal = rangeQuery(acum, i, j, i+1, j+1)
            if not acumLocal % 2:
                res = maxi(res, acumLocal)
    return res

print(maxpar([
    [1,1,1,1],
    [1,1,1,1],
    [1,1,1,1],
    [1,1,1,1]]
))





#Ejercicio 5
direcciones = [[2, 1],[1,2],[-1,2],[-2,1],[-2,-1],[-1,-2],[1,-2],[2,-1]]

def esValido(i, j, matriz):
    return 0 <= i < len(matriz) and 0 <= j < len(matriz[0])

def esSolucion(tablero):
    for i in range(len(tablero)):
        for j in range(len(tablero[0])):
            if tablero[i][j] != "C":
                return False
    return True

def ubicarCaballo(tablero, pos):
    for i in range(len(tablero)):
        for j in range(len(tablero[0])):
            if (i, j) == pos:
                tablero[i][j] = "C"
                return tablero

def caballo(tablero, pos, direcciones):
    if esValido(pos[0], pos[1], tablero):
        visitados = []
        tablero = ubicarCaballo(tablero, pos)
        pila = [pos]
        while pila:
            i, j = pila.pop()
            if esSolucion(tablero):
                return tablero
            if (i, j) not in visitados:
                visitados.append((i, j))
                for di, dj in direcciones:
                    if esValido(i + di, j + dj, tablero) and tablero[i + di][j + dj] != "C":
                        tablero[i + di][j + dj] = "C"
                        pila.append([i + di, j + dj])
        return False
    return False


print(caballo(
    [
    [0,0,0,0],
    [0,0,0,0],
    [0,0,0,0],
    [0,0,0,0]], (0,0), direcciones))

[
    ["C",0,0,0],
    [0,0,"C",0],
    [0,"C",0,0],
    [0,"C",0,"C"]]
