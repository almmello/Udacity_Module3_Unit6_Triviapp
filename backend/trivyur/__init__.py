from flask import Flask, request, abort, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
import random


from config import ProductionConfig

db = SQLAlchemy()

QUESTIONS_PER_PAGE = 10

def create_app():
    # create and configure the app
    app = Flask(__name__)
    app.config.from_object(ProductionConfig)
    
    # setup_db(app)
    db.app = app
    db.init_app(app)
    db.create_all()


    CORS(app)

    # CORS Headers
    @app.after_request
    def after_request(response):
        response.headers.add(
            "Access-Control-Allow-Headers", "Content-Type,Authorization,true"
        )
        response.headers.add(
            "Access-Control-Allow-Methods", "GET,PUT,POST,DELETE,OPTIONS"
        )
        return response
    
    from trivyur.main.routes import main_bp
    from trivyur.categories.routes import categories_bp
    from trivyur.questions.routes import questions_bp
    app.register_blueprint(main_bp)
    app.register_blueprint(categories_bp)
    app.register_blueprint(questions_bp)



    """
    @OK: Set up CORS. Allow '*' for origins. Delete the sample route after completing the TODOs
    """

    """
    @OK: Use the after_request decorator to set Access-Control-Allow
    """

    

    return app

