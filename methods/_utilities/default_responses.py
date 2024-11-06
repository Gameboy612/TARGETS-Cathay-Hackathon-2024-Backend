METHOD_NOT_FOUND = {
        "success": False,
        "response": "Method not found."
    }

def ErrorResponse(message):
    return {
            "success": False,
            "response": message,
        }


def SuccessResponse(data = {}, response = ""):
    """Success Response Template.

    Args:
        data (dict, optional): data. Defaults to {}.
        response (str, optional): response message. Defaults to "".

    Returns:
        dict: Response, formatted as shown below.

        ```
        {
            "success": bool,
            "response": str,
            "data": {
                ...
            }
        }
        ```
    """
    return {
        "success": True,
        "response": response,
        "data": data
    }
