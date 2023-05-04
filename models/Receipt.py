import datetime
from database.db import db
class Receipt(db.Model):
    __tablename__='Receipt'
    id = db.Column(db.Integer,primary_key=True)
    number = db.Column(db.String(20), unique=True, nullable=False)
    total = db.Column(db.Float, unique=True, nullable=False)
    registerDate = db.Column(db.DateTime, default=datetime.utcnow)
    status = db.Column(db.Boolean, default=True, nullable=False)