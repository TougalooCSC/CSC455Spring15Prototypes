# ----------------------------------------------------------------------------#
# Imports
# ----------------------------------------------------------------------------#

from flask import request, jsonify, abort, Blueprint
import models

mod = Blueprint('flashcard', __name__)

# retrieve multiple
@mod.route('/flashcards', methods=['GET'])
def get_flashcards():
    return jsonify({'flashcards': []})

# retrieve individual
@mod.route('/flashcards/<id>', methods=['GET'])
def get_flashcard():
    return jsonify({'flashcard': None})

# create
@mod.route('/flashcards', methods=['POST'])
def create_flashcard():
    return jsonify({'flashcard': []})

# update
@mod.route('/flashcards/<id>', methods=['POST'])
def update_flashcard():
    return jsonify({'flashcard': []})

# delete
@mod.route('/flashcards/<id>', methods=['POST'])
def delete_flashcard():
    return jsonify({'flashcard': []})
