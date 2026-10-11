def factorial(n):
    if n < 2:
        return 1
    return n * factorial(n - 1)

def factores(n):
    listFactores = []
    for i in range(1, n + 1):
        if n % i == 0:
            listFactores.append(i)
    return listFactores

def divisible(N, D):
    resultLista = factores(factorial(N))
    cont = 0
    for elemento in resultLista:
       if elemento % D == 0:
           cont += 1
    return cont

while True:
    N, D = map(int, input().split())
    if N == 0 and D == 0:
        break
    print(divisible(N, D))
