from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.orm import validates

from sqlalchemy.ext.hybrid import hybrid_property

from config import db, bcrypt

from rider import Rider

class Route(db.Model, SerializerMixin):
    __tablename__ = "routes"

    id = db.Column(db.Integer, primary_key=True, nullable=False)
    route_name = db.Column(db.String, nullable=False)
    route_type = db.Column(db.String)
    rider_id = db.Column(db.Integer, db.ForeignKey('riders.id'))
    start_stop_id = db.Column(db.Integer, db.ForeignKey('stations.id'))
    end_stop_id = db.Column(db.Integer, db.ForeignKey('stations.id'))

    rider = db.relationship('Rider', foreign_keys=[Rider.id], back_populates='routes')
    start_stop = db.relationship('Station', foreign_keys=[start_stop_id], back_populates='start_stops')
    end_stop = db.relationship('Station', foreign_keys=[end_stop_id], back_populates='end_stops')

    serialize_rules=['-rider.routes', '-station.start_stops', '-station.end_stops']

    def __repr__(self):
          return f'<Route {self.route_name}, {self.rider}>'