from datetime import datetime
from database.db import db
class Depot(db.Model):
    __tablename__ = 'Depot'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), nullable=False)
    description = db.Column(db.String(20), nullable=False)
    status = db.Column(db.Boolean, default=True, nullable=False)
    registerDate = db.Column(db.DateTime, default=datetime.utcnow())
    branch_id = db.Column(db.Integer, db.ForeignKey('Branch.id'), unique=True)
    branch = db.relationship('Branch', backref='depot', uselist=False)