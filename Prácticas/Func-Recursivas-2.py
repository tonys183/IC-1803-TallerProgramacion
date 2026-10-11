def binToDecimal(binario, decimal=0, i=0):
    if binario == 0:
        return decimal
    else:
        digito = binario % 10 #Recoge el ultimo valor del binario
        decimal = decimal + digito * (2 ** i) #Va acumulando los result de las multiplicaciones del digito * 2 elevado a la posicion
        binario = binario // 10 #Elimina el ultimo valor del binario
        return binToDecimal(binario, decimal, i + 1)
    

def decimalToBin(decimal):
    if decimal == 0:
        return 0
    else:
        return (decimal % 2 + decimalToBin(decimal // 2) * 10) #Modulo de 2 al deciaml, luego se suma el valor de decimal division entera de 2 y se multiplica por 10

def potenciaLog(base, exponente):
    if exponente == 0:
        return 1
    elif exponente == 1:
        return base
    else:
        media_potencia = potenciaLog(base, exponente // 2) #Para calcular la mitad de esa potencia
        resultado = media_potencia * media_potencia #Para volver al valor original
        if exponente % 2 == 1: 
            resultado *= base #Se multiplica porque al hacer // 2 se pierden valores
        return resultado
    

def main():
    binario = 10111
    decimal = binToDecimal(binario)
    print("El número binario", binario, "es", decimal, "en decimal")

    decimal = 47
    binario = decimalToBin(decimal)
    print("El número decimal", decimal, "es", binario, "en binario")

    elevado = potencia(2, 8)
    print("2 elevado a la 8 es:", elevado)

if __name__ == "__main__":
    main()
