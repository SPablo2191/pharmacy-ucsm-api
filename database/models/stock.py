from datetime import datetime
from database.db import db
from database.db import ma


class Stock(db.Model):
    __tablename__ = "Stock"
    id = db.Column(db.Integer, primary_key=True)
    quantity = db.Column(db.Integer)
    status = db.Column(db.Boolean, default=True, nullable=False)
    registerDate = db.Column(db.DateTime, default=datetime.utcnow())
    product_id = db.Column(db.Integer, db.ForeignKey("Product.id"))
    depot_id = db.Column(db.Integer, db.ForeignKey("Depot.id"))
    depot = db.relationship("Depot", backref="stocks")


class StockSchema(ma.SQLAlchemySchema):
    class Meta:
        model = Stock
        load_instance = True
        sqla_session = db.session
        fields = (
            "id",
            "quantity",
            "status",
            "depot_id",
            "product_id",
            "registerDate",
        )


stock_schema = StockSchema()
stocks_schema = StockSchema(many=True)
