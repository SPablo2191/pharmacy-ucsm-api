from flask import Flask
from database.db import initialize_db
from database.db_maker import create_db
from flask_cors import CORS
from config import config
app = Flask(__name__)
config(app=app)
initialize_db(app=app)
create_db(app=app)
CORS(app=app)
@app.route('/')
def index():
    return "hola"


if __name__ == "__main__":
    app.run(debug=True)