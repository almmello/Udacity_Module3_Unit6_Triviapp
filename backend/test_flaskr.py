import os
import unittest
import json
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv

from flaskr import create_app
from models import setup_db, Question, Category


# add all the variable definitions in it to the os.environ dictionary
load_dotenv()


# Create pagination method for testing
def paginate_questions(data):

    # applies the Question.format method on data received
    items = [item.format() for item in data]

    # creates the return dictionary from zero to 10
    return items[0:10]


class TriviaTestCase(unittest.TestCase):
    """This class represents the trivia test case"""

    def setUp(self):
        """Define test variables and initialize app."""
        self.app = create_app()
        self.client = self.app.test_client
        self.database_name = os.getenv("DATABASE_TEST_NAME")
        self.database_user = os.getenv("DATABASE_USER")
        self.database_password = os.getenv("DATABASE_PASSWORD")
        self.database_path = f"postgresql://{self.database_user}:{self.database_password}@localhost:5432/{self.database_name}"
        setup_db(self.app, self.database_path)

        # binds the app to the current context
        with self.app.app_context():
            self.db = SQLAlchemy()
            self.db.init_app(self.app)
            # create all tables
            self.db.create_all()

        self.question = "Who was the first bassist for The Beatles?"
        self.answer = "Stuart Sutcliffe"
        self.difficulty = 3
        self.category = 2

        self.new_question = {
            "question": "Who was the first bassist for The Beatles?",
            "answer": "Stuart Sutcliffe",
            "difficulty": 3,
            "category": 2,
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
        res = self.client().post("/questions", json=self.new_question)

        # create the data dictionary from the URL request
        data = json.loads(res.data)

        # Check request return
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data["success"], True)
        self.assertEqual(data["inserted_question"]["question"], self.question)
        self.assertEqual(data["inserted_question"]["answer"], self.answer)
        self.assertEqual(data["inserted_question"]["difficulty"], self.difficulty)
        self.assertEqual(data["inserted_question"]["category"], self.category)

        # Check return data
        self.assertTrue(len(data["questions"]))
        self.assertTrue(data["total_questions"])

    def test_create_question_bad_request(self):

        # Set an empty question to test
        self.new_question["question"] = ""

        # Define questions route with wrong URL
        res = self.client().post("/questions", json=self.new_question)

        # create the data dictionary from the URL request
        data = json.loads(res.data)

        # Check request return
        self.assertEqual(res.status_code, 400)
        self.assertEqual(data["success"], False)
        self.assertEqual(data["message"], "bad request")

    def test_read_all_questions(self):
        # Define questions route
        res = self.client().get("/questions")

        # create the data dictionary from the URL request
        data = json.loads(res.data)

        # Check request return
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data["success"], True)
        self.assertEqual(data["total_questions"], 19)
        self.assertEqual(data["current_category"], "")

        # Check return data
        self.assertTrue(len(data["questions"]))
        self.assertTrue(len(data["categories"]))
        self.assertTrue(data["total_questions"])

    def test_read_all_questions_not_found(self):

        # Define questions route with page out of range
        res = self.client().get("/questions?page=1000")

        # Read data
        data = json.loads(res.data)

        # Check request return
        self.assertEqual(res.status_code, 404)
        self.assertEqual(data["success"], False)
        self.assertEqual(data["message"], "resource not found")

    def test_read_all_categories(self):
        # Define categories route
        res = self.client().get("/categories")

        # create the data dictionary from the URL request
        data = json.loads(res.data)

        # Check request return
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data["success"], True)

        # Check return data
        self.assertTrue(len(data["categories"]))

    def test_read_all_quizzes(self):

        # create a privious questions list
        previous_questions = [20, 21]

        # Define quizzes route
        res = self.client().post(
            "/quizzes",
            json={
                "previous_questions": previous_questions,
                "quiz_category": {"type": "Science", "id": "1"},
            },
        )

        # create the data dictionary from the URL request
        data = json.loads(res.data)

        # Check request return
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data["success"], True)

        # Check return data
        self.assertTrue(data["question"])
        self.assertTrue(data["question"]["id"] not in previous_questions)

    def test_read_all_quizzes_not_found(self):

        # create a privious questions list
        previous_questions = [1, 2]

        # Define quizzes route with wrong category
        res = self.client().post(
            "/quizzes",
            json={"previous_questions": previous_questions, "quiz_category": 1},
        )

        # create the data dictionary from the URL request
        data = json.loads(res.data)

        # Check request return
        self.assertEqual(res.status_code, 404)
        self.assertEqual(data["success"], False)
        self.assertEqual(data["message"], "resource not found")

    def test_read_single_category(self):
        # Define questions route
        res = self.client().get("/categories/3/questions")

        # create the data dictionary from the URL request
        data = json.loads(res.data)

        # Check request return
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data["success"], True)
        self.assertEqual(data["total_questions"], 3)
        self.assertEqual(data["current_category"], "Geography")

        # Check return data
        self.assertTrue(len(data["questions"]))
        self.assertTrue(data["total_questions"])

    def test_read_single_category_unprocessable(self):
        # Define questions route
        res = self.client().get("/categories/1000/questions")

        # create the data dictionary from the URL request
        data = json.loads(res.data)

        # Check request return
        self.assertEqual(res.status_code, 422)
        self.assertEqual(data["success"], False)
        self.assertEqual(data["message"], "unprocessable")

    def test_search_question(self):

        # Define questions route
        res = self.client().post("/questions/search", json={"searchTerm": "tom"})

        # create the data dictionary from the URL request
        data = json.loads(res.data)

        # create a query for questions using the same term in the route
        query_questions = Question.query.filter(Question.question.ilike("%tom%")).all()

        # paginate the query
        questions_paginated = paginate_questions(query_questions)

        # Check request return
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data["success"], True)
        self.assertEqual(len(data["questions"]), len(questions_paginated))

        # Check return data
        self.assertTrue(data["total_questions"])

    def test_search_question_without_results(self):

        # Define questions route
        res = self.client().post("/questions/search", json={"searchTerm": "qweasdzxc"})

        # create the data dictionary from the URL request
        data = json.loads(res.data)

        # Check request return
        self.assertEqual(res.status_code, 422)
        self.assertEqual(data["success"], False)
        self.assertEqual(data["message"], "unprocessable")

    def test_delete_question(self):

        # Define questions route
        res = self.client().delete("/questions/23")

        # create the data dictionary from the URL request
        data = json.loads(res.data)

        # create a query for questions using id used in the route
        query_questions = Question.query.filter(Question.id == 23).one_or_none()

        # Check request return
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data["success"], True)
        self.assertEqual(data["deleted"], 23)

        # Check return data
        self.assertTrue(len(data["questions"]))
        self.assertTrue(data["total_questions"])

        # check if the question was deleted
        self.assertFalse(query_questions)

    def test_delete_question_unprocessable(self):

        # Define questions route
        res = self.client().delete("/questions/1000")

        # create the data dictionary from the URL request
        data = json.loads(res.data)

        # Check request return
        self.assertEqual(res.status_code, 422)
        self.assertEqual(data["success"], False)
        self.assertEqual(data["message"], "unprocessable")


# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()
