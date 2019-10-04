from flask import Flask, render_template
import requests
import random

app = Flask(__name__)

# a list of regions in prep for the uinames API
regions = ['australia', 'canada', 'denmark', 'england', 'ireland', 'sweden', 'switzerland', 'united states']

# a dict of race in prep of Robohash
race = {
    "robots": "set1",
    "monsters": "set2",
    "advanced_robots": "set3",
    "kittens": "set4"
}

users = []


@app.route("/")
def index():
    return render_template("index.html")


def generate_users_and_photo(region: str):
    res = requests.get("https://uinames.com/api", params={"region": region})


def random_region(list: list):
    region = random.choice(list)
    return region




if __name__ == "__main__":
    app.run(debug=True)
