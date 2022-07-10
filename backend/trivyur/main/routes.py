#----------------------------------------------------------------------------#
# Imports
#----------------------------------------------------------------------------#
from flask import jsonify, render_template, request, flash, redirect, url_for, Blueprint


from werkzeug.exceptions import HTTPException

#create the blueprint
main_bp = Blueprint('main_bp', __name__)

#----------------------------------------------------------------------------#
# Controllers.
#----------------------------------------------------------------------------#

# from https://flask.palletsprojects.com/en/1.1.x/errorhandling/#generic-exception-handlers
@main_bp.errorhandler(HTTPException)
def handle_exception(e):
    
    # Return JSON instead of HTML for HTTP errors.
    # start with the correct headers and status code from the error
    response = e.get_response()

    # replace the body with JSON
    response.data = jsonify.dumps({
        "success": False,
        "error": e.code,
        "message": e.name,
        "description": e.description,
    })
    response.content_type = "application/json"
    return response

"""
@OK:
Create error handlers for all expected errors
including 404 and 422.
"""