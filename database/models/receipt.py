from datetime import datetime
from database.db import db
class Receipt(db.Model):
    __tablename__='Receipt'
    id = db.Column(db.Integer,primary_key=True)
    number = db.Column(db.String(20), unique=True, nullable=False)
    total = db.Column(db.Float, nullable=False)
    registerDate = db.Column(db.DateTime, default=datetime.utcnow())
    status = db.Column(db.Boolean, default=True, nullable=False)
    customer_id = db.Column(db.Integer, db.ForeignKey('Customer.id'), nullable=False)
    details = db.relationship('ReceiptDetail', backref='receipt', lazy=True)
    branch_id = db.Column(db.Integer, db.ForeignKey('Branch.id'), unique=True)
    branch = db.relationship('Branch', backref=db.backref('receipt', uselist=False))