from flask import Flask, jsonify
from espnff import League
app = Flask(__name__)

dot_id = 1507319
bob_id = 1477590
year = 2017

@app.route("/")
def main():
    return "hello schumacher fantasy football"

@app.route("/teams")
def teams():
    dot = League(dot, year)
    bob = League(bob, year)
    names = [team.team_name for team in dot.teams]
    return jsonify(names)
    
if __name__ == "__main__":
    app.run(host='0.0.0.0')