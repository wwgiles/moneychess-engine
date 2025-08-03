import logging
import json
import azure.functions as func
from function_app import app
# 

@app.function_name(name="valid-moves")
@app.route(route="valid-moves")
def valid_moves(req: func.HttpRequest) -> func.HttpResponse:

    return func.HttpResponse("success")