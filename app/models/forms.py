from flask_wtf import FlaskForm
from wtforms import TextAreaField, SubmitField
from wtforms.validators import DataRequired

class PuzzleForm(FlaskForm):
    matrix = TextAreaField('Matriz', validators=[DataRequired()])
    words = TextAreaField('Palabras a buscar', validators=[DataRequired()])
    submit = SubmitField('Resolver')
