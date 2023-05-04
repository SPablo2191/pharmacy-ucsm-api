import datetime
from database.db import db
class Customer(db.Model):
    __tablename__='Customer'
    idCustomer = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(20), unique=True, nullable=False)
    lastName = db.Column(db.String(50), unique=True, nullable=False)
    address = db.Column(db.String(100), unique=True, nullable=False)
    phoneNumber = db.Column(db.String(9))
    email = db.Column(db.String(120), unique=True, nullable=False)
    DNI = db.Column(db.String(8))
    status = db.Column(db.Boolean, default=True, nullable=False)
    registerDate = db.Column(db.DateTime, default=datetime.utcnow)