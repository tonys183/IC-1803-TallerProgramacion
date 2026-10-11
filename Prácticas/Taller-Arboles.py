#1
def mayorArbol(arbol):
    if arbol == []:
        return -1 << 31
    return max([arbol[0], mayorArbol(arbol[1]), mayorArbol(arbol[2])])

def menorArbol(arbol):
    if arbol == []:
        return 1 << 31
    return min([arbol[0], menorArbol(arbol[1]), menorArbol(arbol[2])])


'''
#Sencillo
def mayorArbol(arbol):
    if arbol[1] == []:
        return arbol[0]
    return mayorArbol(arbol[1])

def menorArbol(arbol):
    if arbol[2] == []:
        return arbol[0]
    return menorArbol(arbol[2])
'''

def sumaArbol(arbol):
    return mayorArbol(arbol) + menorArbol(arbol)

arbol = [10, [9, [8, [7, [], []], []], []], [11, [], []]]
print(sumaArbol(arbol))

#2
def buscarValor(arbol, valor):
    if arbol == []:
        return []
    if arbol[0] == valor:
        return arbol
    izq = buscarValor(arbol[1], valor)
    dere = buscarValor(arbol[2], valor)
    return izq + dere

arbol = [5, [12, [17, [3, [], []], []], [13, [], []]], [8, [], []]]
print(buscarValor(arbol, 17))

#3
def invArbol(arbol):
    arbol[1], arbol[2] = arbol[2], arbol[1]
    return arbol

arbol = [10, [9, [8, [7, [], []], []], []], [11, [], []]]
print(invArbol(arbol))

#4
def mediaArbol(arbol):
    return