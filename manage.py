from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand

from app import app, db
from app.seed import seed_database


migrate = Migrate(app, db)

manager = Manager(app)
manager.add_command('db', MigrateCommand)


@manager.command
def recreate_db():
    db.drop_all()
    db.create_all()
    db.session.commit()


@manager.command
def seed():
    seed_database()


if __name__ == '__main__':
    manager.run()
