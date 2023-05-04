from datetime import datetime
from database.db import db

class Customer(db.Model):
    __tablename__='Customer'
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(20), nullable=False)
    lastName = db.Column(db.String(50), nullable=False)
    address = db.Column(db.String(100), nullable=False)
    phoneNumber = db.Column(db.String(9))
    email = db.Column(db.String(120), unique=True, nullable=False)
    DNI = db.Column(db.String(8), unique=True, nullable=False)
    status = db.Column(db.Boolean, default=True, nullable=False)
    registerDate = db.Column(db.DateTime, default=datetime.utcnow())
    receipts = db.relationship('Receipt', backref='customer', lazy=True)