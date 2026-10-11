import sys
import bitarray as bit
import os
import shutil

def descomprimirTexto(fileCompress, binario, lengthFileOrig):
    binarioInv = {value: char for char, value in binario.items()}
    temp = ""
    res = ""
    for bit in fileCompress[:lengthFileOrig]:
        temp += bit
        if temp in binarioInv:
            if binarioInv[temp] == "|":
                res += "\n"
            elif binarioInv[temp] == '':
                res += ' '
            else:
                res += binarioInv[temp]
            temp = ""
    return res

def main():
    if len(sys.argv) != 4:
        print("Uso: python3 compresor.py archivoComprimido.txt.bin archivoTabla.txt.table archivo.txt")
        sys.exit(1)

    archivoComp, tabla, archivo = sys.argv[1], sys.argv[2], sys.argv[3]
    lengthFile = f'{archivo}.length'

    bits2 = bit.bitarray()
    nombre = os.path.splitext(archivo)[0]
    with open(os.path.join(nombre, archivoComp), "rb") as fileCompress:
        bits2.fromfile(fileCompress)
    dataBin = bits2.to01()

    with open(os.path.join(nombre, tabla), "r") as dicti:
        dataTable = dicti.read()
    
    binario = {}
    for linea in dataTable.strip().split('\n'):
        if linea[0] == ':':
            binario[linea[0]] = linea[2:]
        else:
            char, valor = linea.split(':')
            binario[char] = valor

    with open(os.path.join(nombre, lengthFile), "r") as lenFile:
        lengthFileOrig = int(lenFile.read().strip())

    decompress = descomprimirTexto(dataBin, binario, lengthFileOrig)
    nombre = os.path.splitext(archivo)[0]
    with open(f"{nombre}Deco.txt", "w") as decom:
        decom.write(decompress)

    print(f'{archivo} descomprimido con éxito')
    shutil.rmtree(nombre)
    
if __name__ == '__main__':
    main()