#Ejercicio 1
def redireccion1(x):
    print ("Hola", x)

nombres = int(input())

while nombres:
    x = input()
    nombres -= 1
    redireccion1(x)

