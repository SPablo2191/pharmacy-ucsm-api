from flask import Flask
from database.db import initialize_db
from config import config
app = Flask(__name__)
config(app=app)
initialize_db(app=app)
@app.route('/')
def index():
    return "hola"


if __name__ == "__main__":
    app.run(debug=True)