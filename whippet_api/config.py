import os
from datetime import timedelta


class DefaultConfig(object):
    DEBUG = True

    SQLALCHEMY_ECHO = False
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///db.sqlite'

    JWT_SECRET_KEY = 'secret'

    # JWT_VERIFY_EXPIRATION = False
    # Unsupported: https://github.com/mattupstate/flask-jwt/pull/111

    JWT_EXPIRATION_DELTA = timedelta(seconds=31556926)  # 1 year
