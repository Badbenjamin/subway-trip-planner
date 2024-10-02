from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.orm import validates

from sqlalchemy.ext.hybrid import hybrid_property

from config import db, bcrypt

from route import Route

class Station(db.Model, SerializerMixin):
    __tablename__ = 'stations'

    id = db.Column(db.Integer, primary_key=True, nullable=False)
    gtfs_stop_id = db.Column(db.String)
    station_id = db.Column(db.Integer)
    complex_id = db.Column(db.Integer)
    division = db.Column(db.String)
    line = db.Column(db.String)
    stop_name = db.Column(db.String)
    borough = db.Column(db.String)
    cbd = db.Column(db.String)
    daytime_routes = db.Column(db.String)
    structure = db.Column(db.String)
    gtfs_latitude = db.Column(db.String)
    gtfs_longitude = db.Column(db.String)
    north_direction_label = db.Column(db.String)
    south_direction_label = db.Column(db.String)

    station_endpoints = db.relationship('StationEndpoint', back_populates='stations')
    my_stops = db.relationship('Rider', back_populates='my_stop')
    start_stops = db.relationship('Route', foreign_keys=[Route.start_stop_id], back_populates='start_stop')
    end_stops = db.relationship('Route', foreign_keys=[Route.end_stop_id], back_populates='end_stop')

    serialize_rules=['-station_endpoints.stations']

    def __repr__(self):
         return f'<Station {self.stop_name}, {self.gtfs_stop_id} {self.daytime_routes}>'