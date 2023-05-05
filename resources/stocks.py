from flask import Response, request
from flask_restful import Resource
from database.models.stock import Stock,stock_schema,stocks_schema
from database.db import db

class StocksAPI(Resource):
    def get(self):
        product_id = request.args.get('product_id')
        stocks =  Stock.query.filter_by(product_id=product_id).all()
        return Response(stocks_schema.dumps(stocks), mimetype="application/json", status=200)
    def post(self):
        product_id = request.args.get('product_id')
        depot_id = request.args.get('depot_id')
        body = request.get_json()
        new_stock = stock_schema.load(body)
        new_stock.product_id = product_id
        new_stock.depot_id = depot_id
        db.session.add(new_stock)
        db.session.commit()
        return Response(stock_schema.dumps(new_stock), mimetype="application/json", status=200)

# class StockAPI(Resource):
#     def get(self,id):
#         existing_customer = Customer.query.get_or_404(id)
#         return Response(customer_schema.dumps(existing_customer), mimetype="application/json", status=200)
#     def put(self, id):
#         existing_customer = Customer.query.get_or_404(id)
#         body = request.get_json()
#         data = customer_schema.load(body,session = db.session)     
#         existing_customer.name = data.name
#         existing_customer.lastName = data.lastName
#         existing_customer.phoneNumber = data.phoneNumber
#         existing_customer.address = data.address
#         existing_customer.email = data.email
#         existing_customer.status = data.status
#         existing_customer.DNI = data.DNI
#         db.session.commit()
#         return Response(customer_schema.dumps(existing_customer), mimetype="application/json", status=200)
#     def delete(self,id):
#         existing_customer = Customer.query.get_or_404(id)
#         existing_customer.status = False
#         db.session.commit()
#         return Response(customer_schema.dumps(existing_customer), mimetype="application/json", status=200)
