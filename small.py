from flask import Flask, render_template, jsonify
import json, os

app = Flask(__name__,
            static_folder="./dist/static",
            template_folder="./dist"
            )


def get_file(name):
    base = os.path.dirname(__file__)
    with open(os.path.join(base,name)) as f:
        data = json.load(f)
    return data


@app.route('/api/keywords.json')
def keywords():
    data = get_file('keywords.json')
    return jsonify(data)


@app.route('/api/player_a_d.json')
def player_a_d():
    data = get_file('player_a_d.json')
    return jsonify(data)



@app.route('/api/keywordss.json')
def keywordss():
    data = get_file('keywordss.json')
    return jsonify(data)


@app.route('/api/attack_defense.json')
def attack_defense():
    data = get_file('attack_defense.json')
    return jsonify(data)


@app.route('/api/team_s_r_a.json')
def s_r_a():
    data = get_file('s-r-a.json')
    return jsonify(data)


@app.route('/api/player_scatter.json')
def scatter():
    data = get_file('player_scatter.json')
    return jsonify(data)


@app.route('/api/parallel.json')
def parallel():
    data = get_file('cham_team_home_road.json')
    return jsonify(data)


@app.route('/api/team_data.json')
def team_data():
    data = get_file('team_data.json')
    return jsonify(data)


@app.route('/api/players_time.json')
def players_time():
    data = get_file('players_time.json')
    return jsonify(data)


@app.route('/api/team_rank.json')
def team_rank_data():
    data = get_file('rank.json')
    return jsonify(data)


@app.route('/api/player_geo.json')
def player_geo():
    data = get_file('players_geo.json')
    return jsonify(data)


@app.route('/api/players_score.json')
def players_prime():
    data = get_file('players_score.json')
    return jsonify(data)


@app.route('/api/top_score_shot.json')
def top_shot_score():
    data = get_file('top_pie.json')
    return jsonify(data)


@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def hello_world(path):
    return render_template('index.html')


if __name__ == '__main__':
    app.run()
