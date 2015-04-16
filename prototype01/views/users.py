# ----------------------------------------------------------------------------#
# Imports
# ----------------------------------------------------------------------------#

from flask import request, jsonify, abort, Blueprint
import models

mod = Blueprint('user', __name__)

# retrieve all
@mod.route('/users', methods=['GET'])
def get_users():
    users = models.User.query.all()
    return jsonify({'users': [{'id': user.id, 'name': user.name} for user in users]})


# retrieve individual
@mod.route('/users/<id>', methods=['GET'])
def get_user(id):
    user_single = models.User.query.filter_by(id = id).first()
    return jsonify({'user': {'id': user.id, 'name': user.name}})

# create
@mod.route('/users', methods=['POST'])
def create_user():
    print 'args: ', request.args
    if not (request.args['name'] and request.args['password']):
        abort(404)
    name = request.args['name']
    password = request.args['password']
    user = models.User(name=name, password=password)
    models.db_session.add(user)
    models.db_session.commit()
    return jsonify({'user': {'id': user.id, 'name': user.name}})

# update
@mod.route('/users/<id>', methods=['POST'])
def update_user(id):
    # write logic to update user here
    return jsonify({'user': []})

# delete
@mod.route('/users/<id>', methods=['POST'])
def delete_user():
    # write logic to mark user inactive here
    return jsonify({'user': []})
