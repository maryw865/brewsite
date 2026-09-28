from flask import Flask, render_template as rt
import requests
import json
import warnings

app = Flask(__name__)


@app.route("/")
@app.route("/home")
def home():
    return rt("home.html", user="Maryann Wilson")


@app.route("/breweries")
def breweries():
    response = requests.get(
        "https://api.openbrewerydb.org/v1/breweries"
    )

    data = json.loads(response.content)

    return rt("breweries.html", content=data)


@app.route("/beer_types")
def beer_types():
    return rt("beer_types.html")


@app.route("/about_us")
def about_us():
    return rt("about.html")


if __name__ == "__main__":
    app.run(debug=True)