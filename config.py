# coding=utf-8
# dialect+driver://username:password@host:port/database

DIALECT = "mysql"
DRIVER = "mysqlconnector"
USERNAME = "test"
PASSWORD = "0000"
HOST = "127.0.0.1"
PORT = "3306"
DATABASE = "second_pump"

SQLALCHEMY_DATABASE_URI = "{}+{}://{}:{}@{}:{}/{}?charset=utf8".format(DIALECT, DRIVER, USERNAME, PASSWORD, HOST, PORT,
                                                                       DATABASE)
SQLALCHEMY_TRACK_MODIFICATIONS = False
