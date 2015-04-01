from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
# from sqlalchemy import Column, Integer, String
from app import db
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
    # id = db.Column(db.Integer, primary_key=True)
    created_at = db.Column(db.DateTime)
    updated_at = db.Column(db.DateTime)
    is_active = db.Column(db.Boolean)

    def __init__(self):
        self.created_at = datetime.utcnow()
        self.updated_at = self.created_at
        self.is_active = True


class User(Base, TCBase):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), unique=True)
    email = db.Column(db.String(120), unique=True)
    password = db.Column(db.String(30))

    # cards = relationship("FlashCard", order_by="FlashCard.id", backref="user")

    def __init__(self, name=None, password=None):
        TCBase.__init__(self)
        self.name = name
        self.password = password
        self.cards = []

    def __repr__(self):
        return '<User %r>' % self.name


class FlashCard(Base, TCBase):
    __tablename__ = 'flashcards'

    id = db.Column(db.Integer, primary_key=True)
    question_text = db.Column(db.String(256))
    question_answer = db.Column(db.String(127))
    created_by = db.Column(db.Integer, ForeignKey('users.id'))

    user = relationship("User", backref=backref('cards', order_by=id))

    def __init__(self, question_text=None, question_answer=None, user=None):
        TCBase.__init__(self)
        self.question_text = question_text
        self.question_answer = question_answer
        self.created_by = user.id
        self.user = user

# Create tables.
Base.metadata.create_all(bind=engine)
