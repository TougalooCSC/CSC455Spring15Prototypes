# ----------------------------------------------------------------------------#
# Imports
# ----------------------------------------------------------------------------#

from flask import request, jsonify, abort, Blueprint
import models

mod = Blueprint('flashcard', __name__)

# retrieve multiple
@mod.route('/flashcards', methods=['GET'])
<<<<<<< HEAD
def get_flashcards():
    flashcards = models.FlashCard.query.all()
    return jsonify({'flashcard': [{'id': flashcard.id, 'question': flashcard.question_text, 'answer': flashcard.question_answer, "creator": flashcard.created_by} for flashcard in flashcards]})
=======
def get_flashcards(id):
    flashcard = models.FlashCard.query.all()
    return jsonify({'flashcard': [{'id': flashcard.id, 'question': flashcard.question_text, 'answer': flashcard.question_answer, "creator": flashcard.created_by} for user in users]})
>>>>>>> FETCH_HEAD


# retrieve individual
@mod.route('/flashcards/<id>', methods=['GET'])
def get_flashcard(id):
    return jsonify({'flashcard': None})


# create
@mod.route('/flashcards', methods=['POST'])
def create_flashcard():
    if not (request.args['question'] and request.args['answer'] and request.args['creator']):
        abort(404)
    question = request.args['question']
    answer = request.args['answer']
    creator = request.args['creator']
    user_obj = models.User.query.filter_by(id=creator).first()
    if not user_obj:
        print 'User with id: %d not found' % creator
        abort(404)
    card = models.FlashCard(question_text=question, question_answer=answer, user=user_obj)
    models.db_session.add(card)
    models.db_session.commit()
    return jsonify({'flashcard': {'question_text': card.question_text, 'question_answer': card.question_answer,
                                  'created_by': card.user.id}})


# update
@mod.route('/flashcards/<id>', methods=['POST'])
def update_flashcard(id):
    return jsonify({'flashcard': []})


# delete
@mod.route('/flashcards/<id>', methods=['POST'])
def delete_flashcard(id):
    return jsonify({'flashcard': []})
