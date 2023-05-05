from flask import Flask
from database.db import initialize_db,init_app
from database.db_maker import create_db,drop_db
from flask_cors import CORS
from config import config
from flask_restful import Api
from resources.routes import initialize_routes
app = Flask(__name__)
config(app=app)
CORS(app=app)
api = Api(app)
initialize_db(app=app)
init_app(app=app)
create_db(app=app)
initialize_routes(api=api)

@app.route('/')
def index():
    return "hola"


if __name__ == "__main__":
    app.run(debug=True)