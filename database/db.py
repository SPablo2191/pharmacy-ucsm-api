from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

ma = Marshmallow()
db = SQLAlchemy()


def initialize_db(app):
    db.init_app(app)

def init_app(app):
    ma.init_app(app)