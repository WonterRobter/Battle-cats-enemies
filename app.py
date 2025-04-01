from flask import Flask, render_template
import requests

app = Flask(__name__)

API_URL = "https://my-json-server.typicode.com/WonterRobter/battle-cats-enemies/enemies"

@app.route("/")
def home():
    response = requests.get(API_URL)
    if response.status_code == 200:
        data = response.json()
    else:
        data = []
    return render_template("index.html", enemies=data)

if __name__ == "__main__":
    app.run(debug=True)
