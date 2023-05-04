import datetime
from database.db import db
class Stock(db.Model):
    __tablename__='Stock'
    id = db.Column(db.Integer,primary_key=True)
    quantity = db.Column(db.Integer)
    status = db.Column(db.Boolean, default=True, nullable=False)
    registerDate = db.Column(db.DateTime, default=datetime.utcnow)