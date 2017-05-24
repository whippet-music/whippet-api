from sqlalchemy import Column, func

from whippet_api.app import db


class Vote(db.Model):
    __tablename__ = 'votes'

    id = Column(db.Integer, primary_key=True)
    user_id = Column(db.ForeignKey('users.id'), nullable=False)
    track_id = Column(db.ForeignKey('tracks.id'), nullable=False)
    vote_flag = Column(db.Boolean, nullable=False)
    created_at = Column(db.DateTime, nullable=False, default=func.now())
    updated_at = Column(db.DateTime, nullable=False, default=func.now(), onupdate=func.now())
