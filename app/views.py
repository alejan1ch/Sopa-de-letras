import ast
from flask import Blueprint, render_template, jsonify, request
from .models.forms import PuzzleForm
from .models.variables import variables

bp = Blueprint('main', __name__)

@bp.route('/game', methods=('GET', 'POST'))
def game():
    form = PuzzleForm()
    if request.method == 'POST':
        matrix = form.matrix.data
        words = form.words.data
        for var, val in variables.items():
            matrix= matrix.replace(var, f'"{val}"')
            words = words.replace(var, f'"{val}"')

        # Use ast.literal_eval() to convert the string to a nested list
        matrix = ast.literal_eval(matrix)
        words = ast.literal_eval(words)
        results = find_words(matrix, words)
        return jsonify(results=results)
    return render_template('game.html')

def find_word(matrix, word):
    """
    Busca una palabra en una matriz dada en las direcciones horizontal,
    vertical y diagonal (hacia arriba, abajo, izquierda, derecha y diagonal).

    Args:
        matrix (list): Una matriz (lista de listas) de caracteres.
        word (str): La palabra que se busca en la matriz.

    Returns:
        Una lista de coordenadas (tuplas de fila, columna) que representan la posición
        inicial de la palabra en la matriz y las posiciones de las letras restantes
        de la palabra en la matriz en una línea horizontal, vertical o diagonal.
        Si la palabra no se encuentra en la matriz, devuelve None.
    """
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == word[0]: # Si la primera letra de la palabra coincide con la letra en la posición actual
                k = 1 # Inicializa un contador k en 1
                while k < len(word) and i+k < len(matrix) and matrix[i+k][j] == word[k]:
                    k += 1 # Incrementa k mientras las letras de la palabra coinciden con las letras en la matriz
                if k == len(word):
                    # Si se han encontrado todas las letras de la palabra en una línea vertical hacia abajo, devuelve las coordenadas
                    return [[i+x, j] for x in range(k)]
                k = 1 # Resetea el contador k
                while k < len(word) and j+k < len(matrix[i]) and matrix[i][j+k] == word[k]:
                    k += 1 # Incrementa k mientras las letras de la palabra coinciden con las letras en la matriz
                if k == len(word):
                    # Si se han encontrado todas las letras de la palabra en una línea horizontal hacia la derecha, devuelve las coordenadas
                    return [[i, j+x] for x in range(k)]
                k = 1 # Resetea el contador k
                while k < len(word) and i+k < len(matrix) and j+k < len(matrix[i]) and matrix[i+k][j+k] == word[k]:
                    k += 1 # Incrementa k mientras las letras de la palabra coinciden con las letras en la matriz
                if k == len(word):
                    # Si se han encontrado todas las letras de la palabra en una línea diagonal hacia la derecha y abajo, devuelve las coordenadas
                    return [[i+x, j+x] for x in range(k)]
                k = 1 # Resetea el contador k
                while k < len(word) and i-k >= 0 and j+k < len(matrix[i]) and matrix[i-k][j+k] == word[k]:
                    k += 1 # Incrementa k mientras las letras de la palabra coinciden con las letras en la matriz
                if k == len(word):
                    # Si se han encontrado todas las letras de la palabra en una línea diagonal hacia arriba y la derecha, devuelve las coordenadas
                    return [[i-x, j+x] for x in range(k)]
    return None # Si la palabra no se encuentra en la matriz, devuelve None



def find_words(matrix, words):
    """
    Busca una lista de palabras en una matriz dada.

    Args:
        matrix (list): Una matriz (lista de listas) de caracteres.
        words (list): Una lista de palabras a buscar en la matriz.

    Returns:
        Un diccionario que mapea cada palabra encontrada con una lista de coordenadas
        de la matriz que corresponden a la posición inicial de la palabra en la matriz,
        y las posiciones de las letras restantes de la palabra en la matriz en una línea
        horizontal, vertical o diagonal.
    """
    word_coords = {} # Diccionario para almacenar las coordenadas de las palabras encontradas
    for word in words:
        coords = find_word(matrix, word) # Busca la palabra en la matriz
        if coords:
            word_coords[word] = coords # Si se encuentra la palabra, agrega las coordenadas al diccionario
    return word_coords # Devuelve el diccionario de coordenadas de palabras encontradas

