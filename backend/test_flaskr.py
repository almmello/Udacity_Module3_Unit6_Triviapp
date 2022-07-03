import os
import unittest
import json
from flask_sqlalchemy import SQLAlchemy

from trivyur import create_app
from trivyur.categories.models import Category
from trivyur.questions.models import Question

from config import Config_Test


class TriviaTestCase(unittest.TestCase):
    """This class represents the trivia test case"""

    def setUp(self):
        """Define test variables and initialize app."""
        self.app = create_app(config_class=Config_Test)
        self.client = self.app.test_client
        
                # binds the app to the current context
        with self.app.app_context():
            self.db = SQLAlchemy()
            self.db.init_app(self.app)
            # create all tables
            self.db.create_all()
    
    def tearDown(self):
        """Executed after reach test"""
        pass

    """
    TODO
    Write at least one test for each test for successful operation and for expected errors.
    """


# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()