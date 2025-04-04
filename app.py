# BRONNEN: https://battlecats.miraheze.org/wiki/Enemy_Dictionary (1/04/2025)
#          https://chatgpt.com/ (01/04/2025) --> gebruikt om te filteren uit githubfile en ordenen.
#          https://github.com/TMZ-429/bcc/blob/main/enemies.json (31/03/2025) --> inspiratie
#          https://www.w3schools.com/html/html_tables.asp (04/04/2025)
#               https://www.w3schools.com/html/tryit.asp?filename=tryhtml_table_intro (04/04/2025)
#               https://www.youtube.com/watch?v=e62D-aayveY&list=PLP9IO4UYNF0VdAajP_5pYG-jG2JRrG72s (04/04/2025)
#       De URL van mijn GitHub-repository met het JSON-bestand.
#           https://my-json-server.typicode.com/WonterRobter/battle-cats-enemies



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
