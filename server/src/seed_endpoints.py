from models import LineGtfsEndpoint
from config import app, db


def add_endpoints():

    ace = LineGtfsEndpoint(
        lines = "ACE",
        endpoint = "https://api-endpoint.mta.info/Dataservice/mtagtfsfeeds/nyct%2Fgtfs-ace"
    )

    g = LineGtfsEndpoint(
        lines = "G",
        endpoint = "https://api-endpoint.mta.info/Dataservice/mtagtfsfeeds/nyct%2Fgtfs-g"
    )

    nqrw = LineGtfsEndpoint(
        lines = "NQRW",
        endpoint = "https://api-endpoint.mta.info/Dataservice/mtagtfsfeeds/nyct%2Fgtfs-nqrw"
    )

    one234567 = LineGtfsEndpoint(
        lines = "1234567",
        endpoint = "https://api-endpoint.mta.info/Dataservice/mtagtfsfeeds/nyct%2Fgtfs"
    )

    bdfm = LineGtfsEndpoint(
        lines = "BDFM",
        endpoint = "https://api-endpoint.mta.info/Dataservice/mtagtfsfeeds/nyct%2Fgtfs"
    )

    jz = LineGtfsEndpoint(
        lines = "JZ",
        endpoint = "https://api-endpoint.mta.info/Dataservice/mtagtfsfeeds/nyct%2Fgtfs-jz"
    )

    l = LineGtfsEndpoint(
        lines = "L",
        endpoint = "https://api-endpoint.mta.info/Dataservice/mtagtfsfeeds/nyct%2Fgtfs-jz"
    )

    sir = LineGtfsEndpoint(
        lines = "SIR",
        endpoint = "https://api-endpoint.mta.info/Dataservice/mtagtfsfeeds/nyct%2Fgtfs-si"
    )

    endpoints = [ace, g, nqrw, one234567, bdfm, jz, l, sir]
    db.session.add_all(endpoints)
    db.session.commit()

if __name__== "__main__":
    with app.app_context():
        add_endpoints()