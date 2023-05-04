import datetime
from database.db import db
class Branch(db.Model):
    __tablename__='Branch'
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(20), unique=True, nullable=False)
    address = db.Column(db.String(100), unique=True, nullable=False)
    status = db.Column(db.Boolean, default=True, nullable=False)
    registerDate = db.Column(db.DateTime, default=datetime.utcnow)