import azure.functions as func
import logging

app = func.FunctionApp(http_auth_level=func.AuthLevel.FUNCTION)

from HelperFunctions.CalculatePoints import calculate_points
import Moves