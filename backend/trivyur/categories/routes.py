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

@categories_bp.route('/')
@categories_bp.route('/categories')
def read_all_categories():

    # using the try-except method to create the query
    try:

        # create the query categories order by id
        query_categories = Category.query.order_by(Category.id).all()

        # check if the query has no results and abort
        if len(query_categories) == 0:
            abort(404)

        # if has results, return them
        else:

            return jsonify({
                'success': True,
                'categories': {category.id: category.type for category in query_categories}
            })

    # if the query fails, abort
    except:
        abort(404)


"""
@OK:
Create a GET endpoint to get questions based on category.

TEST - OK: In the "List" tab / main screen, clicking on one of the
categories in the left column will cause only questions of that
category to be shown.
"""

@categories_bp.route('/categories/<int:category_id>/questions')
def read_single_category(category_id):

    # using the try-except method to create the query
    try:

        # create the query category type
        query_category_type = Category.query.get(category_id).format()['type']

        # create the query categories filtered by category
        query_questions = Question.query.filter(Question.category == category_id).all()

        # paginate the query
        questions_paginated = paginate_questions(request, query_questions)

        # check if the query results and return them
        if len(query_questions):

            return jsonify({
                'success': True,
                'questions': questions_paginated,
                'total_questions': len(query_questions),
                'current_category': query_category_type
            })

        # if there are no results, abort
        else:
            abort(422)

    # if the query fails, abort
    except:
        abort(422)




