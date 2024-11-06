from methods._utilities.default_responses import ErrorResponse, SuccessResponse
from methods.action.flight_database.query.flights import findFlightByFlightID

def get_all_state(flightid: int) -> dict:
    res = findFlightByFlightID(flightid)
    
    if not res["success"]:
        return ErrorResponse("Flight not found")

    flight = res["data"]["flight"]

    return SuccessResponse({"flight": flight})

