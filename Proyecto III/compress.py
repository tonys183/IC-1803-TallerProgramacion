from collections import deque
import sys
import bitarray as bit
import os
import time

def frecuencias(fileR):
    freq = {}
    for char in fileR:
            if char == '\n':
                char = '|'
            if char in freq:
                freq[char] += 1
            else:
                freq[char] = 1
    dicti = sorted(freq.items())
    return dicti

def ordenarFrencuencia(item):
    return item[0]

def nodosHuffman(diccionario):
    nodos = []
    for char, valor in diccionario:
        nodos.append((valor, char))
    return nodos

def crearArbolHuff(nodos):
	while len(nodos) > 1:
		nodos = sorted(nodos, key=ordenarFrencuencia)
		izq = nodos.pop(0)
		der = nodos.pop(0)
		NovoNodo = (izq[0] + der[0], [izq,der])
		nodos.append(NovoNodo)
	return nodos[0]

def BinarioArbol(arbHuff, dire='',binario={}):
	if isinstance(arbHuff[1],str):
		binario[arbHuff[1]]=dire
	else:
		BinarioArbol(arbHuff[1][0],dire+'0',binario)
		BinarioArbol(arbHuff[1][1],dire+'1',binario)
	return binario

def comprimirTexto(file,binario):
    text=''
    for char in file:
        if char == '\n':
            char = '|'
        text += binario[char] 
    return text

def alturaArbol(arbHuff):
    if isinstance(arbHuff[1], str):
        return 0
    else:
        return 1 + max(alturaArbol(arbHuff[1][0]), alturaArbol(arbHuff[1][1]))

def anchuraArbol(arbHuff):
    if isinstance(arbHuff[1], str):
        return 1
    cola = deque([arbHuff])
    maxAncho = 0
    while cola:
        ancho = len(cola)
        if ancho > maxAncho:
            maxAncho = ancho
        for _ in range(ancho):
            node = cola.popleft()
            if not isinstance(node[1], str):
                cola.append(node[1][0])
                cola.append(node[1][1])
    return maxAncho

def nodosPorNivel(arbHuff):
    levels = {}
    cola = deque([(arbHuff, 0)])
    while cola:
        node, level = cola.popleft()
        if level not in levels:
            levels[level] = 0
        levels[level] += 1
        if not isinstance(node[1], str):
            cola.append((node[1][0], level + 1))
            cola.append((node[1][1], level + 1))
    return levels

def main():
    if len(sys.argv) != 2:
        print("Uso: python3 compresor.py archivo.txt")
        sys.exit(1)

    archivo = sys.argv[1]
    with open(archivo, "r") as file:
        fileR = file.read()

    start = time.time()
    frecuenciasOrig = frecuencias(fileR)
    arbolHuffman = crearArbolHuff(nodosHuffman(frecuenciasOrig))
    binario = BinarioArbol(arbolHuffman)
    compress = comprimirTexto(fileR, binario)
    altura = alturaArbol(arbolHuffman)
    anchura = anchuraArbol(arbolHuffman)
    nodosNivel = nodosPorNivel(arbolHuffman)
    end = time.time()

    nombre = os.path.splitext(archivo)[0]
    os.makedirs(nombre, exist_ok=True)
    with open(os.path.join(nombre, f"{archivo}.tsgr"), "wb") as TSGR:
        bits = bit.bitarray(compress)
        bits.tofile(TSGR)
    
    with open(os.path.join(nombre, f"{archivo}.stats"), "w") as stats:
        sizeOrig = os.path.getsize(archivo)
        sizeCompress = os.path.getsize(f"{nombre}/{archivo}.tsgr")
        stats.write(f'Tamaño del archivo original: {sizeOrig}B\n' + 
                    f'Tamaño del archivo comprimido: {sizeCompress}B\n' + 
                    f'Tiempo de ejecución: {end - start}s\n' +
                    f'Altura del árbol: {altura}\n' +
                    f'Anchura del árbol: {anchura}\n' +
                    f'Cantidad de nodos por nivel: {nodosNivel}\n' +
                    f'Frecuencias originales: {frecuenciasOrig}\n')

    with open(os.path.join(nombre, f"{archivo}.table"), "w") as table:
        for char, binar in binario.items():
            table.write(f'{char}:{binar}\n')

    with open(os.path.join(nombre, f"{archivo}.length"), "w") as fileLength:
        fileLength.write(str(len(compress)))

    print(f'{archivo} comprimido con éxito')

if __name__ == '__main__':
    main()