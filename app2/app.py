import os
from dotenv import load_dotenv
from . import app
from flask import render_template, jsonify
from flask import Flask
from flask_bootstrap import Bootstrap
from flask_cors import CORS
from sqlalchemy import create_engine, text



# INIT APP
app = Flask(__name__)
Bootstrap(app)
CORS(app)

# DB ENGINE
load_dotenv(override=True)
DB_URI = os.getenv("DATABASE_URI")
DB_SCHEMA = os.getenv("DB_SCHEMA")
engine = create_engine(DB_URI)


# HOME PAGE
@app.route("/")
def index():
    return render_template("index.html")


# CARTOGRPHIES PAGE
@app.route("/map", methods=['GET', 'POST'])
def get_map_page():
    return render_template("map.html")

@app.route("/api/stations")
def get_map_data():
    connection = engine.connect()

    query = text(f"""
        SELECT nom, operateur, shop, ST_X(ST_Transform(geometry, 4326)) AS longitude, ST_Y(ST_Transform(geometry, 4326)) AS latitude 
        FROM public.stations
    """)
    result = connection.execute(query)
    result_dict = []
    for row in result :
        result_dict.append(dict(row._asdict()))

    connection.close()

    return jsonify(result_dict)

if __name__ == "__main__":
    app.run(debug=True)