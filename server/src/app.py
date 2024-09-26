import os
from flask import Flask, request, session
from flask_migrate import Migrate
from sqlalchemy_serializer import SerializerMixin
from models import db
from flask_cors import CORS

# 
app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'squlite:///app.db'
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['DATABASE_URI']
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# need to set this in env file
app.secret_key = os.environ['SECRET_KEY']

# initialize sqlalchemy plugin 
db.init_app(app)
# initialize alembic aka flask migrate
Migrate(app, db)

CORS(app)

@app.route('/')
def root():
    return '<h1>welcome 2 da train app</h>'