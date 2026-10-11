malespin =  [['A', 'I', 'B', 'F', 'P', 'E', 'O', 'T', 'G', 'M'],
             ['E', 'O', 'T', 'G', 'M', 'A', 'I', 'B', 'F', 'P']]

def printString(newWord):
    empty = ""
    for element in newWord:
        empty += element
    return empty

def stringToList(text):
    textList = []
    pos = 0
    for char in text:
        textList.append(text[pos])
        pos +=1
    return textList

def traducir(text):
    textList = stringToList(text)

    newWord = []
    strEmpy= ""
    for element in textList:
        char = element
        for i in range(len(malespin[0])):
            if element == malespin[0][i]:
                char = malespin[1][i]
        newWord.append(char)    
    return printString(newWord)

print("\n-------------------\nTRADUCTOR MALESPÍN \n-------------------")
text = input("\nPalabra a traducir : ")
print("Resultado:", traducir(text))