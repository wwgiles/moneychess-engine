import logging
import json
import azure.functions as func
from function_app import app
# 

@app.function_name(name="health")
@app.route(route="health")
def health(req: func.HttpRequest) -> func.HttpResponse:
    return func.HttpResponse(
        json.dumps({"status": "ok"}),
        mimetype="application/json"
    )