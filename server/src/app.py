
from config import app
from flask import request, session

from config import app, db
from models import AllSubwayStations

@app.route('/')
def root():
    return '<h1>welcome 2 da train app</h>'


if __name__ == "__main__":
    app.run(port=5555, debug=True)