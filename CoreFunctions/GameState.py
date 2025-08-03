import logging
import json
import azure.functions as func
from function_app import app
# 

@app.function_name(name="game-state")
@app.route(route="game-state")
def game_state(req: func.HttpRequest) -> func.HttpResponse:

    return func.HttpResponse("success")