
import datetime
from project import db

class Stat(db.Model):

    time = db.Column(db.DateTime,primary_key=True,default=datetime.datetime.now().replace(microsecond=0))
    cpu = db.Column(db.String(10))
    disk = db.Column(db.String(10))
    memory = db.Column(db.String(10))

db.create_all()
