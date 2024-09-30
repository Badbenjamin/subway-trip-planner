
from config import app
from flask import session

from config import app, db, SerializerMixin
from models import Station, Journey

import pprint
import requests
from datetime import datetime, timedelta
from google.transit import gtfs_realtime_pb2


@app.route('/')
def root():
    return '<h1>welcome 2 da train app</h>'

@app.route('/api/stations')
def get_all_stations():
    # stations = AllSubwayStations.query.all()
    return [station.to_dict() for station in Station.query.all()], 200

@app.route('/api/station_name/<string:station_id>')
def get_station(station_id):
    station = Station.query.filter(Station.gtfs_stop_id == station_id).first()
    return station.to_dict()

@app.route('/api/plan_trip/<string:start_stop_id>/<string:end_stop_id>')
def plan_trip(start_stop_id, end_stop_id):
    start_station = Station.query.filter(Station.gtfs_stop_id == start_stop_id).first()
    end_station = Station.query.filter(Station.gtfs_stop_id == end_stop_id).first()
    endpoints = get_endpoints(start_station, end_station)
    train_data = request_train_data(endpoints)
    filtered_trains = filter_trains(train_data, start_station, end_station)
    for train in filtered_trains:
        print(train.trip_update.trip.trip_id)
    new_journey = {
        "start_station" : start_station.stop_name,
        "end_station" : end_station.stop_name,
        "shared_stations" : []
    }
    return new_journey, 200

def get_endpoints(start_station, end_station):
    endpoints = []
    for endpoint in start_station.station_endpoints:
        endpoints.append(endpoint.endpoints.endpoint)
    for endpoint in end_station.station_endpoints:
        endpoints.append(endpoint.endpoints.endpoint)
    return(set(endpoints))

def request_train_data(endpoints):
    for endpoint in endpoints:
        feed = gtfs_realtime_pb2.FeedMessage()
        response = requests.get(endpoint)
        feed.ParseFromString(response.content)
        return feed

# get trains where start stop is before end stop
def filter_trains(train_data, start_station, end_station):
    filtered_trains = []
    for train in train_data.entity: 
        if train.HasField('trip_update'):
            stops = []
            for stop in train.trip_update.stop_time_update:
                stops.append(stop.stop_id[:-1])
            if start_station.gtfs_stop_id in stops and end_station.gtfs_stop_id in stops and stops.index(start_station.gtfs_stop_id) < stops.index(end_station.gtfs_stop_id):
                filtered_trains.append(train)
    return(filtered_trains)

if __name__ == "__main__":
    app.run(port=5555, debug=True)