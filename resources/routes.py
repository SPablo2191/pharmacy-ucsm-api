from .receipts import ReceiptsAPI,ReceiptAPI
from .customers import CustomersAPI,CustomerAPI
from .products import ProductsAPI,ProductAPI
from .branchs import BranchsAPI,BranchAPI
from .depots import DepotsAPI
from .stocks import StocksAPI,StockAPI
url = '/api'
def initialize_routes(api):
 api.add_resource(ReceiptsAPI, url+'/receipts')
 api.add_resource(ReceiptAPI, url+'/receipt/<int:id>')
 api.add_resource(CustomersAPI,url+'/customers')
 api.add_resource(CustomerAPI,url+'/customer/<int:id>')
 api.add_resource(ProductsAPI,url+'/products')
 api.add_resource(ProductAPI,url+'/product/<int:id>')
 api.add_resource(StocksAPI,url+'/stocks')
 api.add_resource(StockAPI,url+'/stock')
 api.add_resource(BranchsAPI,url+'/branchs')
 api.add_resource(BranchAPI,url+'/branch/<int:id>')
 api.add_resource(DepotsAPI,url+'/branch/<int:id>/depots')

 