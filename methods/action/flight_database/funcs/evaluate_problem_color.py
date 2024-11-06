from methods.action.flight_database.constants.problems import ASSISTANCE_REQUIRED, BODY_TEMPERATURE_ANOMALY
from settings.colors import BLUE, GREEN, ORANGE, RED, YELLOW


def _loop_in_list(keys, L):
    for key in keys:
        if key in L:
            return True
    return False

def evaluate_problem_color(
    problem_list: list[str]
) -> str:
    if _loop_in_list([
        BODY_TEMPERATURE_ANOMALY,
    ], problem_list):
        return RED
    
    
    if _loop_in_list([
        ASSISTANCE_REQUIRED,
    ], problem_list):
        return BLUE
    
    if len(problem_list) >= 2:
        return ORANGE
    
    if len(problem_list) == 1:
        return YELLOW
    
    return GREEN