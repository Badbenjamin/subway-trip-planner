
from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.orm import validates

from sqlalchemy.ext.hybrid import hybrid_property

from config import db, bcrypt



# # create engine, allows database connectivity
# engine = create_engine(os.environ['DATABASE_URI'], echo=True)

# station data from https://data.ny.gov/Transportation/MTA-Subway-Stations/39hk-dx4f/about_data
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
    # start_stops = db.relationship('Route', back_populates='start_stop')
    # end_stops = db.relationship('Route', back_populates='end_stop')

    serialize_rules=['-station_endpoints.stations', '-my_stops.my_stop']

    def __repr__(self):
         return f'<Station {self.stop_name}, {self.gtfs_stop_id} {self.daytime_routes}>'
    
class Endpoint(db.Model, SerializerMixin):
     __tablename__ = 'endpoints'

     id = db.Column(db.Integer, primary_key=True, nullable=False)
     lines = db.Column(db.String)
     endpoint = db.Column(db.String)

     station_endpoints = db.relationship('StationEndpoint', back_populates='endpoints')

     def __repr__(self):
          return f'<Endpoint {self.lines}, {self.endpoint}>'

class StationEndpoint(db.Model, SerializerMixin):
    __tablename__ = 'station_endpoints'

    id = db.Column(db.Integer, primary_key=True, nullable=False)
    route = db.Column(db.String)
    station_name = db.Column(db.String)
    station_id = db.Column(db.Integer, db.ForeignKey('stations.id'), nullable=False)
    endpoint_id = db.Column(db.Integer, db.ForeignKey('endpoints.id'), nullable=False)

    stations = db.relationship('Station', back_populates='station_endpoints')
    endpoints = db.relationship('Endpoint', back_populates='station_endpoints')

    serialize_rules=['-stations.station_endpoints', '-endpoints.station_endpoints']

    def __repr__(self):
          return f'<StationEndpoint {self.station_id}, {self.route}, {self.station_name}, {self.endpoint_id}>'

class Rider(db.Model, SerializerMixin):
    __tablename__ = "riders"

    id = db.Column(db.Integer, primary_key=True, nullable=False)
    username = db.Column(db.String, nullable=False)
    _password_hash = db.Column(db.String)
    fav_subway_activity = db.Column(db.String)
    my_stop_id = db.Column(db.Integer, db.ForeignKey('stations.id')) 

    my_stop = db.relationship('Station', uselist=False, back_populates='my_stops')
    # routes = db.relationship('Route', back_populates='rider')

    serialize_rules=['-stations.my_stops', '-my_stop.my_stops',]

    def __repr__(self):
          return f'<Rider {self.username}, {self.my_stop}>'
    
class Route(db.Model, SerializerMixin):
    __tablename__ = "routes"

    id = db.Column(db.Integer, primary_key=True, nullable=False)
    route_name = db.Column(db.String, nullable=False)
    route_type = db.Column(db.String)
    # rider_id = db.Column(db.Integer, db.ForeignKey('riders.id'))
    # start_stop_id = db.Column(db.Integer, db.ForeignKey('stations.id'))
    # end_stop_id = db.Column(db.Integer, db.ForeignKey('stations.id'))

    # rider = db.relationship('Rider', back_populates='routes')
    # start_stop = db.relationship('Station', back_populates='start_stops')
    # end_stop = db.relationship('Station', back_populates='end_stops')

    def __repr__(self):
          return f'<Route {self.route_name}, {self.rider}>'

class Journey(object):
     
     def __init__(self, start_station, end_station, shared_stations = []):
     
        self.start_station = start_station
        self.end_station = end_station
        self.shared_stations = []
     
     def __repr__(self):
          return f'<Journey {self.start_station}, {self.end_station}, {self.shared_stations}>'