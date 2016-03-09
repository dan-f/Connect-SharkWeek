from flask.ext.script import Manager
from flask.ext.migrate import Migrate, MigrateCommand
from run import app
from flask.ext.sqlalchemy import SQLAlchemy

db = SQLAlchemy()

migrate = Migrate(app, db)

manager = Manager(app)
manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manager.run()
