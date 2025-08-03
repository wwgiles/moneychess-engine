import logging
import json
import azure.functions as func
from function_app import app
# 

@app.function_name(name="game-history")
@app.route(route="game-history")
def game_history(req: func.HttpRequest) -> func.HttpResponse:

    return func.HttpResponse("success")