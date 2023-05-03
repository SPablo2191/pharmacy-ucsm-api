from flask import Flask
from database.db import initialize_db
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
initialize_db(app=app)
@app.route('/')
def index():
    return "Hello world"


if __name__ == "__main__":
    app.run()