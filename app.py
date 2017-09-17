from flask import Flask, request, jsonify, render_template, send_from_directory
from espnff import League
from flask_cors import CORS
import jsonpickle
app = Flask(__name__, static_folder='static', static_url_path='')
CORS(app)

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

@app.route("/api/v1/matchup")
def get_matchup():
    dot = League(dot_id, year)
    bob = League(bob_id, year)
    dot_score = dot.scoreboard()
    bob_score = bob.scoreboard()
    
    leagues = {
        bob: bob,
        dot: dot
    }
    matchups = {
        dot: dot_score,
        bob: bob_score
    }
    data = {
        'leagues': leagues,
        'matchups': matchups
    }
    return jsonpickle.encode(data)

@app.route('/robots.txt')
@app.route('/sitemap.xml')
def static_from_root():
    return send_from_directory(app.static_folder, request.path[1:])


if __name__ == "__main__":
    app.run(host='0.0.0.0')