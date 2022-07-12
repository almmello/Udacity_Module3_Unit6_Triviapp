# API Development and Documentation Final Project

## My Release

This repository is my version of the Trivia app (https://github.com/udacity/cd0037-API-Development-and-Documentation-project).
I recorded my development through commits so that you can follow along.

Please let me know if you find any issues with this project.


## References

During the development, I used the following references to build the Fyyur app:

https://learn.udacity.com/nanodegrees/nd0044/parts/cd0037
https://flask-wtf.readthedocs.io/en/1.0.x/
https://flask.palletsprojects.com/en/2.1.x/
https://flask.palletsprojects.com/en/2.1.x/patterns/packages/
https://flask.palletsprojects.com/en/1.0.x/patterns/flashing/
https://flask-sqlalchemy.palletsprojects.com/en/2.x/models/#
https://flask-moment.readthedocs.io/en/latest/quickstart.html#installation-and-configuration
https://www.digitalocean.com/community/tutorials/how-to-use-flask-sqlalchemy-to-interact-with-databases-in-a-flask-application
https://www.linkedin.com/learning/full-stack-web-development-with-flask/
https://flask.palletsprojects.com/en/2.1.x/testing/
https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-xvi-debugging-testing-and-profiling-legacy
https://testdriven.io/blog/flask-pytest/
https://www.geeksforgeeks.org/read-json-file-using-python/
https://flask.palletsprojects.com/en/1.1.x/errorhandling/#generic-exception-handlers
https://www.twilio.com/blog/environment-variables-python
https://pypi.org/project/python-dotenv/

## Trivia App

The Trivia app is a web app where you can play a trivia game and manage questions among some categories.

## Achievements

Created the routes to:
1. Display all questions by category. Questions show their category and difficulty rating by default and can show/hide the answer.
2. Delete questions.
3. Add questions and require that they include a question and answer text.
4. Search for questions based on a text query string.
5. Play the quiz game, randomizing all questions or within a specific category.

Created the Unit Testing for all routes


## About the Stack

The web app is designed with some key functional areas:

### Backend

The [backend](./backend/README.md) directory contains a partially completed Flask and SQLAlchemy server. You will work primarily in `__init__.py` to define your endpoints and can reference models.py for DB and SQLAlchemy setup. 

These files were edited in the backend:

1. `backend/flaskr/__init__.py`
2. `backend/flaskr/models.py
3. `backend/test_flaskr.py`

> View the [Backend README](./backend/README.md) for more details.

### Frontend

The [frontend](./frontend/README.md) directory contains a complete React frontend to consume the data from the Flask server. 

The backend was developed to be compliant with frontend:
1. Endpoints and HTTP methods the frontend expects to consume.
2. The formatted requests from the frontend and its specific parameters or payloads as expected.

These are the files that I used to find those pieces of information:

1. `frontend/src/components/QuestionView.js`
2. `frontend/src/components/FormView.js`
3. `frontend/src/components/QuizView.js`

> View the [Frontend README](./frontend/README.md) for more details.
