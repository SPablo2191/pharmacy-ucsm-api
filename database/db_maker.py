import os
from .db import db
from .models.branch import Branch
from .models.customer import Customer
from .models.depot import Depot
from .models.product import Product
from .models.receipt import Receipt
from .models.receiptDetail import ReceiptDetail
from .models.stock import Stock
def create_db(app):
    """verificar si las tablas ya fueron creadas"""
    if not os.environ.get('TABLES_CREATED'):
        with app.app_context():
            db.create_all()
        os.environ['TABLES_CREATED'] = 'TRUE'

def drop_db(app):
    with app.app_context():
        db.create_all()