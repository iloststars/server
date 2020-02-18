from exts import db

'''
mysql> create table article(
    -> id int primary key autoincrement,
    -> title varchar(100) not null,
    -> context text not null,
    -> );
'''


# class Article(db.Model):  # 继承db.model
#     __tablename__ = 'article'
#     id = db.Column(db.Integer, primary_key=True, autoincrement=True)
#     title = db.Column(db.String(100), nullable=False)
#     context = db.Column(db.Text, nullable=False)


class Record(db.Model):
    __tablename__ = 'record'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    datetime = db.Column(db.DATETIME, nullable=False)
    flowMeter1 = db.Column(db.Float, nullable=False, default=0)
    deltaFlow1 = db.Column(db.Float, default=0)
    flowMeter2 = db.Column(db.Float, default=0)
    deltaFlow2 = db.Column(db.Float, default=0)
    sumFlow = db.Column(db.Float, default=0)
    waterPressure = db.Column(db.Float, default=0)
    waterLevel = db.Column(db.Float, default=0)
    currentMeter2 = db.Column(db.Float, default=0)
    pumpPressure2 = db.Column(db.Float, default=0)
    wattMeter2 = db.Column(db.Float, default=0)
    deltaWatt2 = db.Column(db.Float, default=0)
    currentMeter4 = db.Column(db.Float, default=0)
    pumpPressure4 = db.Column(db.Float, default=0)
    wattMeter4 = db.Column(db.Float, default=0)
    deltaWatt4 = db.Column(db.Float, default=0)
    frequency4 = db.Column(db.Float, default=0)
    barLift = db.Column(db.Float, default=0)  # 平均扬程
    waterYield = db.Column(db.Float, default=0)  # 产水量
