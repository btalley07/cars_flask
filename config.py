import os

basedir = os.path.abspath(os.path.dirname(__file__))

#give access to the project in any os, allow outside files/folders
# to be added to the project from the base directory 

class Config():
    """
        set config variables for the flask app
        using environment variables where availables
        otherwise create the config variable if not done already
    """
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'You will never guess'
    SQLACLCHEMY_DATABASE_URI = os.environ.get('DATABASE_URI') or 'solite:///' + os.path.join(basedir, 'app.ob')
    SQLALCHEMY_TRACK_MODIFICATIONS = False #turn off update messages from sqlalchemy
    