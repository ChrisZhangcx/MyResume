# -*- coding:utf-8 -*-
from app import create_app, db
from app.models import User, MajorInfo, ClassInfo, SC, CS, CE, CER, CountResult, ClassResult
from flask_script import Manager, Shell
from flask_migrate import Migrate, MigrateCommand
from flask_frozen import Freezer
import sys


app = create_app('default')
manager = Manager(app)
migrate = Migrate(app, db)
freezer = Freezer(app)


def make_shell_context():
    return dict(app=app, db=db, User=User, MajorInfo=MajorInfo, ClassInfo=ClassInfo, SC=SC, CS=CS, CE=CE,
                CER=CER, CountResult=CountResult, ClassResult=ClassResult)
manager.add_command("shell", Shell(make_context=make_shell_context))
manager.add_command('db', MigrateCommand)


if __name__ == '__main__':
    if len(sys.argv) > 1 and sys.argv[1] == "build":
        freezer.freeze()
    else:
        app.run(port=5000)
