from math import  sqrt

def duplo(numero):
    return 2 * numero #Doble de un numero

def formuGeneral(a,b,c):
    x1 = (-b + (sqrt((b**2) -4 * a * c))) / (2*a) #Formula general que devuelve la solucion de x1
    #x2 = (-b - (sqrt((b**2) -4 * a * c))) / (2*a) #Se podria obtener x2 si se quisiera
    return x1

def precioFinal(precio, iva=0.13):
    return (precio * iva) + precio #Precio final de un producto con el iva

def valorAbsoluto(numero):
    if (numero < 0):
        return -numero
        #return -1 * numero #Otra manera de hacerlo
    else:
        return numero
    

def main():
    print(duplo(5))
    print(formuGeneral(1, 5, 6))
    print(precioFinal(101))
    print(valorAbsoluto(-5))

if __name__ == "__main__":
    main()