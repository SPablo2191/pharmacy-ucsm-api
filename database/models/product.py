from datetime import datetime
from database.db import db
from database.db import ma

class Product(db.Model):
    __tablename__ = "Product"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), unique=True, nullable=False)
    description = db.Column(db.String(100), nullable=False)
    price = db.Column(db.Float)
    status = db.Column(db.Boolean, default=True, nullable=False)
    registerDate = db.Column(db.DateTime, default=datetime.utcnow())
    stocks = db.relationship("Stock", backref="product", lazy=True)

class ProductSchema(ma.SQLAlchemySchema):
    class Meta:
        model = Product
        load_instance = True
        sqla_session = db.session
        fields = (
            "id",
            "name",
            "description",
            "price",
            "status",
            "registerDate",
        )


product_schema = ProductSchema()
products_schema = ProductSchema(many=True)