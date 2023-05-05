from .receipts import ReceiptsAPI
from .customers import CustomersAPI,CustomerAPI
from .products import ProductsAPI,ProductAPI
url = '/api'
def initialize_routes(api):
 api.add_resource(ReceiptsAPI, url+'/receipts')
 api.add_resource(CustomersAPI,url+'/customers')
 api.add_resource(CustomerAPI,url+'/customer/<int:id>')
 api.add_resource(ProductsAPI,url+'/products')
 api.add_resource(ProductAPI,url+'/product/<int:id>')
 