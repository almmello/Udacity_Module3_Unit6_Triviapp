import os
import sys
from flask import Flask, request, abort, json, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
import random
from werkzeug.exceptions import HTTPException
from models import setup_db, Question, Category, db

QUESTIONS_PER_PAGE = 10

# Create pagination method for questions pages
def paginate_questions(request, data):

    # retrieve the page number on the request
    page = request.args.get('page', 1, type=int)

    # calculate the start question based on the requested page
    start = (page - 1) * QUESTIONS_PER_PAGE

    # calculate the ending question
    end = start + QUESTIONS_PER_PAGE

    # applies the Question.format method on data received
    questions_paginated = [Question.format() for Question in data]

    # creates the return dictionary from start to end questions
    current_questions_page = questions_paginated[start:end]

    return current_questions_page

def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__)
    setup_db(app)



    """
    @OK: Set up CORS. Allow '*' for origins. Delete the sample route after completing the TODOs
    """

    """
    @OK: Use the after_request decorator to set Access-Control-Allow
    """

    CORS(app)

    # CORS Headers
    @app.after_request
    def after_request(response):
        response.headers.add(
            "Access-Control-Allow-Headers",
            "Content-Type, Authorization, true"
        )
        response.headers.add(
            "Access-Control-Allow-Methods",
            "GET,PUT,POST,DELETE,OPTIONS"
        )
        return response





    """
    @OK:
    Create an endpoint to POST a new question,
    which will require the question and answer text,
    category, and difficulty score.

    TEST - OK: When you submit a question on the "Add" tab,
    the form will clear and the question will appear at the end of the last page
    of the questions list in the "List" tab.
    """

    @app.route('/questions', methods=['POST'])
    def create_question():

        # create the data JSON object
        data = request.get_json()

        # create the question_data dictionary from data
        question_data = {
            'question': data['question'],
            'answer': data['answer'],
            'difficulty': data['difficulty'],
            'category': data['category']
        }

        # check if the data is valid
        if (question_data['answer'] != "") &\
                (question_data['question'] != "") &\
                (question_data['category'] is not None) &\
                (question_data['difficulty'] is not None):

            # use the try-except method to insert the data
            try:
                new_question = Question(
                    question=question_data['question'],
                    answer=question_data['answer'],
                    category=question_data['category'],
                    difficulty=question_data['difficulty']
                )

                new_question.insert()

                # query questions
                query_questions = Question.query.order_by(Question.id).all()

                # paginate the query
                questions_paginated = paginate_questions(request, query_questions)

                # return the data
                return jsonify({
                    'success': True,
                    'questions': questions_paginated,
                    'inserted_question': question_data,
                    'total_questions': len(query_questions)
                })

            # if insert fails, abort
            except:
                abort(400)

        # if the data is not valid, abort
        else:
            abort(400)


    """
    @OK:
    Create an endpoint to handle GET requests for questions,
    including pagination (every 10 questions).
    This endpoint should return a list of questions,
    number of total questions, current category, categories.

    TEST - OK: At this point, when you start the application
    you should see questions and categories generated,
    ten questions per page and pagination at the bottom of the screen for three pages.
    Clicking on the page numbers should update the questions.
    """


    @app.route('/questions')
    def read_all_questions():

        # using the try-except method to create the query
        try:

            # create the query questions order by id
            query_questions = Question.query.order_by(Question.id).all()

            # paginate the query
            questions_paginated = paginate_questions(request, query_questions)

            # create query categories
            query_categories = Category.query.order_by(db.desc(Category.id)).all()

            # format the category to frontend
            categories_formatted = {category.id: category.type for category in query_categories}

            # check if the query has no results and abort
            if len(questions_paginated) == 0:
                abort(404)

            # if has results, return them
            else:
                query_categories = {category.id: category.type for category in query_categories}

                return jsonify({
                    'success': True,
                    'questions': questions_paginated,
                    'categories': categories_formatted,
                    'total_questions': len(query_questions),
                    'current_category': ""
                })

        # if the query fails, abort
        except:
            abort(404)


    """
    @OK:
    Create a POST endpoint to get questions to play the quiz.
    This endpoint should take category and previous question parameters
    and return a random questions within the given category,
    if provided, and that is not one of the previous questions.

    TEST - OK: In the "Play" tab, after a user selects "All" or a category,
    one question at a time is displayed, the user is allowed to answer
    and shown whether they were correct or not.
    """

    @app.route('/quizzes', methods=['POST'])
    def read_all_quizzes():

        # using the try-except method to create the queries
        try:
            # create the data JSON object
            data = request.get_json()

            # retrieve the category type from data
            category_type = data['quiz_category']['id']

            # retrieve the previous questions from data
            previous_questions = data['previous_questions']

            # if there is no specific category, query all, except the previous questions
            if category_type == 0:
                query_questions = Question.query.filter(Question.id.notin_(previous_questions)).all()

            # if the category exists, filter by category
            elif category_type:
                query_questions = Question.query.filter(Question.category == category_type ,Question.id.notin_(previous_questions)).all()
            
            # if there are no questions, create an empty result
            if len(query_questions) == 0:
                query_question = Question("","",None, None).format()

            # if there are results select a randon question
            else:
                query_question = random.choice(query_questions).format()

            # check if there is a question and return it
            if query_question:
                return jsonify({
                    'success': True,
                    'question': query_question
                })
                

            # if there are no results, abort
            else:
                abort(422)

        # if the query fails, abort
        except:
            abort(404)


    @app.route('/')
    @app.route('/categories')
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

    @app.route('/categories/<int:category_id>/questions')
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


    """
    @OK:
    Create a POST endpoint to get questions based on a search term.
    It should return any questions for whom the search term
    is a substring of the question.

    TEST - OK: Search by any phrase. The questions list will update to include
    only question that include that string within their question.
    Try using the word "title" to start.
    """

    @app.route('/questions/search', methods=['POST'])
    def search_question():

        # using the try-except method to create the query
        try:

            # create the data JSON object
            data = request.get_json()

            # retrieve the search term from data
            search_term = data['searchTerm']

            # create the query questions filtered by the search term
            query_questions = Question.query.filter(Question.question.ilike('%'+search_term+'%')).all()

            # paginate the query
            questions_paginated = paginate_questions(request, query_questions)

            # check if the query results and return them
            if len(query_questions):

                return jsonify({
                    'success': True,
                    'questions': questions_paginated,
                    'total_questions': len(query_questions),
                    'current_category': ""
                })

            # if there are no results, abort
            else:
                abort(422)

        # if the query fails, abort
        except Exception:
            abort(422)


    """
    @OK:
    Create an endpoint to DELETE question using a question ID.

    TEST - OK: When you click the trash icon next to a question, the question will be removed.
    This removal will persist in the database and when you refresh the page.
    """

    @app.route('/questions/<int:question_id>', methods=['DELETE'])
    def delete_question(question_id):

        # using the try-except method to delete the question
        try:

            # create the query questions with the the question_id
            query_questions = Question.query.get(question_id)

            # if the question is not empty, delete the question
            if query_questions is not None:
                query_questions.delete()

                # create a new query questions with all questions
                query_questions = Question.query.all()

                # paginate the query
                questions_paginated = paginate_questions(request, query_questions)

                # return the JSON object with the paginated questions
                return jsonify({
                    'success': True,
                    'questions': questions_paginated,
                    'total_questions': len(query_questions),
                    'deleted': question_id
                })

            # if the quere is empty, abort
            else:
                abort(422)

        # if the query fails, abort
        except Exception:
            abort(422)


    @app.errorhandler(404)
    def not_found(error):
        return (
            jsonify({"success": False, "error": 404, "message": "resource not found"}),
            404,
        )

    @app.errorhandler(422)
    def unprocessable(error):
        return (
            jsonify({"success": False, "error": 422, "message": "unprocessable"}),
            422,
        )

    @app.errorhandler(400)
    def bad_request(error):
        return jsonify({"success": False, "error": 400, "message": "bad request"}), 400

    @app.errorhandler(405)
    def not_found(error):
        return (
            jsonify({"success": False, "error": 405, "message": "method not allowed"}),
            405,
        )

    return app

