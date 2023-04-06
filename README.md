# Sopa-de-letras
Se necesita desarrollar un algoritmo en Python capaz de resolver una sopa de letras a partir de una matriz
que contiene todas las letras en sus respectivas celdas, junto con un array de palabras que se deben
encontrar.
Este sistema debe ser accesible a través de un endpoint en Flask, y debe recibir las entradas del problema
mediante una solicitud POST. Es decir, se deben proporcionar la matriz de entrada y las palabras a buscar.
Luego, el sistema debe devolver un objeto JSON que contenga los resultados del problema.
Los resultados deben ser visualizados en una vista HTML, la cual se generará a partir del objeto JSON
devuelto por el sistema.
Por ejemplo:
Matriz entrada: [
[ c, g, h, t ],
[ a, a, a, y ],
[ s, z, p, g ],
[ a, o, b, a ],
 ]
Palabras: [casa, capa]
Retorno:
Casa: [ [0, 0], [1, 0], [2, 0], [ 3, 0] ]
Capa: [ [0, 0], [1, 1], [2, 2], [ 3, 3] ]
Requisitos del algoritmo:
El algoritmo deberá tomar las palabras de búsqueda y recorrer la matriz de letras y devolver las
coordenadas [x, y] de las letras encontradas
Restricciones:
Recuerde que solo se pueden hacer uniones en línea recta de manera vertical, horizontal y diagonal
