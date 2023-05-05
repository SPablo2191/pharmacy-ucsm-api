from flask import Response, request
from flask_restful import Resource
from database.models.product import Product,products_schema,product_schema
from database.db import db

class ProductsAPI(Resource):
    def get(self):
        products = Product.query.all()
        return Response(products_schema.dumps(products), mimetype="application/json", status=200)
    def post(self):
        body = request.get_json()
        new_product = product_schema.load(body)
        db.session.add(new_product)
        db.session.commit()
        return Response(product_schema.dumps(new_product), mimetype="application/json", status=200)



class ProductAPI(Resource):
    def get(self,id):
        existing_product = Product.query.get_or_404(id)
        return Response(product_schema.dumps(existing_product), mimetype="application/json", status=200)
    def put(self, id):
        existing_product = Product.query.get_or_404(id)
        print(existing_product)
        body = request.get_json()
        data = product_schema.load(body,session = db.session)     
        existing_product.name = data.name
        existing_product.description = data.description
        existing_product.price = data.price
        existing_product.status = data.status
        db.session.commit()
        return Response(product_schema.dumps(existing_product), mimetype="application/json", status=200)
    def delete(self,id):
        existing_product = Product.query.get_or_404(id)
        existing_product.status = False
        db.session.commit()
        return Response(product_schema.dumps(existing_product), mimetype="application/json", status=200)
