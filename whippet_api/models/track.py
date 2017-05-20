from sqlalchemy import Column, func
from sqlalchemy.orm import relationship

from whippet_api.app import db


class Track(db.Model):
    __tablename__ = 'tracks'

    id = Column(db.Integer, primary_key=True)
    artist_name = Column(db.String, nullable=False)
    title = Column(db.String, nullable=False)
    release = Column(db.String, nullable=False)
    meta_data = relationship('MetaData', cascade='delete,save-update')
    created_at = Column(db.DateTime, nullable=False, default=func.now())
    updated_at = Column(db.DateTime, nullable=False, default=func.now(), onupdate=func.now())
