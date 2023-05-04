from datetime import datetime
from database.db import db
class Stock(db.Model):
    __tablename__='Stock'
    id = db.Column(db.Integer,primary_key=True)
    quantity = db.Column(db.Integer)
    status = db.Column(db.Boolean, default=True, nullable=False)
    registerDate = db.Column(db.DateTime, default=datetime.utcnow())
    product_id = db.Column(db.Integer, db.ForeignKey('Product.id'))
    depot_id = db.Column(db.Integer, db.ForeignKey('Depot.id'))
    depot = db.relationship("Depot", backref="stock")