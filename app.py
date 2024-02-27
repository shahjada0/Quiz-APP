from flask import Flask, render_template, jsonify
import requests

app = Flask(__name__)

API_URL = "https://opentdb.com/api.php?amount=10&type=multiple"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/quiz')
def quiz():
    return render_template('quiz.html')

@app.route('/questions')
def get_questions():
    response = requests.get(API_URL)
    data = response.json()
    questions = data['results']
    return jsonify(questions)

if __name__ == '__main__':
    app.run(debug=True)
