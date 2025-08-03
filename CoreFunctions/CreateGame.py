import logging
import json
import azure.functions as func
from function_app import app
# 

@app.function_name(name="create-game")
@app.route(route="create-game")
def create_game(req: func.HttpRequest) -> func.HttpResponse:

    return func.HttpResponse("success")