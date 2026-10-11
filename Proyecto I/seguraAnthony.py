import time

def digitosRepeti(numero, R):
    vistos = [0] * 10 
    for digito in numero:
        valor = int(digito)
        vistos[valor] += 1
        if vistos[valor] > R:
            return False
    return True

def encontrarCombina(C, R):
    encontrada = False
    for denominador in range(10000 // C, 100000 // C):
        numerador = denominador * C
        numeradorString = str(numerador)
        denominadorString = str(int(denominador))

        if len(denominadorString) >= 4:
            if len(denominadorString) < 5:
                denominadorString = '0' + denominadorString
        
            if digitosRepeti(numeradorString + denominadorString, R):
                print(f"{numerador}/{denominador}={C}")
                encontrada = True
    if not encontrada:
        print(f"No existe ninguna combinación para los valores de C={C} y R={R}")

def main():
    T = int(input())
    if T <= 100 and T >= 1:
        for _ in range(T):
            C, R = map(int, input().split())
            if (C <= 20 and C >= 1) and (R <= 5 and R >= 1):
                start = time.time() 
                encontrarCombina(C, R)
                end = time.time()
                print(end - start)
            else:
                print(f"Los valores de C:{C} o R:{R} se encuentran fuera del rango")
    else:
        print("Inválido número de casos")    
if __name__ == "__main__":
    main()


