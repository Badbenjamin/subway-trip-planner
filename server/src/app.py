
from config import app
from flask import session, request


from config import app, db, SerializerMixin
from models import Station, Journey, Rider


import pprint
import requests
from datetime import datetime, timedelta
from google.transit import gtfs_realtime_pb2

ct = datetime.now()

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

@app.route('/api/login', methods=['POST'])
def login():
    data = request.get_json()
    print(data)
    # query db for user
    rider = Rider.query.filter(Rider.username == data['username']).first()
    print(rider)
    if rider is None:
        return {'error' : 'login failed'}, 401
    # authenticate here
    session['user_id'] = rider.id
    print(session)
    return rider.to_dict(), 200

@app.route('/api/check_session')
def check_session():
    user = Rider.query.filter(Rider.id == session['user_id']).first()
    print('checking session')
    if user is None:
        return {'not logged in'}, 401
    else:
        return user.to_dict(), 200


@app.route('/api/plan_trip/<string:start_stop_id>/<string:end_stop_id>')
def plan_trip(start_stop_id, end_stop_id):
    start_station = Station.query.filter(Station.gtfs_stop_id == start_stop_id).first()
    end_station = Station.query.filter(Station.gtfs_stop_id == end_stop_id).first()
    # right now just one endpoint, maybe split into start and dest endpoints
    endpoints = get_endpoints(start_station, end_station)
    train_data = request_train_data(endpoints)
    filtered_trains = filter_trains_for_stations(train_data, start_station, end_station)
    current_trains = filter_for_current_trains_at_start(filtered_trains, start_station)
    sorted_trains = sort_trains_by_arrival_at_dest(current_trains, start_station, end_station)
    trains_for_react = prep_data_for_react(sorted_trains)
    # print(trains_for_react)
    return trains_for_react, 200

# maybe make two lists of endpoints for start and end?
def get_endpoints(start_station, end_station):
    endpoints = []
    for endpoint in start_station.station_endpoints:
        endpoints.append(endpoint.endpoints.endpoint)
    for endpoint in end_station.station_endpoints:
        endpoints.append(endpoint.endpoints.endpoint)
    return(set(endpoints))

# maybe append endpoints to list? sort by start station and end station? for when a transfer exitsts.
def request_train_data(endpoints):
    for endpoint in endpoints:
        feed = gtfs_realtime_pb2.FeedMessage()
        response = requests.get(endpoint)
        feed.ParseFromString(response.content)
        return feed

# get trains where start stop is before end stop
def filter_trains_for_stations(train_data, start_station, end_station):
    filtered_trains = []
    for train in train_data.entity: 
        if train.HasField('trip_update'):
            stops = []
            # stops list contains each trains stop array. used to determine if start stop is before end stop
            for stop in train.trip_update.stop_time_update:
                stops.append(stop.stop_id[:-1])
            if (start_station.gtfs_stop_id in stops and end_station.gtfs_stop_id in stops and stops.index(start_station.gtfs_stop_id) < stops.index(end_station.gtfs_stop_id)):
                filtered_trains.append(train)
    return(filtered_trains)

# convert 10 digit POSIX timestamp used in feed to readable format
def convert_timestamp(timestamp):
    return datetime.fromtimestamp(timestamp)

# converts seconds to delta time type
def convert_seconds(seconds):
    return timedelta(seconds = seconds)

def time_difference(first_time, second_time):
    detla_time = second_time - first_time
    return detla_time

# maybe combine with filter for stations later....
def filter_for_current_trains_at_start(trains, start_station):
    filtered_trains = []
    for train in trains:
        for stop in train.trip_update.stop_time_update:
            # Filter for station and arrival time in future
            if stop.stop_id[:-1] == start_station.gtfs_stop_id and time_difference(ct, convert_timestamp(stop.arrival.time)) > convert_seconds(30):
                filtered_trains.append(train)
    return filtered_trains
            
def sort_trains_by_arrival_at_dest(trains, start_station, end_station):
    # trains will be sorted into a list based on destination arrival time
    trains_with_arrival = []
    for train in trains:
        train_with_arrival = {
        "start_station_name" : start_station.stop_name,
        "start_station_arrival" : None,
        "end_station_name" : end_station.stop_name,
        "end_station_arrival" : None,
        "route" : train.trip_update.trip.route_id,
        "last_station_name" : train.trip_update.stop_time_update[0].stop_id[:-1],
        "last_station_departure" : train.trip_update.stop_time_update[0].departure.time,
        "direction_label" : train.trip_update.stop_time_update[0].stop_id[-1]
    }
        for stop in train.trip_update.stop_time_update:
            if stop.stop_id[:-1] == start_station.gtfs_stop_id:
                train_with_arrival['start_station_arrival'] = stop.arrival.time
            elif stop.stop_id[:-1] == end_station.gtfs_stop_id:
                train_with_arrival['end_station_arrival'] = stop.arrival.time
        trains_with_arrival.append(train_with_arrival)
    # sorted(iterable, cmp=None, key=None, reverse=False)
    trains_by_dest_arrival =  sorted(trains_with_arrival, key=lambda d: d['end_station_arrival'])
    return trains_by_dest_arrival
    
def prep_data_for_react(sorted_trains):
    trains_for_react = []
    for train in sorted_trains:
        print(train['direction_label'])
        if train['direction_label'] == "N":
            train['direction_label'] = Station.query.filter(Station.gtfs_stop_id == train['last_station_name']).first().north_direction_label
        if train['direction_label'] == "S":
            train['direction_label'] = Station.query.filter(Station.gtfs_stop_id == train['last_station_name']).first().south_direction_label
        train['start_station_arrival'] = str(convert_timestamp(train['start_station_arrival']))
        train['end_station_arrival'] = str(convert_timestamp(train['end_station_arrival']))
        train['last_station_departure'] = str(convert_timestamp(train['last_station_departure']))
        train['last_station_name'] = Station.query.filter(Station.gtfs_stop_id == train['last_station_name']).first().stop_name
        trains_for_react.append(train)
    return trains_for_react





if __name__ == "__main__":
    app.run(port=5555, debug=True)