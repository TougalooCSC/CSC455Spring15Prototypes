from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
# from sqlalchemy import Column, Integer, String
# from app import db
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship, backref

engine = create_engine('sqlite:///database.db', echo=True)
db_session = scoped_session(sessionmaker(autocommit=False,
                                         autoflush=False,
                                         bind=engine))
Base = declarative_base()
Base.query = db_session.query_property()

# Set your classes here.

class User(Base):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), unique=True)
    email = db.Column(db.String(120), unique=True)
    password = db.Column(db.String(30))

    cards = relationship("FlashCard", order_by="FlashCard.id", backref="user")

    def __init__(self, name=None, password=None):
        self.name = name
        self.password = password


class FlashCard(Base):
    __tablename__ = 'flashcards'

    id = db.Column(db.Integer, primary_key=True)
    question_text = db.Column(db.String(256))
    question_answer = db.Column(db.String(127))
    is_active = db.Column(db.Boolean) #TODO set default value
    created_by = db.Column(db.Integer, ForeignKey('users.id'))

    user = relationship("User", backref=backref('cards', order_by=id))


# Create tables.
Base.metadata.create_all(bind=engine)
