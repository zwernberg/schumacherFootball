from flask import Flask
from espnff import League
app = Flask(__name__)

dot = 1507319
bob = 1477590
year = 2017

@app.route("/")
def main():
    return "hello schumacher fantasy football"

@app.route("/teams")
def teams():
    dot = League(dot, year)
    bob = League(bob, year)
    return (teams[0].team_name)

if __name__ == "__main__":
    app.run(host='0.0.0.0')