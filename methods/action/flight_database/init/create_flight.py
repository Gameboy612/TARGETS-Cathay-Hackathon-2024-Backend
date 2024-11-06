from methods._utilities.default_responses import SuccessResponse
from methods.action.flight_database.classes.flights import flights


PLANE_MAP = {
  "data": [
    {
      "type": 'ConstantSeatsTile',
      "rows": 32,
      "columns": 6,
      "default_row_spacing": 0,
      "default_column_spacing": 0,
  
      "starting_row_number": 1,
      "starting_column_number": 1,
  
      "custom_row_spacing": [
        {"index": 12, "spacing": 30},
        {"index": 13, "spacing": 30},
      ],
      
      "custom_column_spacing": [
        {"index": 4, "spacing": 40},
      ],
  
      "removed_seat_ids": [
        {"row": 32, "column": 1},
        {"row": 32, "column": 4},
        {"row": 32, "column": 5},
        {"row": 32, "column": 6},
      ],
  
      "special_seats": [],
    }
  ]
}


def create_flight(flightid: int, plane_map = PLANE_MAP) -> dict:
    """Creates a flight object for the associated flightid.

    Args:
        flightid (int): flightid.

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

    PASSENGER_DETAILS = {}

    for data in plane_map["data"]:
        for i in range(data["default_row_spacing"], data["default_row_spacing"] + data["rows"]):
            PASSENGER_DETAILS[str(i)] = {}

    res = flights.update(str(flightid), {
        "_id": str(flightid),
        "planeMap": plane_map,
        "passengerDetails": PASSENGER_DETAILS
        })

    return SuccessResponse({
        'flight': res["data"]["flight"]
    })
    