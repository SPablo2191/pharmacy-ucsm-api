from flask import Response, request,make_response
from flask_restful import Resource
from database.models.stock import Stock,stock_schema,stocks_schema
from database.db import db
from sqlalchemy import and_,or_

class StocksAPI(Resource):
    def get(self):
        product_id = request.args.get('product_id')
        stocks =  Stock.query.filter(and_(product_id==product_id,Stock.status==True)).all()
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

class StockAPI(Resource):
    def get(self):
        product_id = request.args.get('product_id')
        depot_id = request.args.get('depot_id')
        stock_id = request.args.get('id')
        existing_stock =  Stock.query.filter(or_(and_(Stock.product_id==product_id,Stock.depot_id==depot_id),Stock.id == stock_id)).all()
        print(existing_stock)
        if existing_stock:
            return Response(stocks_schema.dumps(existing_stock), mimetype="application/json", status=200)
        else:
            return make_response('stock not found', 404)
    def put(self):
        product_id = request.args.get('product_id')
        depot_id = request.args.get('depot_id')
        stock_id = request.args.get('id')
        existing_stock =  Stock.query.filter(or_(and_(Stock.product_id==product_id,Stock.depot_id==depot_id),Stock.id == stock_id)).all()
        if existing_stock:
            body = request.get_json()
            data = stock_schema.load(body,session = db.session) 
            existing_stock[0].quantity = data.quantity
            existing_stock[0].status = data.status
            existing_stock[0].depot_id = data.depot_id
            db.session.commit()  
            return Response(stocks_schema.dumps(existing_stock), mimetype="application/json", status=200)
        else:
            return make_response('stock not found', 404)
    def delete(self):
        product_id = request.args.get('product_id')
        depot_id = request.args.get('depot_id')
        stock_id = request.args.get('id')
        existing_stock =  Stock.query.filter(or_(and_(Stock.product_id==product_id,Stock.depot_id==depot_id),Stock.id == stock_id)).all()
        if existing_stock:
            existing_stock[0].status = False
            db.session.commit()  
            return Response(stocks_schema.dumps(existing_stock), mimetype="application/json", status=200)
        else:
            return make_response('stock not found', 404)
