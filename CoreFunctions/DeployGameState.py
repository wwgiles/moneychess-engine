import logging
import json
import azure.functions as func
from function_app import app
# 

@app.function_name(name="deploy-game-state")
@app.route(route="deploy-game-state")
def deploy_game_state(req: func.HttpRequest) -> func.HttpResponse:

    return func.HttpResponse("success")