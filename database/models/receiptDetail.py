from datetime import datetime
from database.db import db
from database.db import ma


class ReceiptDetail(db.Model):
    __tablename__ = "ReceiptDetail"
    id = db.Column(db.Integer, primary_key=True)
    receipt_id = db.Column(db.Integer, db.ForeignKey("Receipt.id"))
    quantity = db.Column(db.Integer)
    unitPrice = db.Column(db.Float, nullable=False)
    subTotal = db.Column(db.Float, nullable=False)
    registerDate = db.Column(db.DateTime, default=datetime.utcnow())
    status = db.Column(db.Boolean, default=True, nullable=False)
    product_id = db.Column(db.Integer, db.ForeignKey("Product.id"))
    product = db.relationship("Product", backref="receipt_details")


class ReceiptDetailSchema(ma.Schema):
    class Meta:
        model = ReceiptDetail
        load_instance = True
        sqla_session = db.session
        fields = (
            "id",
            "unitPrice",
            "quantity",
            "subTotal",
            "receipt_id",
            "product_id",
            "status",
            "registerDate",
        )


receiptDetail_schema = ReceiptDetailSchema()
receiptDetails_schema = ReceiptDetailSchema(many=True)
