#Ejercicio 1
matrizEstu = [[100,100,75],[80,85,95],[80,90,70]]

#Matriz
print("Matriz:")
for i in range(len(matrizEstu)):
    for j in range(len(matrizEstu[i])):
        print(matrizEstu[i][j], end=" ")
    print(" ")


#Promedio Materia Matriz
print("\nPromedio Materia Matriz:")
materia = int(input("¿De cual materia? "))
promedioMate = 0
for i in range(len(matrizEstu[materia])):
    promedioMate += matrizEstu[materia][i]
promedioMate /= len(matrizEstu[materia])
print(promedioMate)


#Promedio Estudiante Matriz
print("\nPromedio Estudiante Matriz:")
estudiante = int(input("¿De cual estudiante? "))
promedioEstu = 0
for i in range(len(matrizEstu)):
    promedioEstu += matrizEstu[i][estudiante]
promedioEstu /= len(matrizEstu)
print(promedioEstu)

#Sacar nota más alta estudiante
print("\nNota más alta estudiante:")
estudiante = int(input("¿De cual estudiante? "))
notaEstuAlta = 0
for i in range(len(matrizEstu)):
    if matrizEstu[i][estudiante] > matrizEstu[i+1][estudiante]:
        notaEstuAlta = matrizEstu[i][estudiante]

print(promedioEstu)
