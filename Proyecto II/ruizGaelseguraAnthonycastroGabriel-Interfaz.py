import time
import tkinter as tk

def matrizGrande(f,c):
    mat=[]
    for _ in range(f):
        mat.append(["."]*c)
    return mat

def esSolucion(matriz):
    for fila in matriz:
        if '.' in fila:
            return False
    return True

def esValido(matriz, pieza, x, y):
    for i in range(len(pieza)):
        for j in range(len(pieza[0])):
            if pieza[i][j] != '.':
                if x + i >= len(matriz) or y + j >= len(matriz[0]):
                        return False
                else:
                    if matriz[x+i][y+j]!=".":
                        return False
    return True

#Función para rotar la pieza n veces
def rotar90Grados(pieza):
    filas = len(pieza)
    columnas = len(pieza[0])
    pieza_rotada = []

    for j in range(columnas):
        fila_rotada = []
        for i in range(filas - 1, -1, -1):
           
            fila_rotada.append(pieza[i][j])
        pieza_rotada.append(fila_rotada)
    return pieza_rotada

def rotarPieza(pieza, rotacion):
    for _ in range(rotacion):
        pieza = rotar90Grados(pieza)
    return pieza

def insertarPieza(matriz, pieza, x, y):
    matriz_copia =[]
    for fila in matriz:
        filaNueva = []
        for elemento in fila:
            filaNueva.append(elemento)
        matriz_copia.append(filaNueva)

    for i in range(len(pieza)):
        for j in range(len(pieza[0])):
            if pieza[i][j] != '.':
                matriz_copia[x + i][y + j] = pieza[i][j]
    return matriz_copia

#Backtracking
def buscarHijos(matriz, piezas, indicePieza, L, A):
    hijos = []
    if indicePieza == len(piezas):
        return hijos
    pieza = piezas[indicePieza]

    for rotacion in range(4):
        pieza_rotada = meterEsquina(rotarPieza(pieza, rotacion))
        for x in range(L):
            for y in range(A):
                if esValido(matriz, pieza_rotada, x, y):
                    nueva_matriz = insertarPieza(matriz, pieza_rotada, x, y)
                    hijos.append((nueva_matriz, indicePieza + 1))
    return hijos

def resolver(piezas, L, A):
    pila = [(matrizGrande(L, A), 0)]
    while pila:
        matrizActu, indicePieza = pila.pop()
        
        if indicePieza == len(piezas):
            if esSolucion(matrizActu):
                return matrizActu
        for hijo in buscarHijos(matrizActu, piezas, indicePieza, L, A):
            pila.append(hijo)
    return None

#Poner la pieza en la esquina superior izquierda
def esquina(pieza):
    fil=False
    col=False
    for e in pieza[0]:
        if e!=".":
            fil=True
    for columnas in range(len(pieza)):
        if pieza[columnas][0]!=".":
            col= True
    return col and fil

def alIzq(pieza,veces):
    for i in range(veces):
        if esquina(pieza):
            break
        for filas in range(len(pieza)):
            pieza[filas].append(".")
            pieza[filas].pop(0)
    return pieza

def Arriba(pieza,veces):
    for i in range(veces):
        if esquina(pieza):
            break
        pieza.append(["."]*len(pieza[0]))
        pieza.pop(0)
    return pieza

def meterEsquina(pieza):
    if not esquina(pieza):
        cambio=False
        for i in range(len(pieza)):
            if cambio:
                break
            for j in range(len(pieza[0])):
                if pieza[i][j] != ".":
                    pieza=Arriba(pieza,i)
                    pieza=alIzq(pieza,j)
                    cambio=True
                    break
    return pieza

#Sección Interefaz
def generarColores(piezas):
    colores = {}
    colores_usados = ["red", "green", "blue", "yellow", "purple", "orange", "cyan", "magenta", "lime", "pink", "teal", "lavender", "brown", "beige", "maroon", "black", "olive", "coral"]
    
    color_index = 0
    for pieza in piezas:
        for fila in pieza:
            for caracter in fila:
                if caracter not in colores:
                    colores[caracter] = colores_usados[color_index % len(colores_usados)]
                    color_index += 1
    return colores

def crearInterfaz(matriz, L, A, colores):
    root= tk.Tk()
    root.wm_attributes("-topmost", 1)
    root.geometry("-180+180")

    celda= 40
    ancho = A * celda + 120
    largo = L * celda + 120

    centroX = (ancho - A * celda) // 2
    centroY = (largo - L * celda) // 2
    
    fondo = tk.PhotoImage(file="wood_texture.png")

    if matriz == None:
        root.title("Sin Solución - Katamino")
        
        ventanaSinSolucion = tk.Canvas(root, width=ancho, height=largo)
        ventanaSinSolucion.pack()
        
        ventanaSinSolucion.create_image(0, 0, image=fondo, anchor="nw")
        ventanaSinSolucion.create_text(ancho//2, largo//2, text="Sin Solución", font=('Segoe UI Semibold', 15))
        ventanaSinSolucion.create_text(30, largo//2, text="KATAMINO", font=('Segoe UI Light', 18), angle = 90)
        ventanaSinSolucion.create_text(ancho-30, largo//2, text="KATAMINO", font=('Segoe UI Light', 18), angle = -90)

    else:
        root.title("Solución del Tablero - Katamino")
        ventanaSolucion = tk.Canvas(root, width=ancho, height=largo)
        ventanaSolucion.pack()
        
        ventanaSolucion.create_image(0, 0, image=fondo, anchor="nw")
        ventanaSolucion.create_text(30, largo//2, text="KATAMINO", font=('Segoe UI Light', 18), angle = -90)
        ventanaSolucion.create_text(ancho-30, largo//2, text="KATAMINO", font=('Segoe UI Light', 18), angle = 90)

        for i in range(len(matriz)):
            j=0
            for caracter in matriz[i]:
                x1, y1 = j * celda + centroX, i * celda + centroY
                x2, y2 = x1 + celda, y1 + celda
                color = colores[caracter]
                ventanaSolucion.create_rectangle(x1, y1, x2, y2, outline="black", fill=color)
                j+=1
    
    root.mainloop()

#Entrada
def main():
    L, A, P = map(int, input().split())
    matrizAllPiezas= []
    for _ in range(P):
        matrizPiezas= matrizGrande(L, A)
        for a in range(P):
            piezas = input()
            for pieza in range(len(piezas)):
                matrizPiezas[pieza][a]=piezas[pieza]
        matrizAllPiezas.append(matrizPiezas) 
    colores = generarColores(matrizAllPiezas) 
    start = time.time()    
    solucion = resolver(matrizAllPiezas, L, A)
    end = time.time()
    print(f"Tiempo: {end - start}\n")
    if solucion:
        crearInterfaz(solucion,L,A,colores)
    else:
        crearInterfaz(solucion,L,A,colores)

if __name__ == '__main__':
    main()