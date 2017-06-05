import csv
import os
import tarfile
import random

from app import db
from models import User, Track, MetaData, Vote


TRACK_DATA_PATH = os.path.join(os.path.dirname(__file__), '../sample_data/tracks_tiny.csv')
TRACK_ARCHIVE_PATH = os.path.join(os.path.dirname(__file__), '../sample_data/tracks.tar.gz')
TRACK_EXTRACT_PATH = os.path.join(os.path.dirname(__file__), '../sample_data')

TRACK_ATTRIBUTES = (
    'artist_name',
    'title',
    'release'
)

META_ATTRIBUTES = (
    'year',
    'artist_familiarity',
    'artist_hotttnesss',
    'artist_latitude',
    'artist_longitude',
    'duration',
    'end_of_fade_in',
    'key',
    'key_confidence',
    'loudness',
    'mode',
    'mode_confidence',
    'song_hotttnesss',
    'start_of_fade_out',
    'tempo',
    'time_signature',
    'time_signature_confidence'
)


def seed_database(user_count = 3):
    user = seed_user()
    seed_tracks()
    seed_votes(user)

    for i in xrange(user_count - 1):
        user = seed_user('demo' + str(i))
        seed_votes(user)


def seed_user(username='demo'):
    user = User(username=username, password='demo')
    db.session.add(user)
    db.session.commit()
    return user


def seed_tracks():
    with open(TRACK_DATA_PATH, 'rb') as csv_file:
        reader = csv.DictReader(csv_file, delimiter=';')
        tracks = []
        meta_data = []
        for data in reader:
            attrs = normalize_attrs(data)
            track_attrs = slice_attrs(attrs, TRACK_ATTRIBUTES)

            meta_attrs = slice_attrs(attrs, META_ATTRIBUTES)
            meta_attrs['artist_hotness'] = meta_attrs.pop('artist_hotttnesss')
            meta_attrs['song_hotness'] = meta_attrs.pop('song_hotttnesss')

            tracks.append(Track(**track_attrs))
            meta_data.append(MetaData(**meta_attrs))

        db.session.add_all(tracks)
        db.session.commit()

        for i, track in enumerate(tracks):
            meta_data[i].track_id = track.id

        db.session.add_all(meta_data)
        db.session.commit()


def seed_votes(user):
    positive = db.session.query(MetaData.track_id, MetaData.year).filter(MetaData.year <= 1990).all()
    negative = db.session.query(MetaData.track_id, MetaData.year).filter(MetaData.year > 1990).all()
    votes = []

    for data in positive:
        if random.random() < 0.2:
            continue
        track_id, _ = data
        votes.append(Vote(user_id=user.id,
                          track_id=track_id,
                          vote_flag=True))

    for data in negative:
        if random.random() < 0.2:
            continue
        track_id, _ = data
        votes.append(Vote(user_id=user.id,
                          track_id=track_id,
                          vote_flag=False))

    db.session.add_all(votes)
    db.session.commit()


def normalize_attrs(data):
    return {k: v.decode('utf-8') for k, v in data.items()}


def slice_attrs(attrs, to_slice):
    return dict([(attr, attrs[attr]) for attr in to_slice])
