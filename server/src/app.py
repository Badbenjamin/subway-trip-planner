
from config import app
from flask import request, session

from config import app, db, SerializerMixin
from models import Station

@app.route('/')
def root():
    return '<h1>welcome 2 da train app</h>'

@app.route('/stations')
def get_all_stations():
    # stations = AllSubwayStations.query.all()
    return [station.to_dict() for station in Station.query.all()]

@app.route('/station_name/<string:station_id>')
def get_station(station_id):
    station = Station.query.filter(Station.gtfs_stop_id == station_id).first()
    return station.to_dict()



if __name__ == "__main__":
    app.run(port=5555, debug=True)