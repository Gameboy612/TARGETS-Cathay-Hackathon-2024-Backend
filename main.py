from flask import Flask, jsonify, request
from flask_cors import CORS
from flask_socketio import SocketIO
from methods.action.flight_database.methods.get_all_state import get_all_state
from settings.paths import ERRORTRACKER_FOLDER, UPLOAD_FOLDER
from socketio_namespace import EndPointNamespace
import os



os.makedirs(ERRORTRACKER_FOLDER, exist_ok=True)

app = Flask(__name__)
CORS(app)

app.secret_key = "hskrgvnauntbu3tbukvgnfjvg"

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


socketio = SocketIO(app, cors_allowed_origins="*")
# https://www.reddit.com/r/flask/comments/mbhqnm/use_sqlalchemy_database_from_another_file/


@app.route("/")
def main():
    return "Please go to /endpoint to submit data"

@app.route("/get_flight/<flightid>", methods=["GET"])
def get_flight(flightid):
    if flightid == -1:
        return jsonify({'error': 'Invalid flightid'})
    return jsonify(get_all_state(flightid))
socketio.on_namespace(EndPointNamespace("/endpoint"))

@app.route("/ping")
def ping():
    socketio.emit('receive_message', {'data': 42}, namespace='/endpoint')
    return "pinged"

if __name__ == "__main__":
    with app.app_context():
        # app.run(host="0.0.0.0", debug=True)
        socketio.run(app, host="0.0.0.0", debug=True, allow_unsafe_werkzeug=True)
