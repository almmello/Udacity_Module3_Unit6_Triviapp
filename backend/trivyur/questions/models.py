#----------------------------------------------------------------------------#
# Imports
#----------------------------------------------------------------------------#
from trivyur import db


#----------------------------------------------------------------------------#
# Models.
#----------------------------------------------------------------------------#

class Question(db.Model):
    __tablename__ = 'questions'

    id = db.Column(db.Integer, primary_key=True)
    question = db.Column(db.String)
    answer = db.Column(db.String)
    category = db.Column(db.String)
    difficulty = db.Column(db.Integer)

    def __init__(self, question, answer, category, difficulty):
        self.question = question
        self.answer = answer
        self.category = category
        self.difficulty = difficulty

    def insert(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def format(self):
        return {
            'id': self.id,
            'question': self.question,
            'answer': self.answer,
            'category': self.category,
            'difficulty': self.difficulty
            }



    
    # Changed relationship to lazy='joined', cascade="all, delete"
    #shows = db.relationship('Show', backref='artist', lazy='joined', cascade="all, delete")

    def __repr__(self):
        return f'<Class ID: {self.id}, QUESTION: {self.question}>'
