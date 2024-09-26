
from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.orm import validates

from sqlalchemy.ext.hybrid import hybrid_property

from config import db, bcrypt



# # create engine, allows database connectivity
# engine = create_engine(os.environ['DATABASE_URI'], echo=True)

# station data from https://data.ny.gov/Transportation/MTA-Subway-Stations/39hk-dx4f/about_data
class AllSubwayStations(db.Model, SerializerMixin):
    __tablename__ = 'all_subway_stations'

    id = db.Column(db.Integer, primary_key=True, nullable=False)
    gtfs_stop_id = db.Column(db.String)
    station_id = db.Column(db.Integer)
    complex_id = db.Column(db.Integer)
    division = db.Column(db.String)
    line = db.Column(db.String)
    stop_name = db.Column(db.String)
    borough = db.Column(db.String)
    cbd = db.Column(db.Boolean)
    daytime_routes = db.Column(db.String)
    structure = db.Column(db.String)
    gtfs_latitude = db.Column(db.Float)
    gtfs_longitude = db.Column(db.Float)
    north_direction_label = db.Column(db.String)
    south_direction_label = db.Column(db.String)

    def __repr__(self):
         return f'<User {self.gtfs_stop_id}, {self.line}>'
