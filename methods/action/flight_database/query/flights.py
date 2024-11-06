

from methods._utilities.default_responses import ErrorResponse, SuccessResponse
from methods.action.flight_database.init.create_flight import create_flight
from methods.action.flight_database.classes.flights import flights

def findFlightByFlightID(
    flightid: int
) -> dict:
    """Gets Flights from flightid.

    Args:
        flightid (int): Input flightid.

    Returns:
        dict: Response, formatted as shown below.

        ```
        {
            "success": bool,
            "response": str,
            "data": {
                "flight": flights
            }
        }
        ```
    """

    flightlist = flights.query(filter={'_id': flightid}, limit=1)
    if len(flightlist) == 0:
        return create_flight(flightid)
    
    return SuccessResponse({
        "flight": flightlist[0]
        })
