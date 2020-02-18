from flask import Flask
from model import Record
from exts import db
from datetime import datetime
import config

app = Flask(__name__)
app.config.from_object(config)
db.init_app(app)

with app.app_context():
    db.create_all()


@app.route('/')
def hello_world():
    # 增
    # 1、创建Python对象
    recordAdd = Record(datetime=datetime.now())
    # 2、添加到对话
    db.session.add(recordAdd)
    # 3、提交对话
    db.session.commit()

    # #删
    #     #1、查询要删除对象
    # recordDelete= Record.query.filter(Record.id == 1).first()
    #     #2、删除添加到对话
    # db.session.delete(recordDelete)
    #     #3、提交对话
    # db.session.commit()

    # # 改
    #     #1、查询要修改的对象
    # recordUpdate = Record.query.filter(Record.id == 2).first()
    #     #2、修改对象
    # recordUpdate.id = 0
    #     #3、提交对话
    # db.session.commit()

    # # 查
    # recordQuery = Record.query.filter(Record.id == 0).first()

    return 'Hello World!'


if __name__ == '__main__':
    app.run(debug=True)
