from models import User


def authenticate(username, password):
    user = User.query.filter_by(username=username).first()
    if user and user.verify_password(password):
        return user


def identity(payload):
    user_id = int(payload['identity'])
    return User.query.get(user_id)
