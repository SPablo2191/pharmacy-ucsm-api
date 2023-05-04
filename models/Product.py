import datetime
from database.db import db
class Product(db.Model):
    __tablename__='Product'
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(20), unique=True, nullable=False)
    description = db.Column(db.String(100), nullable=False)
    price = db.Column(db.Float)
    status = db.Column(db.Boolean, default=True, nullable=False)
    registerDate = db.Column(db.DateTime, default=datetime.utcnow)
    