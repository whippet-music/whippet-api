from sqlalchemy import Column, func
from werkzeug.security import check_password_hash, generate_password_hash

from whippet_api.app import db


class User(db.Model):
    __tablename__ = 'users'

    id = Column(db.Integer, primary_key=True)
    username = Column(db.String(80), nullable=False, unique=True, index=True)
    password_hash = Column(db.String(120), nullable=False)
    created_at = Column(db.DateTime, nullable=False, default=func.now())
    updated_at = Column(db.DateTime, nullable=False, default=func.now(), onupdate=func.now())

    @property
    def password(self):
        raise AttributeError('`password` is not a readable attribute')

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)
