from .receipts import ReceiptsAPI
from .customers import CustomersAPI,CustomerAPI
url = '/api'
def initialize_routes(api):
 api.add_resource(ReceiptsAPI, url+'/receipts')
 api.add_resource(CustomersAPI,url+'/customers')
 api.add_resource(CustomerAPI,url+'/customer/<id>')
 
 