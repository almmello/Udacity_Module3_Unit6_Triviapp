import os
import unittest
import json
from flask_sqlalchemy import SQLAlchemy

from trivyur import create_app
from trivyur.categories.models import Category
from trivyur.questions.models import Question
from trivyur.questions.routes import paginate_questions

from config import TestingConfig


class TriviaTestCase(unittest.TestCase):
    """This class represents the trivia test case"""

    def setUp(self):
        """Define test variables and initialize app."""
        self.app = create_app(config_class=TestingConfig)
        self.client = self.app.test_client
        
        # binds the app to the current context
        with self.app.app_context():
            self.db = SQLAlchemy()
            self.db.init_app(self.app)
            # create all tables
            self.db.create_all()

        self.new_question = {
            "question": "Who was the first bassist for The Beatles?",
            "answer": "Stuart Sutcliffe",
            "difficulty": 3,
            "category": 2
        }
    
    def tearDown(self):
        """Executed after reach test"""
        pass

    """
    OK
    Write at least one test for each test for successful operation and for expected errors.
    """

    def test_create_question(self):

        # Define questions route
        res = self.client().post('/questions', json=self.new_question)
        
        # create the data dictionary from the URL request
        data = json.loads(res.data)
        
        # Check request return
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertEqual(data['inserted_question']['question'], self.new_question.question)
        self.assertEqual(data['inserted_question']['answer'], self.new_question.answer)
        self.assertEqual(data['inserted_question']['difficulty'], self.new_question.difficulty)
        self.assertEqual(data['inserted_question']['category'], self.new_question.category)

        # Check return data
        self.assertTrue(len(data['questions']))
        self.assertTrue(data['total_questions'])


    def test_create_question_method_not_allowed(self):

        # Define questions route with wrong URL
        res = self.client().post('/questions/1000', json=self.new_question)

        # create the data dictionary from the URL request
        data = json.loads(res.data)

        # Check request return
        self.assertEqual(res.status_code, 405)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'method not allowed')


    def test_read_all_questions(self):
        # Define questions route
        res = self.client().get('/questions')

        # create the data dictionary from the URL request
        data = json.loads(res.data)

        # Check request return
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertEqual(data['total_questions'],19)
        self.assertEqual(data['current_category'],"")

        # Check return data
        self.assertTrue(len(data['questions']))
        self.assertTrue(len(data['categories']))
        self.assertTrue(data['total_questions'])


    def test_read_all_questions_not_found(self):

        # Define questions route with page out of range
        res = self.client().get('/questions?page=1000')

        # Read data
        data = json.loads(res.data)

        # Check request return
        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'Not found')


    def test_read_all_categories(self):
        # Define categories route
        res = self.client().get('/questions')
        
        # create the data dictionary from the URL request
        data = json.loads(res.data)
        
        # Check request return
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertEqual(data['total_questions'],19)
        self.assertEqual(data['current_category'],"")

        # Check return data
        self.assertTrue(len(data['questions']))
        self.assertTrue(len(data['categories']))
        self.assertTrue(data['total_questions'])


    def test_read_all_categories_not_found(self):

        # Define questions route with page out of range
        res = self.client().get('/questions?page=1000')

        # create the data dictionary from the URL request
        data = json.loads(res.data)

        # Check request return
        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'Not found')


    def test_read_all_quizzes(self):

        # create a privious questions list
        previous_questions = [1, 2]

        # Define quizzes route
        res = self.client().post('/quizzes', json={'quiz_category': 1, 'previous_questions': previous_questions})

        # create the data dictionary from the URL request
        data = json.loads(res.data)
        
        # Check request return
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)

        # Check return data
        self.assertTrue(data['questions'])
        self.assertTrue(data['question'])
        self.assertTrue(data['question']['id'] not in previous_questions)


    def test_read_all_quizzes_not_found(self):

        # create a privious questions list
        previous_questions = [1, 2]

        # Define quizzes route with wrong category
        res = self.client().post('/quizzes', json={'quiz_category': 1000, 'previous_questions': previous_questions})

        # create the data dictionary from the URL request
        data = json.loads(res.data)

        # Check request return
        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'Not found')


    def test_read_single_category(self):
        # Define questions route
        res = self.client().get('/categories/3/questions')
        
        # create the data dictionary from the URL request
        data = json.loads(res.data)
        
        # Check request return
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertEqual(data['total_questions'],3)
        self.assertEqual(data['current_category'],'Geography')
        
        # Check return data
        self.assertTrue(len(data['questions']))
        self.assertTrue(data['total_questions'])
        
        
    def test_read_single_category_unprocessable(self):
        # Define questions route
        res = self.client().get('/categories/1000/questions')
        
        # create the data dictionary from the URL request
        data = json.loads(res.data)
        
        # Check request return
        self.assertEqual(res.status_code, 422)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'Unprocessable Entity')
        
        # Check return data
        self.assertTrue(len(data['questions']))
        self.assertTrue(data['total_questions'])


    def test_search_question(self):

        # Define questions route
        res = self.client().post('/questions/search', json={'searchTerm': 'tom'})
        
        # create the data dictionary from the URL request
        data = json.loads(res.data)
        
        # create a query for questions using the same term in the route
        query_questions = Question.query.filter(Question.question.ilike('%tom%')).all()
        
        # paginate the query
        questions_paginated = paginate_questions(query_questions)
        
        # Check request return
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertEqual(len(data['questions_paginated']), len(questions_paginated))
        
        # Check return data
        self.assertTrue(data['total_questions'])
    

    def test_search_question_without_results(self):

        # Define questions route
        res = self.client().post('/questions/search', json={'searchTerm': 'qweasdzxc'})

        # create the data dictionary from the URL request
        data = json.loads(res.data)

        # Check request return
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertEqual(len(data['questions']), 0)

        # Check return data
        self.assertTrue(data['total_questions'])


    def test_delete_question(self):

        # Define questions route
        res = self.client().delete('/questions/7')
        
        # create the data dictionary from the URL request
        data = json.loads(res.data)
        
        # create a query for questions using id used in the route
        query_questions = Question.query.filter(Question.id == 7).one_or_none()
        
        # Check request return
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertEqual(data['deleted'], 7)
        
        # Check return data
        self.assertTrue(len(data['questions']))
        self.assertTrue(data['total_questions'])
        
        # check if the question was deleted
        self.assertFalse(query_questions)
    

    def test_delete_question_unprocessable(self):

        # Define questions route
        res = self.client().delete('/books/1000')

        # create the data dictionary from the URL request
        data = json.loads(res.data)

        # Check request return
        self.assertEqual(res.status_code, 422)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'unprocessable')


    
# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()