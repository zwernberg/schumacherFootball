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
    dot_scoreboard = dot.scoreboard()
    bob_scoreboard = bob.scoreboard()

    return render_template('matchups.html', bob = bob, dot = dot, bob_scoreboard = bob_scoreboard, dot_scoreboard = dot_scoreboard)

@app.route("/teams")
def teams():
    dot = League(dot_id, year)
    bob = League(bob_id, year)

    return render_template('teams.html', bob=bob, dot=dot)
if __name__ == "__main__":
    app.run(host='0.0.0.0')