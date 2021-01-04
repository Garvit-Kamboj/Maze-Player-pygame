import json
from os import path
from flask import Flask, request, render_template
from models.score_manager import ScoreManager
from models.score import Score


app = Flask(__name__)
score_manager = ScoreManager()

@app.route('/', methods=["GET"])
def list_all_scores():
    file_path = path.join(path.dirname( __file__ ), 'game_data', 'database.json')
    highscore_list = ScoreManager()
    with open(file_path, 'r') as file:
        data = json.load(file)
        for each in data['scores']:
            n = Score(
                each['name'],
                int(each['score'])
            )
            highscore_list.add_score(n)

    return render_template("table.html", scores=highscore_list.scores)

if __name__ == '__main__':
    app.run(debug=True)
