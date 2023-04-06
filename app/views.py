from flask import Blueprint, render_template, jsonify, request
from .models.forms import PuzzleForm

bp = Blueprint('main', __name__)

@bp.route('/game', methods=('GET', 'POST'))
def game():
    form = PuzzleForm()
    if request.method == 'POST':
        matrix = form.matrix.data
        words = form.words.data
        print(matrix)
        print(words)
        # Lógica para resolver la sopa de letras
             
        results= {
                 "key": ['coordinates']
        }
        return jsonify(results=results)
    return render_template('game.html')
    
