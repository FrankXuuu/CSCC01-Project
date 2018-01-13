import os
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand

from app import db, app

def load_models():
    from models import Professor
    from models import Student
    from models import QuestionTemplate
    from models import Assignment

app.config.from_object(os.environ['APP_SETTINGS'])

migrate = Migrate(app, db)
manager = Manager(app)

manager.add_command('db', MigrateCommand)


if __name__ == '__main__':
    load_models()
    manager.run()
