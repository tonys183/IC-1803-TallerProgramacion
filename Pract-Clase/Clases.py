class Libro():
    def __init__(self, pTitulo, pISBN, pAutor, pCategoria, pAñoPubli):
        self.titulo = pTitulo
        self.ISBN = pISBN
        self.autor = pAutor
        self.categoria = pCategoria
        self.añoPubli = pAñoPubli
    
    def descripcion(self):
        return f"\nEl libro [{self.titulo}] con ISBN: {self.ISBN} fue publicado en {self.añoPubli}. Su autor fue {self.autor} y categorizado como {self.categoria}"

    def actualizarAño(self, pAñoPubli):
        self.añoPubli = pAñoPubli
        return f"-Año actualizado correctamente-"
    
libro1 = Libro("La Odisea", "9781509431168", "Omero", "Poema épico", "2024")    
print(libro1.descripcion())
libro2 = Libro("El señor de los anillos", "9788845292613", "J. R. R. Tolkien", "Literatura fantástica, Alta fantasía, Ficción de aventuras,", "1954")    
print(libro2.descripcion())
libro3 = Libro("El Principito", "9783140464079", "Antoine de Saint-Exupéry", "Literatura infantil, Novela corta, Fábula", "1943")    
print(libro3.descripcion())

pActualizarAño = input("\n----Actualizar Año----\nActualizar el año el Libro 1: ")
print(libro1.actualizarAño(pActualizarAño))
print(libro1.descripcion())



class Nodo():
    def __init__(self, pValor):
        self.valor = pValor
        self.nodoIzq = None
        self.nodoMedio = None
        self.nodoDere = None

    def actualizarValor(self, pValor):
        if pValor < self.valor:
            if self.nodoIzq == None:
                self.nodoIzq = pValor
            else:
                self.nodoIzq = self.insertar(self.nodoIzq, pValor)

        if pValor > self.valor:
            if self.nodoDere == None:
                self.nodoDere = pValor
            else:
                self.nodoDere = self.insertar(self.nodoDere, pValor)

        if pValor == self.valor:
            if self.nodoMedio == None:
                self.nodoMedio = pValor
            else:
                self.nodoMedio = self.insertar(self.nodoMedio, pValor)
        

    def crearNodo(self, pValor):
        return pValor
    
    def insertar(self, nodo, dato):
        if nodo == None:
            return self.crearNodo(dato)
        if nodo > dato:
            self.nodoIzq = self.insertar(self.nodoIzq , dato)
        else:
            self.nodoDere = self.insertar(self.nodoDere, dato)

    def printNodo(self):
        print(self.valor)
        print(self.nodoIzq)
        print(self.nodoDere)
        print(self.nodoMedio)
    
nodo = Nodo(1)
nodo.actualizarValor(-1)
nodo.actualizarValor(1)
nodo.actualizarValor(2)
nodo.actualizarValor(3)
nodo.printNodo()