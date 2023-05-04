import datetime
from database.db import db
class Depot(db.Model):
    __tablename__='Depot'
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(20), unique=True, nullable=False)
    description = db.column(db.String(20), nullable=False)
    status = db.Column(db.Boolean, default=True, nullable=False)
    registerDate = db.Column(db.DateTime, default=datetime.utcnow)
    