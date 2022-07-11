#----------------------------------------------------------------------------#
# Imports
#----------------------------------------------------------------------------#
from trivyur import db


#----------------------------------------------------------------------------#
# Models.
#----------------------------------------------------------------------------#

class Category(db.Model):
    __tablename__ = 'categories'

    id = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.String)


    def __init__(self, type):
        self.type = type


    def format(self):
        return {
            'id': self.id,
            'type': self.type
            }

    
    def __repr__(self):
        return f'<Class ID: {self.id}, TYPE: {self.type}>'

