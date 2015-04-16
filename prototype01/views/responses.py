# ----------------------------------------------------------------------------#
# Imports
# ----------------------------------------------------------------------------#

from flask import request, jsonify, abort, Blueprint
import models

mod = Blueprint('response', __name__)

# retrieve multiple
@mod.route('/responses', methods=['GET'])
def get_responses():
    return jsonify({'responses': []})

# retrieve individual
@mod.route('/responses/<id>', methods=['GET'])
def get_response(id):
    return jsonify({'response': None})

# create
@mod.route('/responses', methods=['POST'])
def create_response():
    if not (request.args['question'] and request.args['answer'] and request.args['creator']):
        abort(404)
    flashcard_id = request.args['question']
    question_response = request.args['answer']
    user_id = request.args['creator']
    new_user_id = models.User.query.filter_by(id=user_id).first()
    if not user_id:
        print 'User with id: %d not found' % creator
        abort(404)
    response = models.FlashCardResponse(flashcard=flashcard_id, response_user=user_id, response_text=response)
    models.db_session.add(response)
    models.db_session.commit()
    return jsonify({'response': {'id': response.id, 'question_response': response.response,
                                  'flashcard': flashcard_id, 'user': user_id}})

# update
@mod.route('/responses/<id>', methods=['POST'])
def update_response(id):
    return jsonify({'response': []})

# delete
@mod.route('/responses/<id>', methods=['POST'])
def delete_response(id):
    response_delete = models.Deck.query.filter_by(id = id).first()
    response_delete.is_active = false
    models.db_session.commit()
    return jsonify({'response': {'id': response.id, 'question_response': response.question_response,
                                  'flashcard_id': response.flashcard_id, 'user_id': response.user_id}})
}})
