from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

ma = Marshmallow()
db = SQLAlchemy()


def initialize_db(app):
    db.init_app(app)


def add_engine(app):
    with app.app_context():
        engine = db.create_engine(app.config['SQLALCHEMY_DATABASE_URI'])
        db.session.configure(bind=engine)   

def init_app(app):
    ma.init_app(app)