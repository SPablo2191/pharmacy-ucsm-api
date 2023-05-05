from .receipts import ReceiptsAPI
from .customers import CustomersAPI
url = '/api'
def initialize_routes(api):
 api.add_resource(ReceiptsAPI, url+'/receipts')
 api.add_resource(CustomersAPI,url+'/customers')
 