# Whippet API

## Setup

Create virtual env for project and install required dependencies:

```bash
mkvirtualenv whippet
pip install -r requirements.txt
```

In order to activate virtual env:

```bash
workon whippet
```

## Management

You can manage application using `manage.py` script. Run `python manage.py --help` to display all available commands.

#### Recreating database

```bash
python manage.py recreate_db
```

#### Database schema migration

```bash
python manage.py db migrate
python manage.py db upgrade
```

Rollback with:

```bash
python manage.py db downgrade
```

#### Seed

We've prepared seed populating sample data for the application.

```bash
python manage.py seed
```

#### Running application server

```bash
python manage.py runserver
```

## Training data preparation

Learning algorithm has been tested using subset of Million Song Dataset. Original dataset contains data with missing or invalid values. In order to sanitize the data from this specific dataset, run:

```bash
python filter_data.py
```

It'll process records from `./sample_data/tracks.csv` file and persist output in `./sample_data/tracks_filtered.csv`.
