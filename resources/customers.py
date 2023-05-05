from flask import Response,request
from flask_restful import Resource
from database.models.customer import Customer
class CustomersAPI(Resource):
    def get(self):
        customers = Customer.query.all()
        return Response(customers,mimetype="application/json",status=200)
class CustomerAPI(Resource):
    def put(self,id):
        body = request.get_json()
        Customer = Customer(name=body['name'],lastName=body['lastName'],)


    
