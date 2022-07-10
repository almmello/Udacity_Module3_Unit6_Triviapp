#----------------------------------------------------------------------------#
# Imports
#----------------------------------------------------------------------------#
from flask import (
                   render_template,
                   flash,
                   redirect,
                   request,
                   url_for,
                   Blueprint,
                   abort,
                   jsonify
                  )


from trivyur import db
from datetime import datetime
from trivyur.questions.routes import paginate_questions


import sys

#create the blueprint
categories_bp = Blueprint('categories_bp', __name__)

#adjusted the imports to package
from trivyur.categories.models import Category
from trivyur.questions.models import Question

#----------------------------------------------------------------------------#
# Controllers.
#----------------------------------------------------------------------------#

"""
@TODO:
Create an endpoint to handle GET requests
for all available categories.
"""




