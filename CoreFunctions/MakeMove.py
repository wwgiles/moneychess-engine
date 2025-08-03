import logging
import json
import azure.functions as func
#import chess
from function_app import app
# send a JSON body with gameID, currentFen, moveUci

@app.function_name(name="make-move")
@app.route(route="make-move")
def move_piece(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request for a move.')

    return func.HttpResponse("success")
