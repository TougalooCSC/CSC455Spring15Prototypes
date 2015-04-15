from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, DateTime, Boolean, Table
# from app import db
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship, backref

from datetime import datetime

engine = create_engine('sqlite:///database.db', echo=True)
db_session = scoped_session(sessionmaker(autocommit=False,
                                         autoflush=False,
                                         bind=engine))
Base = declarative_base()
Base.query = db_session.query_property()

# Set your classes here.
class TCBase:
    # id = Column(Integer, primary_key=True)
    created_at = Column(DateTime)
    updated_at = Column(DateTime)
    is_active = Column(Boolean)

    def __init__(self):
        self.created_at = datetime.utcnow()
        self.updated_at = self.created_at
        self.is_active = True


class User(Base, TCBase):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String(120), unique=True)
    email = Column(String(120), unique=True)
    password = Column(String(30))

    cards = relationship("FlashCard", backref="creator", lazy='dynamic')
    responses = relationship("FlashCardResponse", backref="responder", lazy='dynamic')
    decks = relationship("Deck", backref="creator", lazy='dynamic')

    def __init__(self, name=None, password=None):
        TCBase.__init__(self)
        self.name = name
        self.password = password
        self.cards = []

        # def __repr__(self):
        # return '<User %r>' % self.name


class FlashCard(Base, TCBase):
    __tablename__ = 'flashcards'

    id = Column(Integer, primary_key=True)
    question_text = Column(String(256))
    question_answer = Column(String(127))
    created_by = Column(Integer, ForeignKey('users.id'))

    # user = relationship("User", backref=backref('cards', order_by=id))
    responses = relationship("FlashCardResponse", backref="flashcard", lazy='dynamic')

    def __init__(self, question_text=None, question_answer=None, user=None):
        TCBase.__init__(self)
        self.question_text = question_text
        self.question_answer = question_answer
        self.created_by = user.id
        self.user = user


class FlashCardResponse(TCBase, Base):
    __tablename__ = 'flashcard_responses'

    id = Column(Integer, primary_key=True)
    response = Column(String(127))
    flashcard_id = Column(Integer, ForeignKey('flashcards.id'))
    user_id = Column(Integer, ForeignKey('users.id'))

    # user = relationship("User", backref=backref('responses_by', order_by=id))
    # card = relationship("FlashCard", backref=backref('responses_to', order_by=id))

    def __init__(self, flashcard=None, user=None, response=None):
        TCBase.__init__(self)
        if isinstance(flashcard, FlashCard):
            self.flashcard_id = flashcard.id
            self.flashcard = flashcard
        elif type(flashcard) is int:
            self.flashcard_id = flashcard
        # TODO else throw error 'must provide flashcard'
        if isinstance(user, User):
            self.user_id = user.id
            self.user = user
        elif type(user) is int:
            self.user_id = user
        # TODO throw error 'must provide user'
        self.response = response  # Consider disallowing NULL values.


card_decks = Table('card_decks',
                      Base.metadata, # AttributeError thanks to stackoverflow.com Q/A
                      Column('flashcard_id', Integer, ForeignKey('flashcards.id')),
                      Column('deck_id', Integer, ForeignKey('decks.id'))
)


class Deck(TCBase, Base):
    __tablename__ = 'decks'

    id = Column(Integer, primary_key=True)
    title = Column(String(127))
    created_by = Column(Integer, ForeignKey('users.id'))

    cards = relationship('FlashCard', secondary=card_decks, backref='decks')

    def __init__(self, title=None, created_by=None):
        self.title = title
        if type(created_by) == int:
            self.created_by = created_by
            self.creator = User.query.filter_by(id=created_by).first()
        elif isinstance(created_by, User):
            self.created_by = created_by.id
            self.creator = created_by
        else:
            self.created_by = None


# Create tables.
Base.metadata.create_all(bind=engine)
