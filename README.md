# IC-1803 — Taller de Programación

<p align="center">🐍</p>

<p align="center">
  <img alt="Python" src="https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white">
  <a href="LICENSE"><img alt="Licencia GPL-3.0" src="https://img.shields.io/github/license/tonys183/IC-1803-TallerProgramacion?style=flat-square&label=Licencia&logo=opensourceinitiative&logoColor=white"></a>
</p>

<p align="center">
  <a href="#temas-generales">Temas generales</a> · <a href="#proyecto-i">Proyecto I</a> · <a href="#proyecto-ii">Proyecto II</a> · <a href="#proyecto-iii">Proyecto III</a>
</p>

Soluciones a ejercicios del curso Taller de Programación (IC-1803), desarrolladas en Python.

## Temas generales

1. Funciones, condicionales y ciclos.
2. Recursividad y operaciones numéricas.
3. Manejo de cadenas y listas.
4. Matrices y sus operaciones.
5. Búsqueda y ordenamiento.
6. Clases y estructuras de datos.
7. Árboles y recorridos.
8. Búsqueda de soluciones con restricciones.

## Proyecto I

El proyecto consistía en buscar parejas de numeradores y denominadores de hasta cinco dígitos cuyo cociente fuera un número dado, respetando un límite de repeticiones de dígitos. La relación que debían cumplir era:

$$
\frac{d_1d_2d_3d_4d_5}{d_6d_7d_8d_9d_0} = C
$$

Aquí, $C$ es el cociente dado y $R$ limita cuántas veces puede aparecer cada dígito entre el numerador y el denominador.
La carpeta incluye la solución en Python y los casos de prueba.

## Proyecto II

El proyecto consistía en resolver el rompecabezas Katamino: buscar una forma de colocar un conjunto de piezas en un tablero rectangular de modo que quedara completamente cubierto, sin superposiciones ni espacios vacíos. La búsqueda debía considerar distintas posiciones y rotaciones de las piezas, así como casos sin solución.

## Proyecto III

El proyecto consistía en comprimir y descomprimir archivos mediante árboles de Huffman. A partir de la frecuencia de los símbolos, se construían códigos binarios para reducir el tamaño del archivo y permitir recuperar su contenido original sin pérdida de información.
