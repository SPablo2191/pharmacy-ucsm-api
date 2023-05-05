from flask import Response, request
from flask_restful import Resource
from database.models.customer import Customer,customers_schema,customer_schema
from database.db import db

class CustomersAPI(Resource):
    def get(self):
        customers = Customer.query.all()
        return Response(customers_schema.dumps(customers), mimetype="application/json", status=200)
    def post(self):
        body = request.get_json()
        new_customer = customer_schema.load(body)
        db.session.add(new_customer)
        db.session.commit()
        return Response(customer_schema.dumps(new_customer), mimetype="application/json", status=200)



class CustomerAPI(Resource):
    def get(self,id):
        existing_customer = Customer.query.get_or_404(id)
        return Response(customer_schema.dumps(existing_customer), mimetype="application/json", status=200)
    def put(self, id):
        existing_customer = Customer.query.get_or_404(id)
        body = request.get_json()
        data = customer_schema.load(body,session = db.session)     
        existing_customer.name = data.name
        existing_customer.lastName = data.lastName
        existing_customer.phoneNumber = data.phoneNumber
        existing_customer.address = data.address
        existing_customer.email = data.email
        existing_customer.status = data.status
        existing_customer.DNI = data.DNI
        db.session.commit()
        return Response(customer_schema.dumps(existing_customer), mimetype="application/json", status=200)
    def delete(self,id):
        existing_customer = Customer.query.get_or_404(id)
        existing_customer.status = False
        db.session.commit()
        return Response(customer_schema.dumps(existing_customer), mimetype="application/json", status=200)
