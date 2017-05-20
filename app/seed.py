from app import db

from models import User


def seed_database():
    demo_user = User(username='demo', password='demo')
    db.session.add(demo_user)
    db.session.commit()
