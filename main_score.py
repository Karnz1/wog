from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/')
def score_server():
    score = 0
    with open('Scores.txt', 'r') as f:
        score += int(f.readline())
    if isinstance(score, int):
        return render_template('index.html', score=score)
    else:
        return render_template('index.html', score="Error opening scores file")


app.run(host='0.0.0.0', debug=True, port=8777)

