from flask import *
from flask import request
from flask_socketio import SocketIO, emit
from time import sleep
import random

app = Flask(__name__, static_path="")
socketio = SocketIO(app)

most_recent_point = 0

@app.route('/', methods=["GET"])
def index_route():
    return render_template('index.html')

@app.route('/graph', methods=["POST"])
def graph():
    global most_recent_point
    most_recent_point = int(request.form['point'])

    emit('new_data', most_recent_point)

    return jsonify(**{
            'status': 'okay'
        })

if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0', debug=True)
    # app.run(host='0.0.0.0', debug=True)
