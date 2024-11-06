import json
from flask import request
from flask_socketio import Namespace, emit, join_room, leave_room

from methods._utilities.get_room_name import getUserRoom
from methods.action.flight_database.methods.update_passenger import add_passenger_problem_flag, remove_passenger_problem_flag

class EndPointNamespace(Namespace):
    def on_connect(self):
        pass

    def on_disconnect(self):
        pass

    def on_my_event(self, data):
        emit('message', data)
        print(request.sid)
        print(data)


    def on_messages(self, data):
        content = json.loads(data)

    def on_join_flightroom(self, data):
        
        join_room(data)
        emit('room_update', {"state": "join", "roomid": data})

    def on_update_flight(self, data):
        print(data)


    def on_add_passenger_problem_flag(self, data):
        print(data)
        add_passenger_problem_flag(data["flightid"], data["seatid"], data["flag"])
        
    def on_remove_passenger_problem_flag(self, data):
        print(data)
        remove_passenger_problem_flag(data["flightid"], data["seatid"], data["flag"])
        

