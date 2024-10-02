from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.orm import validates

from sqlalchemy.ext.hybrid import hybrid_property

from config import db, bcrypt

class Endpoint(db.Model, SerializerMixin):
     __tablename__ = 'endpoints'

     id = db.Column(db.Integer, primary_key=True, nullable=False)
     lines = db.Column(db.String)
     endpoint = db.Column(db.String)

     station_endpoints = db.relationship('StationEndpoint', back_populates='endpoints')

     def __repr__(self):
          return f'<Endpoint {self.lines}, {self.endpoint}>'