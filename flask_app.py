# Flask App
#   Routes
#
#       * `/api/v1.0/top`


# import dependencies
import datetime as dt
import numpy as np
import pandas as pd
import datetime as dt
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session, scoped_session, sessionmaker
from sqlalchemy import create_engine, func
from flask import Flask, jsonify

app = Flask(__name__)

# Create an engine to a SQLite database
engine = create_engine("sqlite:///contributions.sqlite")

# reflect an existing database into a new model
Base = automap_base()

# reflect the tables
Base.prepare(engine, reflect=True)

# Save reference to the tables
Contributions = Base.classes.contributions

# Create our session (link) from Python to the DB
#session = Session(engine)
session = scoped_session(sessionmaker(bind=engine))

# Flask Routes
@app.route("/")
def welcome():
    print("Server received request for 'Home' page...")
    return "<h3>Beto for Texas 2018 Contributions API Routes</h3> <br>" + \
            "/api/v1.0/top<br> JSON of contributions from donors who gave at least $5,000 total."\
            "<br><br>/api/v1.0/&ltlast_name&gt/&ltfirst_name&gt<br> a JSON of contributions from\
            donors with a matching last_name and first_name."

@app.route("/api/v1.0/top")
def top():
    """Return a list of contributions from donors who gave at least $5,000 total"""
#    * Query for the contributions from donors with more than $5,000 aggregate .
#           * Convert the query results to a Dictionary using `date` as the key and `last_name` as the value.
#           * Return the json representation of your dictionary.
    results = session.query(Contributions.last_name, Contributions.first_name, \
                                Contributions.contrib_agg, Contributions.contrib_itemize, \
                                Contributions.contrib_date, Contributions.address_1, \
                                Contributions.address_2, Contributions.city, \
                                Contributions.state, Contributions.zip_code).\
        filter(Contributions.contrib_agg >= "5000").\
        all()

    top_list = []
    for result in results:
        row = {}
        row["last_name"] = result[0]
        row["first_name"] = result[1]
        row["contrib_agg"] = int(result[2])
        row["contrib_itemize"] = int(result[3])
        row["contrib_date"] = result[4]
        row["address_1"] = result[5]
        row["address_2"] = result[6]
        row["city"] = result[7]
        row["state"] = result[8]
        row["zip_code"] = result[9]
        top_list.append(row)

    return jsonify(top_list)


@app.route("/api/v1.0/<last_name>/<first_name>")
def fullname(last_name,first_name):

    fullname_results = session.query(Contributions.last_name, Contributions.first_name, \
                                Contributions.contrib_agg, Contributions.contrib_itemize, \
                                Contributions.contrib_date, Contributions.address_1, \
                                Contributions.address_2, Contributions.city, \
                                Contributions.state, Contributions.zip_code).\
        filter(Contributions.last_name == last_name, \
                Contributions.first_name == first_name).\
        all()

    fullname_list = []
    for fullname_result in fullname_results:
        row = {}
        row["last_name"] = fullname_result[0]
        row["first_name"] = fullname_result[1]
        row["contrib_agg"] = int(fullname_result[2])
        row["contrib_itemize"] = int(fullname_result[3])
        row["contrib_date"] = fullname_result[4]
        row["address_1"] = fullname_result[5]
        row["address_2"] = fullname_result[6]
        row["city"] = fullname_result[7]
        row["state"] = fullname_result[8]
        row["zip_code"] = fullname_result[9]
        fullname_list.append(row)

    return jsonify(fullname_list)

if __name__ == "__main__":
    app.run(debug=True)
