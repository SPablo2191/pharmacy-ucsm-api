from datetime import datetime
from database.db import db
from database.db import ma
from .receiptDetail import ReceiptDetailSchema


class Receipt(db.Model):
    __tablename__ = "Receipt"
    id = db.Column(db.Integer, primary_key=True)
    number = db.Column(db.String(20), unique=True, nullable=False)
    total = db.Column(db.Float, nullable=False)
    registerDate = db.Column(db.DateTime, default=datetime.utcnow())
    status = db.Column(db.Boolean, default=True, nullable=False)
    customer_id = db.Column(db.Integer, db.ForeignKey("Customer.id"), nullable=False)
    details = db.relationship("ReceiptDetail", backref="receipt", lazy=True)
    branch_id = db.Column(db.Integer, db.ForeignKey("Branch.id"))
    branch = db.relationship("Branch", backref=db.backref("receipt", uselist=False))


class ReceiptSchema(ma.Schema):
    class Meta:
        model = Receipt
        load_instance = True
        fields = (
            "id",
            "number",
            "total",
            "customer_id",
            "branch_id",
            "status",
            "registerDate"
        )
        details = ma.Nested(ReceiptDetailSchema,many=True)


receipt_schema = ReceiptSchema()
receipts_schema = ReceiptSchema(many=True)
