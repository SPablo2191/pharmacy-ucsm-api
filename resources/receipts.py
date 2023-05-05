from flask import Response, request
from flask_restful import Resource
from functions.receipt_code import generate_invoice_code
from database.models.receipt import Receipt, receipt_schema, receipts_schema
from database.models.receiptDetail import ReceiptDetail,receiptDetail_schema
from database.db import db


class ReceiptsAPI(Resource):
    def get(self):
        receipts = Receipt.query.all()
        return Response(
            receipts_schema.dumps(receipts), mimetype="application/json", status=200
        )

    def post(self):
        customer_id = request.args.get("customer_id")
        branch_id = request.args.get("branch_id")
        body = request.get_json()
        # receipt_dict = receipt_schema.load(body)
        # instancio una nueva facuta
        new_receipt = Receipt(
            number=generate_invoice_code(),
            total=body['total'],
            customer_id=customer_id,
            branch_id=branch_id,
        )
        for detail in body['details']:
            detail_ = receiptDetail_schema.load(detail)
            new_detail = ReceiptDetail(
                unitPrice=detail['unitPrice'],
                quantity=detail['quantity'],
                subTotal=detail['subTotal'],
                product_id=detail['product_id'],
            )
            new_receipt.details.append(new_detail)
        db.session.add(new_receipt)
        db.session.commit()
        return Response(
            'Receipt Register successfully', mimetype="application/json", status=200
        )
