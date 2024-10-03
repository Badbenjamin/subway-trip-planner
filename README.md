# subway-trip-planner

-Subway trip planner is an app that lets you plan a trip between two subway stations.

-It currently only supports trips on the same subway line. 

-Trips with transfers, or trips including stations that are not currently being served (modified service), will yield a blank form. 

-Users can log in and will be able to save their commutes in the future.

-Login with TommyTrains (pw trains123) to explore the user login feature.

## installation

open two terminal windows...

in the first, cd into client and run...

$ npm install

in the second, cd into server and run...

$ pipenv install

then run...

$ pipenv shell

in the virtual environment, cd into src and run...

$ flask run

The app should now load in localhost!