# coding=utf-8
from flask_script import Manager

DBManager = Manager()


@DBManager.command
def init():
    print("init...")


@DBManager.command
def migrate():
    print("migrate...")
