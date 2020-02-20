# coding=utf-8
from flask_script import Manager
from app import app
from db_script import DBManager
from flask_migrate import Migrate, MigrateCommand
from exts import db

manager = Manager(app)
# 1、绑定app、db
migrate = Migrate(app, db)
# 2、添加命令
manager.add_command('db', MigrateCommand)


@manager.command
def runserver():
    print("running...")


if __name__ == '__main__':
    manager.run()
