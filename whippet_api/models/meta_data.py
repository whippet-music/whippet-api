from sqlalchemy import Column, func
from sqlalchemy.orm import relationship

from whippet_api.app import db


class MetaData(db.Model):
    __tablename__ = 'meta_data'

    id = Column(db.Integer, primary_key=True)
    track_id = Column(db.ForeignKey('tracks.id'), nullable=False, index=True)
    track = relationship('Track')
    year = Column(db.Integer)
    artist_familiarity = Column(db.Float)
    artist_hotness = Column(db.Float)
    artist_latitude = Column(db.Float)
    artist_longitude = Column(db.Float)
    duration = Column(db.Float)
    end_of_fade_in = Column(db.Float)
    key = Column(db.Integer)
    key_confidence = Column(db.Float)
    loudness = Column(db.Float)
    mode = Column(db.Integer)
    mode_confidence = Column(db.Float)
    song_hotness = Column(db.Float)
    start_of_fade_out = Column(db.Float)
    tempo = Column(db.Float)
    time_signature = Column(db.Integer)
    time_signature_confidence = Column(db.Float)
    created_at = Column(db.DateTime, nullable=False, default=func.now())
    updated_at = Column(db.DateTime, nullable=False, default=func.now(), onupdate=func.now())
