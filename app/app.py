from flask import Flask, render_template
from flask_bootstrap import Bootstrap
import waitress

app = Flask(__name__)
Bootstrap(app)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/map", methods=['GET', 'POST'])
def get_map_page():
    return render_template("map.html")


if __name__ == "__main__":
    waitress.serve(app, host="0.0.0.0", port=5000)
