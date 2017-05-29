import csv
import os
import tarfile

from app import db
from models import User, Track


TRACK_DATA_PATH = os.path.join(os.path.dirname(__file__), '../sample_data/tracks.csv')
TRACK_ARCHIVE_PATH = os.path.join(os.path.dirname(__file__), '../sample_data/tracks.tar.gz')
TRACK_EXTRACT_PATH = os.path.join(os.path.dirname(__file__), '../sample_data')
TRACK_ATTRIBUTES = ('artist_name', 'title', 'release')


def seed_database():
    seed_user()
    seed_tracks()


def seed_user():
    demo_user = User(username='demo', password='demo')
    db.session.add(demo_user)
    db.session.commit()


def seed_tracks():
    if not os.path.isfile(TRACK_DATA_PATH):
        tar = tarfile.open(TRACK_ARCHIVE_PATH)
        member = tar.getmember("tracks.csv")
        tar.extract(member, path=TRACK_EXTRACT_PATH)
        tar.close()

    with open(TRACK_DATA_PATH, 'rb') as tracks_file:
        reader = csv.DictReader(tracks_file, delimiter=';')
        all_attrs = reader.fieldnames
        for track_data in reader:
            track_attrs = {k: v.decode('utf-8') for k, v in slice_dict(track_data, TRACK_ATTRIBUTES).items()}
            db.session.add(Track(**track_attrs))

        db.session.commit()


def slice_dict(d, attrs):
    return dict([(attr, d[attr]) for attr in attrs])
