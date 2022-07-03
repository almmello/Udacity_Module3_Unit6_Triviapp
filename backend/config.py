#----------------------------------------------------------------------------#
# App Config.
#----------------------------------------------------------------------------#

import os


class Config(object):
    SECRET_KEY = os.urandom(32)
    
    # Enable debug mode.
    DEBUG = True

    database_name = 'trivia'
    database_path = 'postgres://{}/{}'.format('localhost:5432', database_name)

    # Set SQLALCHEMY Track Notifications
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    
    # OK IMPLEMENT DATABASE URL
    SQLALCHEMY_DATABASE_URI = database_path


class Config_Test(object):
    SECRET_KEY = os.urandom(32)
    
    # Enable debug mode.
    DEBUG = True

    database_name = 'trivia_test'
    database_path = 'postgres://{}/{}'.format('localhost:5432', database_name)

    # Set SQLALCHEMY Track Notifications
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    
    # OK IMPLEMENT DATABASE URL
    SQLALCHEMY_DATABASE_URI = database_path