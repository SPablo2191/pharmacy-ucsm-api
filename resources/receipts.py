from flask import Response, request, jsonify
from flask_restful import Resource
from functions.receipt_code import generate_invoice_code
from database.models.receipt import Receipt, receipt_schema, receipts_schema
from database.models.receiptDetail import ReceiptDetail, receiptDetail_schema
from database.db import db
from sqlalchemy import and_, or_
import json


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
            total=body["total"],
            customer_id=customer_id,
            branch_id=branch_id,
        )
        for detail in body["details"]:
            detail_ = receiptDetail_schema.load(detail)
            new_detail = ReceiptDetail(
                unitPrice=detail["unitPrice"],
                quantity=detail["quantity"],
                subTotal=detail["subTotal"],
                product_id=detail["product_id"],
            )
            new_receipt.details.append(new_detail)
        db.session.add(new_receipt)
        db.session.commit()
        return Response(
            "Receipt Register successfully", mimetype="application/json", status=200
        )


class ReceiptAPI(Resource):
    def get(self, id):
        existing_receipt = Receipt.query.get_or_404(id)
        details = ReceiptDetail.query.filter(
            ReceiptDetail.receipt_id == existing_receipt.id
        ).all()
        existing_receipt.details = details
        receipt_selected = json.loads(receipt_schema.dumps(existing_receipt))
        print(receipt_selected)
        aux = []
        for detail in details:
            aux_detail = {
                "id": detail.id,
                "quantity": detail.quantity,
                "unitPrice": detail.unitPrice,
                "subTotal" : detail.subTotal,
                "product_id": detail.product_id
            }

            aux.append(aux_detail)
        receipt_selected["details"] = aux
        return receipt_selected
    def delete(self,id):
        existing_receipt = Receipt.query.get_or_404(id)
        existing_receipt.status = False
        db.session.commit()
        return Response(receipt_schema.dumps(existing_receipt), mimetype="application/json", status=200)
