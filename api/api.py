from flask import *
from flask import request
from time import sleep
import random

app = Flask(__name__, static_path="")

most_recent_point = 0

@app.route('/', methods=["GET"])
def index_route():
    return render_template('index.html')

@app.route('/graph', methods=["POST"])
def graph():
    most_recent_point = request.form['point']

    print '----------'
    print most_recent_point
    print '----------'

    return jsonify(**{
            'status': 'okay'
        })

@app.route('/point', methods=["GET"])
def point():
    random_number = random.randint(0, 100)
    return jsonify(**{
            'data': random_number
        })

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
