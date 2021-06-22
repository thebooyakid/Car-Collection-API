import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config():
    """
        Set Config variables for flask app
        Using Environment variables where available
        Otherwise create the cofig variable if it's not done already
    """
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'You will never guess'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False #Turn off update messages from SQLALCHEMY