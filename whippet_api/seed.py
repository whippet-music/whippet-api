import csv
import os

from app import db
from models import User, Track


TRACK_DATA_PATH = os.path.join(os.path.dirname(__file__), '../sample_data/tracks.csv')
TRACK_ATTRIBUTES = ('artist_name', 'title', 'release')


def seed_database():
    seed_user()
    seed_tracks()


def seed_user():
    demo_user = User(username='demo', password='demo')
    db.session.add(demo_user)
    db.session.commit()


def seed_tracks():
    with open(TRACK_DATA_PATH, 'rb') as tracks_file:
        reader = csv.DictReader(tracks_file, delimiter=';')
        all_attrs = reader.fieldnames
        for track_data in reader:
            track_attrs = slice_dict(track_data, TRACK_ATTRIBUTES)
            db.session.add(Track(**track_attrs))
            db.session.commit()


def slice_dict(d, attrs):
    return dict([(attr, d[attr]) for attr in attrs])
