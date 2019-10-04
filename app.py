from flask import Flask, render_template
import requests
import random

app = Flask(__name__)

regions = ['australia', 'canada', 'denmark', 'england', 'ireland', 'sweden', 'switzerland', 'united states']


@app.route("/")
def index():
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)
