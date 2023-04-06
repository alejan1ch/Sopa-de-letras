# Sopa-de-letras

Este es un proyecto que tiene como objetivo desarrollar un algoritmo en Python capaz de resolver una sopa de letras a partir de una matriz que contiene todas las letras en sus respectivas celdas, junto con un array de palabras que se deben encontrar.

El sistema está diseñado para ser accesible a través de un endpoint en Flask, y recibir las entradas del problema mediante una solicitud POST. Es decir, se deben proporcionar la matriz de entrada y las palabras a buscar. Luego, el sistema devuelve un objeto JSON que contiene los resultados del problema.

## Ejemplo

A continuación se presenta un ejemplo de la matriz de entrada y las palabras a buscar, junto con el resultado obtenido:
```
Matriz entrada:
[
[c, g, h, t],
[a, a, a, y],
[s, z, p, g],
[a, o, b, a]
]

Palabras: `[casa, capa]`

Retorno:
Casa: [[0, 0], [1, 0], [2, 0], [3, 0]]
Capa: [[0, 0], [1, 1], [2, 2], [3, 3]]
```
## Requisitos del algoritmo

El algoritmo debe tomar las palabras de búsqueda y recorrer la matriz de letras para devolver 
las coordenadas `[x, y]` de las letras encontradas.

## Restricciones

Recuerde que solo se pueden hacer uniones en línea recta de manera vertical, horizontal y diagonal.

## Cómo utilizar

Para utilizar el proyecto, sigue los siguientes pasos:

### Clonar el repositorio

1. Abre una terminal y dirígete al directorio en el que deseas clonar el repositorio.
2. Ejecuta el siguiente comando: `git clone <URL del repositorio>`.
3. Después de clonar el repositorio, ingresa al directorio del proyecto utilizando el comando `cd <nombre del proyecto>`.

### Configurar el entorno virtual

1. Ejecuta el siguiente comando para crear un entorno virtual: `python -m venv <nombre del entorno virtual>`.
2. Activa el entorno virtual ejecutando `source <nombre del entorno virtual>/bin/activate` (en Linux o MacOS) o `<nombre del entorno virtual>\Scripts\activate` (en Windows).
3. Ahora, debes instalar las dependencias utilizando el archivo `requirements.txt`. Ejecuta el siguiente comando: `pip install -r requirements.txt`.

### Ejecutar la aplicación

1. Ejecuta el siguiente comando: `flask run`.
2. Abre un navegador y dirígete a la dirección `http://localhost:5000/game`.
3. En el apartado matriz, ingresa la matriz de letras que deseas utilizar.
```
[
[c, g, h, t],
[a, a, a, y],
[s, z, p, g],
[a, o, b, a]
]
```

4. En el apartado palabras, ingresa las palabras que deseas buscar en la matriz.

```
[casa, capa]
```

5. Finalmente, presiona el botón "resolver" para obtener los resultados en formato JSON.

#Autor de la resolucion del problema
Alejandro Cruz Hernandez

    
