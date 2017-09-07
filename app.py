from flask import Flask, jsonify, render_template
from espnff import League
app = Flask(__name__)

dot_id = 1507319
bob_id = 1477590
year = 2017


@app.route("/")
def main():
    dot = League(dot_id, year)
    bob = League(bob_id, year)

    return render_template('teams.html', bob_teams = bob.teams, dot_teams = dot.teams)

if __name__ == "__main__":
    app.run(host='0.0.0.0')