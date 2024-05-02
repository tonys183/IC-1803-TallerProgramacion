#Ejercicio 1
def esPrimo(num):
    if num  <= 2:
        return num == 2
    i = 2
    while(i*i <= num):
        if num % i == 0:
            return False
        i += 1
    return True

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
def short(lista):
    min = lista[0][1]
    for i in range(len(lista)):
        if lista[0][i] > min:
            min = lista[0][i]
        

def ordenar(nombres, edad):
    listaOrig = []
    for i in range(len(nombres)):
        listaOrig.append((nombres[i], edad[i]))
    short(listaOrig)



        

print(ordenar(["A", "B", "C", "D"], [21,37,17,23]))