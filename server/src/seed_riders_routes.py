from models import Station, Rider, Route
from config import app, db
import pprint


def add_riders():
    
    tommy = Rider(
    username = "TommyTrains",
    _password_hash = None,
    fav_subway_activity = "Listening to loud music.",

    my_stop = Station.query.first()
    )

    sally = Rider(
    username = "SallySevenTrain",
    _password_hash = None,
    fav_subway_activity = "Fighting with boyfriend.",

    my_stop = Station.query.first()
    )

    sammy = Rider(
    username = "SammySubway",
    _password_hash = None,
    fav_subway_activity = "Smoking cigs.",

    my_stop = Station.query.first()
    )
    print('riders')
    riders = [tommy, sally, sammy]
    db.session.add_all(riders)
    db.session.commit()

def add_routes():
    
    r1 = Route(
        route_name = "Going to work",
        route_type = "work",

        rider = Rider.query.filter(Rider.username == "SammySubway").first(),
        # start_stop = Station.query.filter(Station.station_id == 1).first(),
        # end_stop = Station.query.filter(Station.station_id == 11).first()
    )

    r2 = Route(
        route_name = "Go shopping",
        route_type = "leisure",

        rider = Rider.query.filter(Rider.username == "SallySevenTrain").first(),
        # start_stop = Station.query.filter(Station.station_id == 456).first(),
        # end_stop = Station.query.filter(Station.station_id == 466).first()
    )
    routes = [r1, r2]
    db.session.add_all(routes)
    db.session.commit


with app.app_context():
    add_riders()
    # add_routes()