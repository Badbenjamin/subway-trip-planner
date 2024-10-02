from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.orm import validates

from sqlalchemy.ext.hybrid import hybrid_property

from config import db, bcrypt

class Rider(db.Model, SerializerMixin):
    __tablename__ = "riders"

    id = db.Column(db.Integer, primary_key=True, nullable=False)
    username = db.Column(db.String, nullable=False)
    _password_hash = db.Column(db.String)
    fav_subway_activity = db.Column(db.String)
    my_stop_id = db.Column(db.Integer, db.ForeignKey('stations.id')) 

    my_stop = db.relationship('Station', uselist=False, back_populates='my_stops')
    routes = db.relationship('Route', back_populates='rider')

    def __repr__(self):
          return f'<Rider {self.username}, {self.my_stop}>'