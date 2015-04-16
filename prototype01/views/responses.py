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
    return jsonify({'response': []})

# update
@mod.route('/responses/<id>', methods=['POST'])
def update_response(id):
    return jsonify({'response': []})

# delete
@mod.route('/responses/<id>', methods=['POST'])
def delete_response(id):
    return jsonify({'response': []})
