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
def get_response():
    return jsonify({'response': None})

# create
@mod.route('/responses', methods=['POST'])
def create_response():
    if not (request.args['question'] and request.args['answer'] and request.args['creator']):
        abort(404)
    id = request.args['question']
    question_response = request.args['answer']
    flashcard_id = request.args['creator']
    user_id = models.User.query.filter_by(id=creator).first()
    if not user_id:
        print 'User with id: %d not found' % creator
        abort(404)
    response = models.FlashCardResponse(question_text=question, question_answer=answer, user=user_id)
    models.db_session.add(response)
    models.db_session.commit()
    return jsonify({'response': {'id': response.id, 'question_response': response.question_response,
                                  'flashcard_id': response.flashcard_id, 'user_id': response.user_id}})

# update
@mod.route('/responses/<id>', methods=['POST'])
def update_response():
    return jsonify({'response': []})

# delete
@mod.route('/responses/<id>', methods=['POST'])
def delete_response():
    return jsonify({'response': []})
