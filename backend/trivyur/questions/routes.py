#----------------------------------------------------------------------------#
# Imports
#----------------------------------------------------------------------------#
from flask import (
                   render_template,
                   flash,
                   redirect,
                   request,
                   url_for,
                   Blueprint
                  )
from trivyur import db
from datetime import datetime
import sys

#create the blueprint
questions_bp = Blueprint('questions_bp', __name__)

#adjusted the imports to package
from trivyur.questions.models import Question


#----------------------------------------------------------------------------#
# Controllers.
#----------------------------------------------------------------------------#

#Adjusted all decorators to use the blueprint

#@artists_bp.route('/artists')
#def artists():
