#----------------------------------------------------------------------------#
# App Config.
#----------------------------------------------------------------------------#

import os

class Config(object):
    TESTING = False
    SECRET_KEY = os.urandom(32)
    
    # Enable debug mode.
    DEBUG = True


class ProductionConfig(Config):

    database_name = 'trivia'
    database_path = 'postgresql://{}/{}'.format('localhost:5432', database_name)

    # Set SQLALCHEMY Track Notifications
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    
    # OK IMPLEMENT DATABASE URL
    SQLALCHEMY_DATABASE_URI = database_path


class TestingConfig(Config):

    database_name = 'trivia_test'
    database_path = 'postgresql://{}/{}'.format('localhost:5432', database_name)

    # Set SQLALCHEMY Track Notifications
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    
    # OK IMPLEMENT DATABASE URL
    SQLALCHEMY_DATABASE_URI = database_path

    TESTING = True