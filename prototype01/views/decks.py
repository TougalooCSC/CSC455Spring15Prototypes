# ----------------------------------------------------------------------------#
# Imports
# ----------------------------------------------------------------------------#

from flask import request, jsonify, abort, Blueprint
import models

mod = Blueprint('deck', __name__)

# retrieve multiple
@mod.route('/decks', methods=['GET'])
def get_decks():
    return jsonify({'decks': []})

# retrieve individual
@mod.route('/decks/<id>', methods=['GET'])
def get_deck(id):
    return jsonify({'deck': None})

# create
@mod.route('/decks', methods=['POST'])
def create_deck():
    return jsonify({'deck': []})

# update
@mod.route('/decks/<id>', methods=['POST'])
def update_deck(id):
    deck_update = models.Deck.query.filter_by(id = id).first()
    deck.title = new_title
    deck.created_by = new_creator
    deck.cards = new_cards
    db_session.commit()
    return jsonify({'user': None})


# delete
@mod.route('/decks/<id>', methods=['POST'])
def delete_deck(id):
    return jsonify({'deck': []})
