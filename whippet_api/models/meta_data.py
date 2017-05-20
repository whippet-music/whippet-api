from sqlalchemy import Column, func
from sqlalchemy.orm import relationship

from whippet_api.app import db


class MetaData(db.Model):
    __tablename__ = 'meta_data'

    id = Column(db.Integer, primary_key=True)
    track_id = Column(db.ForeignKey('tracks.id'), nullable=False, index=True)
    track = relationship('Track')
    year = Column(db.Integer, nullable=False)
    artist_familiarity = Column(db.Float, nullable=False)
    artist_hotttnesss = Column(db.Float, nullable=False)
    artist_latitude = Column(db.Float, nullable=False)
    artist_longitude = Column(db.Float, nullable=False)
    duration = Column(db.Float, nullable=False)
    end_of_fade_in = Column(db.Float, nullable=False)
    key = Column(db.Integer, nullable=False)
    key_confidence = Column(db.Float, nullable=False)
    loudness = Column(db.Float, nullable=False)
    mode = Column(db.Integer, nullable=False)
    mode_confidence = Column(db.Float, nullable=False)
    song_hotttnesss = Column(db.Float, nullable=False)
    start_of_fade_out = Column(db.Float, nullable=False)
    tempo = Column(db.Float, nullable=False)
    time_signature = Column(db.Integer, nullable=False)
    time_signature_confidence = Column(db.Float, nullable=False)
    created_at = Column(db.DateTime, nullable=False, default=func.now())
    updated_at = Column(db.DateTime, nullable=False, default=func.now(), onupdate=func.now())
