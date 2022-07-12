# Backend - Trivia API

## Setting up the Backend

### Install Dependencies

1. **Python 3.7** - Follow instructions to install the latest version of Python for your platform in the [python docs](https://docs.python.org/3/using/unix.html#getting-and-installing-the-latest-version-of-python)

2. **Virtual Environment** - We recommend working within a virtual environment whenever using Python for projects. This approach keeps your dependencies for each project separate and organized. You can find instructions for setting up a virtual environment for your platform in the [python docs](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/)

```bash
pip3 install virtualenv	  
python3 -m venv venv 	  
source venv/bin/activate  	  
```


3. **PIP Dependencies** - Once your virtual environment is set up and running, install the required dependencies by navigating to the `/backend` directory and running:

```bash
pip install -r requirements.txt
```

#### Key Pip Dependencies

- [Flask](http://flask.pocoo.org/) is a lightweight backend microservices framework. Flask is required to handle requests and responses.

- [SQLAlchemy](https://www.sqlalchemy.org/) is the Python SQL toolkit and ORM we'll use to handle the lightweight SQL database. You'll primarily work in `app. py' and can reference `models.py`.

- [Flask-CORS](https://flask-cors.readthedocs.io/en/latest/#) is the extension we'll use to handle cross-origin requests from our frontend server.

### Set up the Database

With Postgres running, create a `trivia` database:

"`bash
createdb trivia
```

Populate the database using the `trivia.psql` file provided. Then, from the `backend` folder in the terminal, run:

```bash
psql trivia < trivia.psql
```

### Run the Server

From within the `./src` directory, ensure you work using your created virtual environment.

To run the server, execute:

"`bash
flask run --reload
```

The `--reload` flag will detect file changes and restart the server automatically.

## Development from source files

These are the files you'd want to edit in the backend:

1. `backend/flaskr/__init__.py`
2. `backend/flaskr/models.py
2. `backend/test_flaskr.py`

# Achievement

For each endpoint, was defined the endpoint and response data.

1. Used Flask-CORS to enable cross-domain requests and set response headers. => OK
2. Created an endpoint to handle `GET` requests for questions, including pagination (every ten questions). This endpoint returns a list of questions, the number of total questions, and the current category. =>OK
3. Created an endpoint to handle `GET` requests for all available categories. => OK
4. Created an endpoint to `DELETE` a question using a question `ID`. => OK
5. Created an endpoint to `POST` a new question, requiring the question and answer text, category, and difficulty score. => OK
6. Created a `POST` endpoint to get questions based on category. => OK
7. Created a `POST` endpoint to get questions based on a search term. It returns any questions for whom the search term is a substring of the question. => OK
8. Created a `POST` endpoint to get questions to play the quiz. This endpoint takes a category and previous question parameters and returns random questions within the given category if provided and that is not one of the previous questions. => OK
9. Created error handlers for all expected errors, including 400, 404, 405, 422, and 500. => OK

# Endpoints Documentation

Find below the detailed documentation of Trivia app API endpoints, including the URL, request parameters, and the response body.

## Base URL

- Currently, You can only run this app locally.
- The default address, http://127.0.0.1:5000/, is used to host the app backend.

## Authentication: 
This application version does not require authentication or API keys.

## Error Handling

The API returns Errors as JSON objects in the following format:

```
{
    "success": False, 
    "error": 400,
    "message": "bad request"
}
```

The API will return five error types when requests fail:

- 400: Bad Request
- 404: Resource Not Found
- 405: Method not Allowed
- 422: Unprocessable
- 500: Internal Server Error


## GET /questions

### Description:

You can retrieve all the questions. The API returns the list of categories, the list of questions, the success value, and the total number of questions.
The return is paginated in groups of 10.
You can include a request argument to choose page number, starting from 1.

### Sample:

```
curl "http://127.0.0.1:5000/questions?page=1"
```

### Return:

```
{
 "categories": {
  "1": "Science", 
  "2": "Art", 
  "3": "Geography", 
  "4": "History", 
  "5": "Entertainment", 
  "6": "Sports"
 }, 
 "current_category": "", 
 "questions": [
  {
   "answer": "Apollo 13", 
   "category": 5, 
   "difficulty": 4, 
   "id": 2, 
   "question": "What movie earned Tom Hanks his third straight Oscar nomination, in 1996?"
  }, 
  {
   "answer": "Tom Cruise", 
   "category": 5, 
   "difficulty": 4, 
   "id": 4, 
   "question": "What actor did author Anne Rice first denounce, then praise in the role of her beloved Lestat?"
  }, 
  {
   "answer": "Maya Angelou", 
   "category": 4, 
   "difficulty": 2, 
   "id": 5, 
   "question": "Whose autobiography is entitled 'I Know Why the Caged Bird Sings'?"
  }, 
  {
   "answer": "Edward Scissorhands", 
   "category": 5, 
   "difficulty": 3, 
   "id": 6, 
   "question": "What was the title of the 1990 fantasy directed by Tim Burton about a young man with multi-bladed appendages?"
  }, 
  {
   "answer": "Muhammad Ali", 
   "category": 4, 
   "difficulty": 1, 
   "id": 9, 
   "question": "What boxer's original name is Cassius Clay?"
  }, 
  {
   "answer": "Brazil", 
   "category": 6, 
   "difficulty": 3, 
   "id": 10, 
   "question": "Which is the only team to play in every soccer World Cup tournament?"
  }, 
  {
   "answer": "Uruguay", 
   "category": 6, 
   "difficulty": 4, 
   "id": 11, 
   "question": "Which country won the first ever soccer World Cup in 1930?"
  }, 
  {
   "answer": "George Washington Carver", 
   "category": 4, 
   "difficulty": 2, 
   "id": 12, 
   "question": "Who invented Peanut Butter?"
  }, 
  {
   "answer": "Lake Victoria", 
   "category": 3, 
   "difficulty": 2, 
   "id": 13, 
   "question": "What is the largest lake in Africa?"
  }, 
  {
   "answer": "The Palace of Versailles", 
   "category": 3, 
   "difficulty": 3, 
   "id": 14, 
   "question": "In which royal palace would you find the Hall of Mirrors?"
  }
 ], 
 "success": true, 
 "total_questions": 19
}

```

## GET /categories

### Description:

You can retrieve the list of all categories. In addition, the API returns the list of categories and the success value.

### Sample:

```
curl "http://127.0.0.1:5000/categories"
```

### Return:

```
{
 "categories": {
  "1": "Science", 
  "2": "Art", 
  "3": "Geography", 
  "4": "History", 
  "5": "Entertainment", 
  "6": "Sports"
 }, 
 "success": true
}
```

## GET /categories/<int:category_id>/questions

### Description:

You can search for a specific category. The API returns the list of questions, success value, and the total number of questions under a particular category.
The return is paginated in groups of 10.
You can include a request argument to choose page number, starting from 1.

### Sample:

```
curl "http://127.0.0.1:5000/categories/1/questions"
```

### Return:

```
{
  "current_category": "Science", 
  "questions": [
    {
      "answer": "The Liver", 
      "category": 1, 
      "difficulty": 4, 
      "id": 20, 
      "question": "What is the heaviest organ in the human body?"
    }, 
    {
      "answer": "Alexander Fleming", 
      "category": 1, 
      "difficulty": 3, 
      "id": 21, 
      "question": "Who discovered penicillin?"
    }, 
    {
      "answer": "Blood", 
      "category": 1, 
      "difficulty": 4, 
      "id": 22, 
      "question": "Hematology is a branch of medicine involving the study of what?"
    }
  ], 
  "success": true, 
  "total_questions": 3
}
```

## POST /questions

### Description:

You can create a new question using the submitted question, answer, difficulty, and category. The API returns the inserted question, the list of questions, the success value, and the total number of questions.
The return is paginated in groups of 10.
You can include a request argument to choose page number, starting from 1.

### Sample:

```
curl http://127.0.0.1:5000/questions -X POST -H "Content-Type: application/json" -d '{"question": "Who was the first bassist for The Beatles?", "answer": "Stuart Sutcliffe", "difficulty": 3, "category": 2}'
```

### Return:

```
{
 "inserted_question": {
  "answer": "Stuart Sutcliffe", 
  "category": 2, 
  "difficulty": 3, 
  "question": "Who was the first bassist for The Beatles?"
 }, 
 "questions": [
  {
   "answer": "Apollo 13", 
   "category": 5, 
   "difficulty": 4, 
   "id": 2, 
   "question": "What movie earned Tom Hanks his third straight Oscar nomination, in 1996?"
  }, 
  {
   "answer": "Tom Cruise", 
   "category": 5, 
   "difficulty": 4, 
   "id": 4, 
   "question": "What actor did author Anne Rice first denounce, then praise in the role of her beloved Lestat?"
  }, 
  {
   "answer": "Maya Angelou", 
   "category": 4, 
   "difficulty": 2, 
   "id": 5, 
   "question": "Whose autobiography is entitled 'I Know Why the Caged Bird Sings'?"
  }, 
  {
   "answer": "Edward Scissorhands", 
   "category": 5, 
   "difficulty": 3, 
   "id": 6, 
   "question": "What was the title of the 1990 fantasy directed by Tim Burton about a young man with multi-bladed appendages?"
  }, 
  {
   "answer": "Muhammad Ali", 
   "category": 4, 
   "difficulty": 1, 
   "id": 9, 
   "question": "What boxer's original name is Cassius Clay?"
  }, 
  {
   "answer": "Brazil", 
   "category": 6, 
   "difficulty": 3, 
   "id": 10, 
   "question": "Which is the only team to play in every soccer World Cup tournament?"
  }, 
  {
   "answer": "Uruguay", 
   "category": 6, 
   "difficulty": 4, 
   "id": 11, 
   "question": "Which country won the first ever soccer World Cup in 1930?"
  }, 
  {
   "answer": "George Washington Carver", 
   "category": 4, 
   "difficulty": 2, 
   "id": 12, 
   "question": "Who invented Peanut Butter?"
  }, 
  {
   "answer": "Lake Victoria", 
   "category": 3, 
   "difficulty": 2, 
   "id": 13, 
   "question": "What is the largest lake in Africa?"
  }, 
  {
   "answer": "The Palace of Versailles", 
   "category": 3, 
   "difficulty": 3, 
   "id": 14, 
   "question": "In which royal palace would you find the Hall of Mirrors?"
  }
 ], 
 "success": true, 
 "total_questions": 20
}
```

## POST /questions/search

### Description:

You can search for a specific question using the submitted term. The API returns the current category, the list of questions, the success value, and the total number of questions in the result.
The return is paginated in groups of 10.
You can include a request argument to choose page number, starting from 1.

### Sample:

```
curl http://127.0.0.1:5000/questions/search -X POST -H "Content-Type: application/json" -d '{"searchTerm": "tom"}'
```

### Return:

```
{
  "current_category": "", 
  "questions": [
    {
      "answer": "Apollo 13", 
      "category": 5, 
      "difficulty": 4, 
      "id": 2, 
      "question": "What movie earned Tom Hanks his third straight Oscar nomination, in 1996?"
    }
  ], 
  "success": true, 
  "total_questions": 1
}
```

## POST /quizzes

### Description:

You can search for a specific quiz using the submitted category and previous questions. The API returns a random quiz question and the success value in the result.

### Sample:

```
curl http://127.0.0.1:5000/quizzes -X POST -H "Content-Type: application/json" -d '{"previous_questions": [21,22], "quiz_category": {"type": "Science", "id": "1"}}'
```

### Return:

```
{
 "question": {
  "answer": "The Liver", 
  "category": 1, 
  "difficulty": 4, 
  "id": 20, 
  "question": "What is the heaviest organ in the human body?"
 }, 
 "success": true
}

## DELETE /questions/{question_id}

### Description:
You can delete the question of the given ID if it exists.
The API will return the deleted question id, success value, total questions, and questions list based on the current page number to update the frontend.

### Sample:

```python
curl -X DELETE http://127.0.0.1:5000/questions/23
```

### Return:

```
{
 "deleted": 23, 
 "questions": [
  {
   "answer": "Maya Angelou", 
   "category": 4, 
   "difficulty": 2, 
   "id": 5, 
   "question": "Whose autobiography is entitled 'I Know Why the Caged Bird Sings'?"
  }, 
  {
   "answer": "Muhammad Ali", 
   "category": 4, 
   "difficulty": 1, 
   "id": 9, 
   "question": "What boxer's original name is Cassius Clay?"
  }, 
  {
   "answer": "Apollo 13", 
   "category": 5, 
   "difficulty": 4, 
   "id": 2, 
   "question": "What movie earned Tom Hanks his third straight Oscar nomination, in 1996?"
  }, 
  {
   "answer": "Tom Cruise", 
   "category": 5, 
   "difficulty": 4, 
   "id": 4, 
   "question": "What actor did author Anne Rice first denounce, then praise in the role of her beloved Lestat?"
  }, 
  {
   "answer": "Edward Scissorhands", 
   "category": 5, 
   "difficulty": 3, 
   "id": 6, 
   "question": "What was the title of the 1990 fantasy directed by Tim Burton about a young man with multi-bladed appendages?"
  }, 
  {
   "answer": "Brazil", 
   "category": 6, 
   "difficulty": 3, 
   "id": 10, 
   "question": "Which is the only team to play in every soccer World Cup tournament?"
  }, 
  {
   "answer": "Uruguay", 
   "category": 6, 
   "difficulty": 4, 
   "id": 11, 
   "question": "Which country won the first ever soccer World Cup in 1930?"
  }, 
  {
   "answer": "George Washington Carver", 
   "category": 4, 
   "difficulty": 2, 
   "id": 12, 
   "question": "Who invented Peanut Butter?"
  }, 
  {
   "answer": "Lake Victoria", 
   "category": 3, 
   "difficulty": 2, 
   "id": 13, 
   "question": "What is the largest lake in Africa?"
  }, 
  {
   "answer": "The Palace of Versailles", 
   "category": 3, 
   "difficulty": 3, 
   "id": 14, 
   "question": "In which royal palace would you find the Hall of Mirrors?"
  }
 ], 
 "success": true, 
 "total_questions": 19
}
```

## Authors
-Coach Caryn
-Alexandre Monteiro de Mello

## Acknowledgments
-Udacity Full-Stack Web Development Course

# Testing

The test_flaskr.py script uses the Unittest library to test each endpoint success and one error behavior.

To deploy the tests, run:
```bash
dropdb trivia_test
createdb trivia_test
psql trivia_test < trivia.psql
Python test_flaskr.py
```
