from flask import Response,Request
from flask_restful import Resource
from database.models.receipt import Receipt
class ReceiptsAPI(Resource):
    def get(self):
        receipts = Receipt.query.all()
        print(receipts)
        return Response(receipts,mimetype="application/json",status=200)
    
    
