


from methods._utilities.default_responses import ErrorResponse
from methods.action.flight_database.classes.flights import flights
from methods.action.flight_database.funcs.evaluate_problem_color import evaluate_problem_color
from methods.action.flight_database.query.flights import findFlightByFlightID
from settings.colors import GREEN

from flask_socketio import Namespace, emit, join_room, leave_room

def update_passenger(flightid: int, seatId: tuple[int, str], update: dict):
    """Updates MongoDB passenger data, then sends a socketio update to the flightid room.

    Args:
        flightid (int): ID of the flight
        seatId (tuple[int, str]): row, column
    """

    flights.query(flightid)


def add_passenger_problem_flag(flightid: str, seatId: tuple[int, str], flag: str):
    """Adds a problem flag to the passenger in the given seat.

    Args:
        flightid (int): ID of the flight
        seatId (tuple[int, str]): row, column
        flag (str): The problem flag to add
    """

    res = findFlightByFlightID(flightid)
    
    if not res["success"]:
        return ErrorResponse("Flight not found.")
    
    flight = res["data"]["flight"]

    if str(seatId[0]) not in flight["passengerDetails"]:
        return ErrorResponse("Seat row not found.")

    # Create the object
    if seatId[1] not in flight["passengerDetails"][str(seatId[0])]:
        flight["passengerDetails"][str(seatId[0])][seatId[1]] = {
            "color": GREEN,
            "problems": [],
        }

    # Add the flag if it is not already present.
    if flag not in flight["passengerDetails"][str(seatId[0])][seatId[1]]["problems"]:
        flight["passengerDetails"][str(seatId[0])][seatId[1]]["problems"].append(flag)

    flight["passengerDetails"][str(seatId[0])][seatId[1]]["color"] = evaluate_problem_color(
        flight["passengerDetails"][str(seatId[0])][seatId[1]]["problems"])
    
    res = flights.update(flightid, flight)

    if not res["success"]:
        return ErrorResponse("Failed to update passenger problem flag.")

    # Sockets
    OUTPUT_DATA = {"path": ["passengerDetails", str(seatId[0]), seatId[1]], "data": flight["passengerDetails"][str(seatId[0])][seatId[1]]}

    emit("update_flight", OUTPUT_DATA, to=flightid, namespace='/endpoint')


    return res



def remove_passenger_problem_flag(flightid: str, seatId: tuple[int, str], flag: str):
    """Adds a problem flag to the passenger in the given seat.

    Args:
        flightid (int): ID of the flight
        seatId (tuple[int, str]): row, column
        flag (str): The problem flag to add
    """

    res = findFlightByFlightID(flightid)
    
    if not res["success"]:
        return ErrorResponse("Flight not found.")
    
    flight = res["data"]["flight"]

    if str(seatId[0]) not in flight["passengerDetails"]:
        return ErrorResponse("Seat row not found.")

    # Create the object
    if seatId[1] not in flight["passengerDetails"][str(seatId[0])]:
        flight["passengerDetails"][str(seatId[0])][seatId[1]] = {
            "color": GREEN,
            "problems": [],
        }

    # Add the flag if it is not already present.
    if flag in flight["passengerDetails"][str(seatId[0])][seatId[1]]["problems"]:
        flight["passengerDetails"][str(seatId[0])][seatId[1]]["problems"].remove(flag)

    flight["passengerDetails"][str(seatId[0])][seatId[1]]["color"] = evaluate_problem_color(
        flight["passengerDetails"][str(seatId[0])][seatId[1]]["problems"])
    
    res = flights.update(flightid, flight)

    if not res["success"]:
        return ErrorResponse("Failed to update passenger problem flag.")

    # Sockets
    OUTPUT_DATA = {"path": ["passengerDetails", str(seatId[0]), seatId[1]], "data": flight["passengerDetails"][str(seatId[0])][seatId[1]]}

    emit("update_flight", OUTPUT_DATA, to=flightid, namespace='/endpoint')


    return res