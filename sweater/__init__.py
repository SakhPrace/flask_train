from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///flask_test'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['ENV'] = 'development'
app.config['DEBUG'] = True
app.config['TESTING'] = True
app.secret_key = 'secret string'
db = SQLAlchemy(app)
migrate = Migrate(app, db)

from sweater import models, routes

db.create_all()
