from flask import Flask
from flask import request
import random

app = Flask(__name__)

most_recent_point = 0

@app.route('/graph', methods=["POST"])
def graph():
    most_recent_point = request.form['point']

@app.route('/point', methods=["GET"])
def point():
    return random.randint(0, 100)

if __name__ == '__main__':
    app.run()
