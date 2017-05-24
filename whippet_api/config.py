import os


class DefaultConfig(object):
    DEBUG = True

    SQLALCHEMY_ECHO = False
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///db.sqlite'

    JWT_SECRET_KEY = 'secret'
    JWT_VERIFY_EXPIRATION = False
