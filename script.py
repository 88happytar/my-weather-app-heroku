import os
import requests

from flask import Flask

app = Flask(__name__)
API_KEY = os.environ.get("API_KEY")
BASE_URL = "https://api.openweathermap.org/data/2.5"
CITY_NAME = "wellington"


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


@app.route("/current")
def current():
    try:
        r = requests.get(f"{BASE_URL}/weather?q={CITY_NAME}&appid={API_KEY}")
        r.raise_for_status()
        return r.json()
    except requests.exceptions.ConnectionError as err:
        return f"Error: {err}"


@app.route("/forecast")
def forecast():
    return requests.get(
        f"{BASE_URL}/onecall?lat={41.2924}&lon={174.7787}&appid={API_KEY}"
    ).json()
