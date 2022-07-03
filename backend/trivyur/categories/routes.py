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
categories_bp = Blueprint('categories_bp', __name__)

#adjusted the imports to package
from trivyur.categories.models import Category

#----------------------------------------------------------------------------#
# Controllers.
#----------------------------------------------------------------------------#

#Adjusted all decorators to use the blueprint


