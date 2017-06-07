from sqlalchemy import Column, func
from sqlalchemy.orm import relationship

from whippet_api.app import db


class Recommendation(db.Model):
    __tablename__ = 'recommendations'

    id = Column(db.Integer, primary_key=True)
    user_id = Column(db.ForeignKey('users.id'), nullable=False, index=True)
    track_id = Column(db.ForeignKey('tracks.id'), nullable=False, index=True)
