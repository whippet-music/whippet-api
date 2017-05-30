import csv
import os
import tarfile

from app import db
from models import User, Track, MetaData


TRACK_DATA_PATH = os.path.join(os.path.dirname(__file__), '../sample_data/tracks.csv')
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


def seed_database():
    # seed_user()
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

    with open(TRACK_DATA_PATH, 'rb') as csv_file:
        reader = csv.DictReader(csv_file, delimiter=';')
        tracks = []
        meta_data = []
        counter = 0
        for data in reader:
            attrs = normalize_attrs(data)
            track_attrs = slice_attrs(attrs, TRACK_ATTRIBUTES)

            meta_attrs = slice_attrs(attrs, META_ATTRIBUTES)
            meta_attrs['artist_hotness'] = meta_attrs.pop('artist_hotttnesss')
            meta_attrs['song_hotness'] = meta_attrs.pop('song_hotttnesss')

            tracks.append(Track(**track_attrs))
            meta_data.append(MetaData(**meta_attrs))

            counter += 1
            if counter % 1000 == 0:
                db.session.add_all(tracks)
                db.session.commit()

                for i, track in enumerate(tracks):
                    meta_data[i].track_id = track.id

                db.session.add_all(meta_data)
                db.session.commit()

                del tracks[:]
                del meta_data[:]

                print counter


def normalize_attrs(data):
    return {k: v.decode('utf-8') for k, v in data.items()}


def slice_attrs(attrs, to_slice):
    return dict([(attr, attrs[attr]) for attr in to_slice])
